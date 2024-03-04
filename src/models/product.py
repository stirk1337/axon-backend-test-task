import datetime

from sqlalchemy import Integer, Boolean, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    code: Mapped[str] = mapped_column(
        String(length=100), nullable=False, unique=True
    )
    is_aggregated: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    aggregated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
