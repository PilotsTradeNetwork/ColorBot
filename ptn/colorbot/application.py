"""
The Python script that starts the bot.

"""

# import libraries
import asyncio
import os

from discord.ext.prometheus import PrometheusCog
# from discord.utils import setup_logging

from ptn.colorbot.bot import bot

from loguru import logger

# import bot Cogs
from ptn.colorbot.botcommands.Commands import Commands
from ptn_utils.logger.logger import Logger

# import bot object, token, production status
from ptn_utils.global_constants import DATA_DIR, TOKEN, _production


logger = logger.bind(logger_name="colorbot")

logger.info(f"Color bot is connecting against production: {_production}.")

def run():
    asyncio.run(colorbot())


async def colorbot():
    async with bot:
        await bot.add_cog(Logger())
        logger.debug("Loaded Logger cog.")
        bot.logger = logger
        await bot.add_cog(Commands(bot))
        logger.debug("Loaded Commands cog.")
        await bot.add_cog(PrometheusCog(bot))
        logger.debug("Loaded PrometheusCog cog.")
        logger.info(
            f"Data dir is {DATA_DIR} from {os.path.join(os.getcwd(), 'ptn', 'colorbot', DATA_DIR, 'ptn/colorbot/.env')}"
        )
        logger.info(f"PTN ColorBot is connecting against production: {_production}.")
        try:
            logger.info("Starting the bot.")
            await bot.start(TOKEN)
        except Exception as e:
            logger.exception(f"Error in bot login: {e}")


if __name__ == "__main__":
    """
    If running via `python ptn/colorbot/application.py
    """
    run()
