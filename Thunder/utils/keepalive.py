# Thunder/utils/keepalive.py

import asyncio
import aiohttp
from Thunder.vars import Var
from Thunder.utils.logger import logger

async def ping_server():
    try:
        health_url = f"{Var.URL.rstrip('/')}/health"
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=10)
        ) as session:
            while True:
                try:
                    await asyncio.sleep(Var.PING_INTERVAL)
                    async with session.get(health_url) as resp:
                        if resp.status != 200:
                            logger.warning(f"Ping to {health_url} returned status {resp.status}.")
                except asyncio.CancelledError:
                    break
    except Exception as e:
        logger.error(f"Error in ping_server: {e}", exc_info=True)
