import abc
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from dataclasses_json import dataclass_json

@dataclass_json
@dataclass(repr=False)
class BaseEntity(metaclass=abc.ABCMeta):
    """
    Basic Entity to be extended by all entities
    """
    id: UUID
    creation_time: datetime = field(metadata=iso_datetime_field)
    last_update_time: datetime = field(metadata=iso_datetime_field)

    def __eq__(self, other):
        if self.id == other.id:
            return True

    def __str__(self):
        return f"{self.__class__.__name__}:{self.id}"

    def __repr__(self):
        return f"{self.__class__.__name__}:{self.id}"
