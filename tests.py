import asyncio
from pprint import pprint

from aiobrawlstats import Client

TOKEN = "Token"
client = Client(token=TOKEN)


async def app():
    player_battles_info = await client.get_battle("PlayerTag")
    pprint(player_battles_info)


loop = asyncio.get_event_loop()
loop.run_until_complete(app())
