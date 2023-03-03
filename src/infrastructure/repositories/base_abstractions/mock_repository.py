from abc import ABCMeta
from uuid import UUID

from src.infrastructure.repositories.base_abstractions.abstract_base_repository import AbstractBaseRepository


class AbstractMockRepository(metaclass=ABCMeta, AbstractBaseRepository):
    PAGE_SIZE = 25
    __domain_model__ = None
    mock_db = []

    def list(self, page=0):
        return self.mock_db[page * self.PAGE_SIZE:(page * self.PAGE_SIZE) + self.PAGE_SIZE]

    def get(self, id: UUID):
        return list(filter(lambda x: x.id == id, self.mock_db)).pop()

    def add(self, entity):
        self.mock_db.append(entity)

    def update(self, entity):
        self.delete(entity.id)
        self.mock_db.append(entity)

    def delete(self, id: UUID):
        self.mock_db = [x for x in self.mock_db if x.id != id]
