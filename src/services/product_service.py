from datetime import datetime

import sqlalchemy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.handlers.pydantic_models.product_model import ProductInRus
from src.models.product import Product


class ProductService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_product(self, product_model: ProductInRus, batch_id: int):
        product = Product(code=product_model.code, batch_id=batch_id)
        self.db_session.add(product)
        try:
            await self.db_session.commit()
        except sqlalchemy.exc.IntegrityError:
            pass

    async def get_product_by_code(self, code: str) -> Product:
        product = await self.db_session.scalar(
            select(Product)
            .where(Product.code == code)
        )
        return product

    async def aggregate_product(self, product: Product):
        product.is_aggregated = True
        product.aggregated_at = datetime.now()
        await self.db_session.commit()
