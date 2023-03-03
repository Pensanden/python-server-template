from dataclasses import dataclass


@dataclass
class MainConfigurations:
    PG_HOST: str
    PG_DB: str
    PG_USER: str
    PG_PASSWORD: str
    PG_PORT: int
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

