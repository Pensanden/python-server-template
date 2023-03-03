from abc import ABCMeta
from uuid import UUID


class AbstractBaseRepository(metaclass=ABCMeta):
    def list(self, page=0):
        raise NotImplementedError

    def get(self, id: UUID):
        raise NotImplementedError

    def add(self, entity):
        raise NotImplementedError

    def update(self, entity):
        raise NotImplementedError

    def delete(self, id: UUID):
        raise NotImplementedError

    def count(self):
        raise NotImplementedError

    def all(self):
        raise NotImplementedError
