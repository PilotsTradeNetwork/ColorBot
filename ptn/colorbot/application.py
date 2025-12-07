"""
The Python script that starts the bot.

"""

# import libraries
import asyncio
import logging
import os

from discord.ext.prometheus import PrometheusCog
from discord.utils import setup_logging

from ptn.colorbot.bot import bot

# import bot Cogs
from ptn.colorbot.botcommands.Commands import Commands

# import bot object, token, production status
from ptn.colorbot.constants import DATA_DIR, LOG_LEVEL, TOKEN, _production, log_handler


def run():
    asyncio.run(colorbot())


async def colorbot():
    async with bot:
        await bot.add_cog(Commands(bot))
        await bot.add_cog(PrometheusCog(bot))
        setup_logging(handler=log_handler, level=LOG_LEVEL)
        logging.info(
            f"Data dir is {DATA_DIR} from {os.path.join(os.getcwd(), 'ptn', 'colorbot', DATA_DIR, 'ptn/colorbot/.env')}"
        )
        logging.info(f"PTN ColorBot is connecting against production: {_production}.")
        await bot.start(TOKEN)


if __name__ == "__main__":
    """
    If running via `python ptn/colorbot/application.py
    """
    run()
