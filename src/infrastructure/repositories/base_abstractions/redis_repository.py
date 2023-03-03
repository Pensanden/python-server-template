import json
from uuid import UUID

import redis_om
from redis import Redis

from src.infrastructure.repositories.base_abstractions.abstract_base_repository import AbstractBaseRepository

from src.infrastructure.config.project_config import MainConfigurations as Config


class RedisRepository(AbstractBaseRepository):
    __base_key__: str = None
    PAGE_SIZE = 25

    def __init__(self):
        self.redis = Redis(host=Config.REDIS_HOST,
                           port=Config.REDIS_PORT)

    def list(self, page=0):
        keys = self.redis.keys(self.__base_key__)[page * self.PAGE_SIZE: (page * self.PAGE_SIZE) + self.PAGE_SIZE]
        return [self.get(x) for x in keys]

    def get(self, id: UUID):
        self.redis.get(self.__base_key__ + str(id))

    def add(self, entity):
        self.redis.set(name=self.__base_key__ + str(entity.id), value=json.dumps(entity))

    def update(self, entity, ):
        self.get(entity.id)
        self.delete(entity.id)
        self.add(entity)

    def delete(self, id: UUID):
        self.redis.delete(self.__base_key__ + str(id))

    def count(self):
        return len(self.redis.keys(self.__base_key__))

    def all(self):
        keys = self.redis.keys(self.__base_key__)
        return [self.get(x) for x in keys]
