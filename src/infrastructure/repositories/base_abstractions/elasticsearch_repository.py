from uuid import UUID

from src.infrastructure.repositories.base_abstractions.abstract_base_repository import AbstractBaseRepository


class ElasticsearchRepository(AbstractBaseRepository):
    def list(self, page=0):
        pass

    def get(self, id: UUID):
        pass

    def add(self, entity):
        pass

    def update(self, entity):
        pass

    def delete(self, id: UUID):
        pass

    def count(self):
        pass

    def all(self):
        pass
