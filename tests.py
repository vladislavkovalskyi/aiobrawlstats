import asyncio
from pprint import pprint

from aiobrawlstats import Client
from aiobrawlstats.types.players.player_battlelog import BattleLog

TOKEN = ""

client = Client(token=TOKEN)


async def app():
    # player_info = await client.get_player("R809PCRV")
    # pprint(player_info)
    player_battles_info = await client.get_battle("22LRPLGRY")
    pprint(player_battles_info)
    pprint(BattleLog(**player_battles_info), sort_dicts=False)


loop = asyncio.get_event_loop()
loop.run_until_complete(app())
