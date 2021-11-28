from typing import Optional, List

from pydantic import BaseModel, Field


class Event(BaseModel):
    mode: Optional[str] = None
    id: Optional[int] = None
    map: Optional[str] = None


class BattleResult(BaseModel):
    pass


class Battle(BaseModel):
    event: Optional[Event] = None
    battle: List[BattleResult] = None
    battle_time: Optional[str] = Field(alias="battleTime")


class BattleLog(BaseModel):
    items: List[Battle] = None  # ВОТ ТУТ ОШИБКА НАХУЙ
    paging: Optional[dict] = None
