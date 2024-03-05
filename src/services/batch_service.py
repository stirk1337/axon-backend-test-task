from datetime import datetime, date

import sqlalchemy.exc
from sqlalchemy import select, inspect
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.handlers.pydantic_models.batch_model import BatchModelInRus, BatchModelInUpdate
from src.models.batch import Batch


class BatchService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_batch_by_number_and_date(self, number: int, batch_date: date) -> Batch:
        batch = await self.db_session.scalar(
            select(Batch)
            .where(Batch.number == number)
            .where(Batch.batch_date == batch_date)
        )
        return batch

    async def create_batch(self, batch_model: BatchModelInRus):
        batch_args = {
            attr: getattr(batch_model, attr)
            for attr in vars(batch_model)
        }
        batch = await self.get_batch_by_number_and_date(batch_model.number, batch_model.batch_date)
        if batch:
            await self.db_session.delete(batch)
            await self.db_session.commit()
        batch = Batch(**batch_args)
        if batch_model.closing_status:
            batch.closed_at = datetime.now()
        self.db_session.add(batch)
        await self.db_session.commit()

    async def update_batch(self, batch, batch_model: BatchModelInUpdate) -> Batch | None:
        fields_to_update = BatchModelInUpdate.__fields__.keys()
        for attribute in fields_to_update:
            if hasattr(batch_model, attribute):
                value = getattr(batch_model, attribute)
                if value is not None:
                    setattr(batch, attribute, value)

        if batch_model.closing_status is not None:
            batch.closing_status = batch_model.closing_status
            batch.closed_at = datetime.now() if batch_model.closing_status else None

        try:
            await self.db_session.commit()
            await self.db_session.refresh(batch)
        except sqlalchemy.exc.IntegrityError:
            batch = None

        return batch

    async def get_batch_by_id(self, batch_id: int) -> Batch | None:
        batch = await self.db_session.scalar(
            select(Batch)
            .where(Batch.id == batch_id)
            .options(
                selectinload(Batch.products)
            )
        )
        return batch
