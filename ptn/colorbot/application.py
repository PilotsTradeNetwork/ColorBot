"""
The Python script that starts the bot.

"""

# import libraries
import asyncio
import os

# import bot Cogs
from ptn.colorbot.botcommands.Commands import Commands

# import bot object, token, production status
from ptn.colorbot.constants import TOKEN, _production, DATA_DIR
from ptn.colorbot.bot import bot

print(f"Data dir is {DATA_DIR} from {os.path.join(os.getcwd(), 'ptn', 'colorbot', DATA_DIR, 'ptn/colorbot/.env')}")

print(f'PTN ColorBot is connecting against production: {_production}.')


def run():
    asyncio.run(colorbot())


async def colorbot():
    async with bot:
        await bot.add_cog(Commands(bot))
        await bot.start(TOKEN)


if __name__ == '__main__':
    """
    If running via `python ptn/colorbot/application.py
    """
    run()
