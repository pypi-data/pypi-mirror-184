from enum import Enum

from . import BaseParams, Field


class ListType(str, Enum):
    five_minute = "5-minute"
    hourly = "hourly"
    daily = "daily"


class ListParams(BaseParams):
    type: ListType
    from_date: str = Field(
        description="Filter files on date ex: 2023-01-01",
        alias="from"
    )
    to_date: str = Field(
        description="Filter files on date ex: 2023-01-01",
        alias="to"
    )


class DownloadParams(BaseParams):
    path: str
