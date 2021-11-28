from typing import Optional

from aiohttp import ClientSession


async def request(url: str, data: Optional[dict] = None, **kwargs) -> dict:
    async with ClientSession() as session:
        async with session.get(url=url, data=data, **kwargs) as response:
            return await response.json(encoding="UTF-8")
