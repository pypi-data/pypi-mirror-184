from pydantic import BaseModel, Field


class BaseParams(BaseModel):
    apikey: str
