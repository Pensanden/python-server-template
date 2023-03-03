from dataclasses import dataclass

from src.domain.enums.currency_type import CurrencyType


@dataclass
class Money:
    amount: int
    currency: CurrencyType = CurrencyType.Rial
