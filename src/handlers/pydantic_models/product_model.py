from datetime import datetime

from pydantic import BaseModel


class ProductOut(BaseModel):

    class Config:
        orm_mode = True
        from_attributes = True

    id: int
    code: str
    is_aggregated: bool
    aggregated_at: datetime
