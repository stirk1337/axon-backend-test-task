from datetime import datetime, date

from pydantic import BaseModel, Field


class ProductInRus(BaseModel):
    code: str = Field(validation_alias='УникальныйКодПродукта')
    number: int = Field(validation_alias='НомерПартии')
    batch_date: date = Field(validation_alias='ДатаПартии')


class ProductInAggregate(BaseModel):
    batch_id: int


class ProductOut(BaseModel):
    class Config:
        orm_mode = True
        from_attributes = True

    id: int
    code: str
    is_aggregated: bool
    aggregated_at: datetime


class ProductOutAggregate(BaseModel):

    class Config:
        orm_mode = True
        from_attributes = True

    code: str
