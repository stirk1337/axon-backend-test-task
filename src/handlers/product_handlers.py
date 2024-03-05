from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session

from src.services.batch_service import BatchService
from src.services.product_service import ProductService

router = APIRouter(prefix='/product',
                   tags=['product'])


@router.post('/', status_code=201)
async def add_product(session: AsyncSession = Depends(get_async_session)):
    batch_service = BatchService(session)
    product_service = ProductService(session)