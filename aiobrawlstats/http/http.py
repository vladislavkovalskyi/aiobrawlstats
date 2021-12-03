from typing import Optional, Mapping
from urllib import parse

from aiohttp import ClientSession


async def request(
    url: str, data: Optional[dict] = None, params: Optional[Mapping[str, str]] = None, **kwargs
) -> dict:
    async with ClientSession() as session:
        async with session.get(
            url=parse.quote(url).replace("%3A", ":"), data=data, params=params, **kwargs
        ) as response:
            return await response.json(encoding="UTF-8")
