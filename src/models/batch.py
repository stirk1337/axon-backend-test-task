from datetime import datetime, date

from sqlalchemy import Integer, Boolean, String, UniqueConstraint, DateTime, Date
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Batch(Base):
    __tablename__ = 'batch'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    closing_status: Mapped[bool] = mapped_column(
        Boolean, nullable=False
    )
    closed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    submission: Mapped[str] = mapped_column(
        String(length=100), nullable=False
    )
    line: Mapped[str] = mapped_column(
        String(length=100), nullable=False
    )
    shift: Mapped[str] = mapped_column(
        String(length=100), nullable=False
    )
    crew: Mapped[str] = mapped_column(
        String(length=100), nullable=False
    )
    number: Mapped[str] = mapped_column(
        Integer, nullable=False
    )
    batch_date: Mapped[date] = mapped_column(
        Date(), nullable=False
    )
    nomenclature: Mapped[str] = mapped_column(
        String(length=100), nullable=False
    )
    single_cadastral_number: Mapped[str] = mapped_column(
        String(length=100), nullable=False
    )
    work_center: Mapped[str] = mapped_column(
        String(length=100), nullable=False
    )
    shift_start_datetime: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    shift_end_datetime: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )

    __table_args__ = (
        UniqueConstraint(number, batch_date, name='u_number_date'),
    )
