import datetime
import dataclasses
from typing import List, Optional

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship,MappedAsDataclass
from sqlalchemy import String, ForeignKey

''''
    SQL naming

    Table
    - Singular naming = student
    - lowercase_lowercase
    - use a noun
    - No prefix for table
    - Relation many to many tabel1_table2
    Column
    - PK = id
    - FK = table_id
    - Bool = has_value or is_value
    - Date = value_date
    Views v_
    Function f_
    Stored procedures p_<table_name>_<action_name>
'''


class Base(MappedAsDataclass, DeclarativeBase):
    pass


class Location(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[Optional[str]] = mapped_column(String(256))
    address: Mapped[Optional[str]] = mapped_column(String(60))
    phone: Mapped[Optional[str]] = mapped_column(String(15))
    email: Mapped[Optional[str]] = mapped_column(String(30))
    fields: Mapped[List["Field"]] = relationship(back_populates="location", lazy="selectin")
    days_open: Mapped[List["DaysOpen"]] = relationship(back_populates="location",lazy="selectin")
    days_closed: Mapped[List["DaysClosed"]] = relationship(back_populates="location",lazy="selectin")

    def __init__(self, name: str, description: str, address: str, phone: str, email: str,
                 fields: List["SportField"] = None, days_open: List["DaysOpen"] = None,
                 days_closed: List["DaysClosed"] = None):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.phone = phone
        self.email = email
        self.fields = fields or []
        self.days_open = days_open or []
        self.days_closed = days_closed or []



class Pricing(Base):
    __tablename__ = "pricing"

    id: Mapped[int] = mapped_column(primary_key=True)
    price_member: Mapped[Optional[float]]
    price: Mapped[float]
    #fields: Mapped[List["Field"]] = relationship(back_populates="fields", lazy="selectin")

    def __init__(self, price: float, price_member: float):
        super().__init__()
        self.price = price
        self.price_member = price_member


class Sport(Base):
    __tablename__ = "sport"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[Optional[str]] = mapped_column(String(256))
    #fields: Mapped[List["Field"]] = relationship(back_populates="fields", lazy="selectin")

    def __init__(self, name: str, description: str = ""):
        super().__init__()
        self.name = name
        self.description = description


    def __repr__(self):
        super().__repr__()
        return f'<Sport Name: {self.name} >'

class Field(Base):
    __tablename__ = "field"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    is_available: Mapped[bool]
    location_id: Mapped[Location] = mapped_column(ForeignKey("location.id"))
    location: Mapped[Location] = relationship(back_populates="fields")
    sport_id: Mapped["Sport"] = mapped_column(ForeignKey("sport.id"))
    pricing_id: Mapped["Pricing"] = mapped_column(ForeignKey("pricing.id"))
    reservations: Mapped[List["Reservation"]] = relationship(back_populates="field", lazy="selectin")

    def __init__(self, name: str, location_id: int, sport_id: int, pricing_id: int, is_available: bool = True):
        super().__init__()
        self.name = name
        self.is_available = is_available
        self.location_id = location_id
        self.sport_id = sport_id
        self.pricing_id = pricing_id


class Reservation(Base):
    __tablename__ = "reservation"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer: Mapped[str] = mapped_column(String(30))
    date: Mapped[datetime.date]
    start_time: Mapped[datetime.time]
    end_time: Mapped[datetime.time]
    field_id: Mapped[Field] = mapped_column(ForeignKey("field.id"))
    field: Mapped[Field] = relationship(back_populates="reservations", lazy="selectin")
    def __init__(self, customer: str, reservation_date: datetime.date,
                 start_time: datetime.time, end_time: datetime.time, field_id: int):
        super().__init__()
        self.customer = customer
        self.date = reservation_date
        self.start_time = start_time
        self.end_time = end_time
        self.field_id = field_id


class DaysOpen(Base):
    __tablename__ = "days_open"

    id: Mapped[int] = mapped_column(primary_key=True)
    weekday: Mapped[int]
    start_time: Mapped[datetime.time]
    end_time: Mapped[datetime.time]
    location_id: Mapped[Location] = mapped_column(ForeignKey("location.id"))
    location: Mapped[Location] = relationship(back_populates="days_open", lazy="selectin")

    def __init__(self, weekday: int, start_time: datetime.time, end_time: datetime.time, location_id: int):
        super().__init__()
        self.weekday = weekday
        self.start_time = start_time
        self.end_time = end_time
        self.location_id = location_id


class DaysClosed(Base):
    __tablename__ = "days_closed"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime.date]
    location_id: Mapped[Location] = mapped_column(ForeignKey("location.id"))
    location: Mapped[Location] = relationship(back_populates="days_closed", lazy="selectin")

    def __init__(self, date: datetime.date, location_id: int):
        super().__init__()
        self.date = date
        self.location_id = location_id

