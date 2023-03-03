from dataclasses import dataclass


@dataclass
class MetaAPIResponse:
    error: int
    pagination: int
    gamification: int


@dataclass
class APIResult:
    pass


@dataclass
class TemplateAPIResponse:
    meta: MetaAPIResponse | None = None
    result: APIResult | None = None
