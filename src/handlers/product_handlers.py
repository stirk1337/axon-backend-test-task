from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.handlers.pydantic_models.product_model import ProductInRus, ProductInAggregate, ProductOutAggregate
from src.handlers.pydantic_models.response import Message

from src.services.batch_service import BatchService
from src.services.product_service import ProductService

router = APIRouter(prefix='/product',
                   tags=['product'])


@router.post('/', status_code=201)
async def add_product(products_in: List[ProductInRus],
                      session: AsyncSession = Depends(get_async_session)):
    batch_service = BatchService(session)
    product_service = ProductService(session)
    for product in products_in:
        batch = await batch_service.get_batch_by_number_and_date(product.number, product.batch_date)
        if batch:
            await product_service.create_product(product, batch.id)
    return {'status': 'ok'}


@router.patch('/aggregate/', status_code=200, responses={
    404: {'model': Message, 'description': "Product not found"},
    400: {'model': Message, 'description': 'unique code is attached to another batch or already used'}})
async def aggregate_product(code: str, product_in: ProductInAggregate,
                            session: AsyncSession = Depends(get_async_session)) -> ProductOutAggregate:
    product_service = ProductService(session)
    product = await product_service.get_product_by_code(code)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.batch_id != product_in.batch_id:
        raise HTTPException(status_code=400, detail="unique code is attached to another batch")
    if product.is_aggregated:
        raise HTTPException(status_code=400, detail=f"unique code already used at {product.aggregated_at}")
    await product_service.aggregate_product(product)
    return ProductOutAggregate.from_orm(product)
