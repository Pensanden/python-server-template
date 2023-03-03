from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class ProductSellEvent:
    product_id: UUID
    event_date: datetime
    sold_to: UUID
