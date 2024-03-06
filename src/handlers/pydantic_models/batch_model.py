from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel, Field

from src.handlers.pydantic_models.product_model import ProductOut


class BatchModelInRus(BaseModel):
    class Config:
        orm_mode = True
        from_attributes = True

    closing_status: bool = Field(validation_alias="СтатусЗакрытия")
    submission: str = Field(validation_alias="ПредставлениеЗаданияНаСмену")
    line: str = Field(validation_alias="Линия")
    shift: str = Field(validation_alias="Смена")
    crew: str = Field(validation_alias="Бригада")
    number: int = Field(validation_alias="НомерПартии")
    batch_date: date = Field(validation_alias="ДатаПартии")
    nomenclature: str = Field(validation_alias="Номенклатура")
    single_cadastral_number: str = Field(validation_alias="КодЕКН")
    work_center: str = Field(validation_alias="ИдентификаторРЦ")
    shift_start_datetime: datetime = Field(validation_alias="ДатаВремяНачалаСмены")
    shift_end_datetime: datetime = Field(validation_alias="ДатаВремяОкончанияСмены")


class BatchModelInFilters(BaseModel):
    closing_status: Optional[bool] = None
    closed_at_before: Optional[datetime] = None
    closed_at_after: Optional[datetime] = None
    submission: Optional[str] = None
    line: Optional[str] = None
    shift: Optional[str] = None
    crew: Optional[str] = None
    number: Optional[int] = None
    batch_date_before: Optional[date] = None
    batch_date_after: Optional[date] = None
    nomenclature: Optional[str] = None
    single_cadastral_number: Optional[str] = None
    work_center: Optional[str] = None
    shift_start_datetime_before: Optional[datetime] = None
    shift_start_datetime_after: Optional[datetime] = None
    shift_end_datetime_before: Optional[datetime] = None
    shift_end_datetime_after: Optional[date] = None


class BatchModelInUpdate(BaseModel):
    closing_status: Optional[bool] = None
    submission: Optional[str] = None
    line: Optional[str] = None
    shift: Optional[str] = None
    crew: Optional[str] = None
    number: Optional[int] = None
    batch_date: Optional[date] = None
    nomenclature: Optional[str] = None
    single_cadastral_number: Optional[str] = None
    work_center: Optional[str] = None
    shift_start_datetime: Optional[datetime] = None
    shift_end_datetime: Optional[datetime] = None


class BatchModelOut(BaseModel):
    class Config:
        orm_mode = True
        from_attributes = True

    id: int
    closing_status: bool
    closed_at: datetime | None
    submission: str
    line: str
    shift: str
    crew: str
    number: int
    batch_date: date
    nomenclature: str
    single_cadastral_number: str
    work_center: str
    shift_start_datetime: datetime
    shift_end_datetime: datetime


class BatchModelOutWithProducts(BatchModelOut):
    products: List[ProductOut]
