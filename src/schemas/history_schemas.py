from typing import List, Optional
from pydantic import BaseModel
from .tron_info_schemas import TronResponseSchema


class PaginatorHistorySchema(BaseModel):
    offset: int
    limit: Optional[int]
    total: int


class HistoryResponseSchema(BaseModel):
    history: List[TronResponseSchema]
    paginator: PaginatorHistorySchema
