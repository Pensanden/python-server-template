from dataclasses import dataclass
from datetime import date

from src.domain.common.base_entity import BaseEntity
from src.domain.value_objects.money import Money


@dataclass
class Product(BaseEntity):
    name: str
    shelve: int
    price: Money
    is_sold: bool
    expiration_date: date
