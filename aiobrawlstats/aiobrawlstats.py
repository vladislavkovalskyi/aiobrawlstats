from aiobrawlstats.const.const import URL_PLAYER, URL_PLAYER_BATTLELOG
from aiobrawlstats.http.http import request
from aiobrawlstats.types.player.player import Player


class Client:
    def __init__(self, token: str):
        self._token = token
        self.headers = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(self._token)
        }

    async def get_player(self, tag: str):
        response = await request(URL_PLAYER.format(tag=tag), headers=self.headers)
        # return Player(**response)
        return response

    async def get_battle(self, tag: str):
        response = await request(URL_PLAYER_BATTLELOG.format(tag=tag), headers=self.headers)
        return response


