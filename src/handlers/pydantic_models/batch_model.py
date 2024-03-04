from datetime import datetime, date

from pydantic import BaseModel, Field


class BatchModel(BaseModel):
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
