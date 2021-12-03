from aiobrawlstats.const import URL_PLAYERS, URL_BRAWLERS, URL_EVENTS
from aiobrawlstats.http.http import request
from aiobrawlstats.types.events import ScheduledEvents
from aiobrawlstats.types.players import Player
from aiobrawlstats.types.players import BattleLog
from aiobrawlstats.types.brawlers import Brawlers, Brawler
from typing import Union


class Client:
    def __init__(self, token: str, debug: bool = False):
        self._token = token
        self.debug = debug
        self.headers = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(self._token),
        }

    async def get_player(self, tag: str) -> Union[Player, dict]:
        response = await request(f"{URL_PLAYERS}/{tag}", headers=self.headers)
        return response if self.debug else Player(**response)

    async def get_battlelog(self, tag: str) -> Union[BattleLog, dict]:
        response = await request(
            URL_PLAYERS + "/{tag}/battlelog".format(tag=tag), headers=self.headers
        )
        return response if self.debug else BattleLog(**response)

    async def get_brawlers(
        self, before: str = None, after: str = None, limit: int = None
    ) -> Union[Brawlers, dict]:
        if before and after:
            raise TypeError("Only after or before can be specified for a request, not both.")

        params = {k: v for k, v in locals().items() if k != "self" and v}
        response = await request(URL_BRAWLERS, headers=self.headers, params=params)
        return response if self.debug else Brawlers(**response)

    async def get_brawler_by_id(self, brawler_id: int) -> Union[Brawler, dict]:
        response = await request(
            URL_BRAWLERS + "/{brawler_id}/".format(brawler_id=brawler_id), headers=self.headers
        )
        return response if self.debug else Brawler(**response)

    async def get_events(self) -> Union[ScheduledEvents, dict]:
        response = await request(URL_EVENTS, headers=self.headers)
        return response if self.debug else ScheduledEvents.parse_obj(response)
