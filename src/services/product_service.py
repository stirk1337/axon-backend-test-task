from sqlalchemy.ext.asyncio import AsyncSession


class ProductService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_product(self):
        pass
