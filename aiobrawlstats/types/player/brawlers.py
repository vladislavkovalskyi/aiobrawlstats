from typing import Optional, List

from pydantic import BaseModel, Field


class StarPower(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class Accessory(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class BrawlerStat(BaseModel):
    id: Optional[int] = None
    rank: Optional[int] = None
    power: Optional[int] = None
    name: Optional[str] = None

    highest_trophies: Optional[int] = Field(alias="highestTrophies")
    star_powers: List[StarPower] = Field(alias="starPowers")

    gadgets: List[Accessory] = None
