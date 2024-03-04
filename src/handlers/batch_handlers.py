from datetime import datetime
from typing import Union, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.handlers.pydantic_models.batch_model import BatchModel
from src.services.batch_service import BatchService

router = APIRouter(prefix='/batch',
                   tags=['batch'])


@router.post('/add_batches')
async def add_batches(batches: List[BatchModel],
                      session: AsyncSession = Depends(get_async_session)):
    batch_service = BatchService(session)
    for batch in batches:
        await batch_service.create_batch(batch)
