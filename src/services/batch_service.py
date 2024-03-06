from datetime import datetime, date
from typing import List

import sqlalchemy.exc
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.handlers.pydantic_models.batch_model import BatchModelInRus, BatchModelInUpdate, BatchModelInFilters
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

    async def filter_batches(self, filters: BatchModelInFilters) -> List[Batch]:
        apply_filters = []

        filter_mapping = {
            "closing_status": Batch.closing_status,
            "closed_at_before": Batch.closed_at,
            "closed_at_after": Batch.closed_at,
            "submission": Batch.submission,
            "line": Batch.line,
            "shift": Batch.shift,
            "crew": Batch.crew,
            "number": Batch.number,
            "batch_date_before": Batch.batch_date,
            "batch_date_after": Batch.batch_date,
            "nomenclature": Batch.nomenclature,
            "single_cadastral_number": Batch.single_cadastral_number,
            "work_center": Batch.work_center,
            "shift_start_datetime_before": Batch.shift_start_datetime,
            "shift_start_datetime_after": Batch.shift_start_datetime,
            "shift_end_datetime_before": Batch.shift_end_datetime,
            "shift_end_datetime_after": Batch.shift_end_datetime,
        }

        for filter_name, filter_value in vars(filters).items():
            if filter_value is not None:
                if filter_name.endswith("_before"):
                    apply_filters.append(filter_mapping[filter_name] <= filter_value)
                elif filter_name.endswith("_after"):
                    apply_filters.append(filter_mapping[filter_name] >= filter_value)
                else:
                    apply_filters.append(filter_mapping[filter_name] == filter_value)

        query = select(Batch)
        if filters:
            query = query.where(and_(*apply_filters))

        batches = await self.db_session.execute(query)
        return batches.scalars().all()
