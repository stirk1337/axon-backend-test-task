from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.handlers.pydantic_models.batch_model import BatchModelInRus, BatchModelOut, BatchModelInUpdate, \
    BatchModelOutWithProducts, BatchModelInFilters
from src.handlers.pydantic_models.response import Message
from src.services.batch_service import BatchService

router = APIRouter(prefix='/batch',
                   tags=['batch'])


@router.post('/', status_code=201)
async def add_batches(batches_in: List[BatchModelInRus],
                      session: AsyncSession = Depends(get_async_session)):
    batch_service = BatchService(session)
    for batch in batches_in:
        await batch_service.create_batch(batch)
    return {'status': 'ok'}


@router.get('/{batch_id}', responses={
    404: {"model": Message, "description": "Batch was not found"}})
async def get_batch(batch_id: int,
                    session: AsyncSession = Depends(get_async_session)) -> BatchModelOutWithProducts:
    batch_service = BatchService(session)
    batch = await batch_service.get_batch_by_id(batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    return BatchModelOutWithProducts.from_orm(batch)


@router.patch('/{batch_id}', status_code=200, responses={
    404: {'model': Message, 'description': "Batch was not found"},
    500: {'model': Message, 'description': 'Error updating. Unique number and unique date already exists'}})
async def update_batch(batch_id: int,
                       batch_in: BatchModelInUpdate,
                       session: AsyncSession = Depends(get_async_session)) -> BatchModelOut:
    batch_service = BatchService(session)
    batch = await batch_service.get_batch_by_id(batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    updated_batch = await batch_service.update_batch(batch, batch_in)
    if not updated_batch:
        raise HTTPException(status_code=500, detail="Error updating. Unique number and unique date already exists")
    return BatchModelOut.from_orm(updated_batch)


@router.get('/filter/', status_code=200)
async def get_batches_with_filters(filters: BatchModelInFilters = Depends(BatchModelInFilters),
                                   session: AsyncSession = Depends(get_async_session)) -> List[BatchModelOut]:
    batch_service = BatchService(session)
    filtered_batches = await batch_service.filter_batches(filters)
    return [BatchModelOut.from_orm(filtered_batch) for filtered_batch in filtered_batches]
