"""
bot.py

This is where we define our bot object and setup_hook (replacement for on_ready)

Dependencies: Constants, Metadata

"""

# import libraries

# import discord
import discord
from discord.ext import commands

# import constants
from ptn.colorbot._metadata import __version__
from ptn_utils.global_constants import EMBED_COLOUR_OK, DISCORD_GUILD, CHANNEL_DEV_COLOR_BOT

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
        self.logger = None

        super().__init__(
            command_prefix=commands.when_mentioned_or("🌈"), intents=intents, chunk_guilds_at_startup=False
        )
        self.get_or_fetch = GetOrFetch(self, DISCORD_GUILD)

    async def on_ready(self):
        try:
            # TODO: this should be moved to an on_setup hook
            bot.logger.info(f"{bot.user.name} version: {__version__} has connected to Discord!")
            devchannel = await self.get_or_fetch.channel(CHANNEL_DEV_COLOR_BOT)

            embed = discord.Embed(
                title="🌈 COLORBOT ONLINE (on_ready)",
                description=f"🌈<@{bot.user.id}> connected, version **{__version__}**.",
                color=EMBED_COLOUR_OK,
            )
            await devchannel.send(embed=embed)

        except Exception as e:
            bot.logger.exception(e)

    async def on_disconnect(self):
        bot.logger.warning(f"🔌colorbot has disconnected from discord server, version: {__version__}.")


bot = ColorBot()
