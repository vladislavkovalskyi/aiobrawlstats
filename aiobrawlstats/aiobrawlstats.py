from aiobrawlstats.const.const import URL_PLAYER, URL_PLAYER_BATTLELOG
from aiobrawlstats.http.http import request
from aiobrawlstats.types.players.player import Player
from aiobrawlstats.types.players.player_battlelog import BattleLog


class Client:
    def __init__(self, token: str, debug: bool = False):
        self._token = token
        self.debug = debug
        self.headers = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(self._token),
        }

    async def get_player(self, tag: str):
        response = await request(URL_PLAYER.format(tag=tag), headers=self.headers)
        return response if self.debug else Player(**response)

    async def get_battle(self, tag: str):
        response = await request(URL_PLAYER_BATTLELOG.format(tag=tag), headers=self.headers)
        return response if self.debug else BattleLog(**response)
