import sqlalchemy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.handlers.pydantic_models.batch_model import BatchModel
from src.models.batch import Batch


class BatchService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_batch(self, batch_model: BatchModel):
        batch_args = {
            attr: getattr(batch_model, attr)
            for attr in vars(batch_model)
        }
        batch = await self.db_session.scalar(
            select(Batch)
            .where(Batch.number == batch_model.number)
            .where(Batch.batch_date == batch_model.batch_date)
        )
        if not batch:
            batch = Batch(**batch_args)
        else:
            pass
        await self.db_session.commit()

    async def update_batch(self, batch_model: BatchModel):
        pass
