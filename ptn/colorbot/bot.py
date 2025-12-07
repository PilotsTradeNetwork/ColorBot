"""
bot.py

This is where we define our bot object and setup_hook (replacement for on_ready)

Dependencies: Constants, Metadata

"""

# import libraries
import logging

# import discord
import discord
from discord.ext import commands

# import constants
from ptn.colorbot._metadata import __version__
from ptn.colorbot.constants import EMBED_COLOUR_OK, bot_guild, channel_botdev

# import utils
from ptn_utils.get_or_fetch import GetOrFetch

"""
Bot object
"""


# define bot object
class ColorBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.none()
        intents.guilds = True
        intents.members = True
        intents.messages = True

        super().__init__(
            command_prefix=commands.when_mentioned_or("🌈"), intents=intents, chunk_guilds_at_startup=False
        )
        self.get_or_fetch = GetOrFetch(self, bot_guild())

    async def on_ready(self):
        try:
            # TODO: this should be moved to an on_setup hook
            logging.info(f"{bot.user.name} version: {__version__} has connected to Discord!")
            guild = await self.get_or_fetch.guild(bot_guild())
            devchannel = await self.get_or_fetch.channel(channel_botdev())

            embed = discord.Embed(
                title="🌈 COLORBOT ONLINE (on_ready)",
                description=f"🌈<@{bot.user.id}> connected, version **{__version__}**.",
                color=EMBED_COLOUR_OK,
            )
            await devchannel.send(embed=embed)

        except Exception as e:
            logging.exception(e)

    async def on_disconnect(self):
        logging.warning(f"🔌colorbot has disconnected from discord server, version: {__version__}.")


bot = ColorBot()
