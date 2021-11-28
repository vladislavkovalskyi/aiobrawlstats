from typing import Optional, List

from pydantic import BaseModel, Field

from aiobrawlstats.types.brawlers.brawler import BrawlerStat


class PlayerClub(BaseModel):
    tag: Optional[str] = None
    name: Optional[str] = None


class PlayerIcon(BaseModel):
    id: Optional[int] = None


class Player(BaseModel):
    tag: Optional[str] = None
    trophies: Optional[int] = None
    name: Optional[str] = None

    name_color: Optional[str] = Field(alias="nameColor")
    highest_trophies: Optional[int] = Field(alias="highestTrophies")
    exp_level: Optional[int] = Field(alias="expLevel")
    exp_points: Optional[int] = Field(alias="expPoints")
    is_qualified_from_championship_challenge: Optional[bool] = Field(
        alias="isQualifiedFromChampionshipChallenge"
    )
    solo_victories: Optional[int] = Field(alias="soloVictories")
    duo_victories: Optional[int] = Field(alias="duoVictories")
    trio_victories: Optional[int] = Field(alias="3vs3Victories")
    best_robo_rumble_time: Optional[int] = Field(alias="bestRoboRumbleTime")
    best_time_as_big_brawler: Optional[int] = Field(alias="bestTimeAsBigBrawler")

    club: Optional[PlayerClub]
    icon: Optional[PlayerIcon]
    brawlers: List[BrawlerStat]
