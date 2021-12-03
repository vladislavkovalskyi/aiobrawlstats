from pydantic import BaseModel, Field
from typing import Optional, List

from aiobrawlstats.types.players.player import PlayerIcon


class ClubMember(BaseModel):
    icon: PlayerIcon = None
    tag: str = None
    name: str = None
    trophies: str = None
    role: Optional[str] = None
    name_color: Optional[str] = Field(alias="nameColor")


class Club(BaseModel):
    tag: str = None
    name: str = None
    description: Optional[str] = None
    trophies: int = None
    required_trophies: Optional[int] = Field(alias="requiredTrophies")
    members: Optional[List[ClubMember]] = None
    type: Optional[str] = None
    badge_id: Optional[int] = None
