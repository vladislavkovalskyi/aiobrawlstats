from typing import Optional, List

from pydantic import BaseModel, Field


class Brawler(BaseModel):
    id: str = None
    name: str = None
    power: int = None
    trophies: int = None


class TeamMembers(BaseModel):
    tag: str = None
    name: str = None
    brawler: Brawler = None


class Event(BaseModel):
    mode: Optional[str] = None
    id: Optional[int] = None
    map: Optional[str] = None


class BattleResult(BaseModel):
    mode: str = None
    type: str = None
    rank: int = None
    trophy_change: Optional[int] = Field(alias="trophyChange")
    teams: Optional[List[List[TeamMembers]]] = None


class Battle(BaseModel):
    event: Optional[Event] = None
    battle: BattleResult = None
    battle_time: Optional[str] = Field(alias="battleTime")


class BattleLog(BaseModel):
    items: List[Battle] = None
    paging: Optional[dict] = None
