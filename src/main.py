import logging
import sys
from contextlib import suppress

import bot

logging.basicConfig(level=logging.INFO)


async def main():
    await bot.start()


if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        if sys.platform in ['linux', 'darwin']:
            import uvloop

            uvloop.run(main())
        else:
            import asyncio

            asyncio.run(main())
