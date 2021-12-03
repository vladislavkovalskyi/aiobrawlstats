from typing import Optional, List

from pydantic import BaseModel, Field


class StarPower(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class Accessory(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class Brawler(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    star_powers: List[StarPower] = Field(alias="starPowers")

    gadgets: List[Accessory] = None
