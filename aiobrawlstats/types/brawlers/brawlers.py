from typing import List

from pydantic import BaseModel, Field
from . import Brawler


class Brawlers(BaseModel):
    BrawlerList: List[Brawler] = Field(alias="items")
