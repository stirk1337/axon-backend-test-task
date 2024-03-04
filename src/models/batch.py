import datetime

from sqlalchemy import Integer, Boolean, String, text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Batch(Base):
    __tablename__ = 'batch'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    closing_status: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    closed_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"), nullable=True
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
    batch_date: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    nomenclature: Mapped[str] = mapped_column(
        Integer, unique=True, nullable=False
    )
    single_cadastral_number: Mapped[str] = mapped_column(
        String(length=100), nullable=False
    )
    work_center: Mapped[str] = mapped_column(
        String(length=100), nullable=False
    )
    shift_start_datetime: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    shift_end_datetime: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

    __table_args__ = (
        UniqueConstraint(number, batch_date, name='u_number_date'),
    )
