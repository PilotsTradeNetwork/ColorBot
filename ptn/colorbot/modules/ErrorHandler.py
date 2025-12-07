"""
ErrorHandler.py

Our custom global error handler for the bot. v1 is directly imported from MAB

Dependends on: constants
"""

import logging

# import discord.py
import discord
from discord import Interaction, app_commands
from discord.app_commands import AppCommandError

# import local constants
import ptn.colorbot.constants as constants
from ptn.colorbot.constants import channel_botspam
from ptn.colorbot.bot import bot



# custom errors
class CommandChannelError(app_commands.CheckFailure):  # channel check error
    def __init__(self, permitted_channel, formatted_channel_list):
        self.permitted_channel = permitted_channel
        self.formatted_channel_list = formatted_channel_list
        super().__init__(permitted_channel, formatted_channel_list, "Channel check error raised")

    pass


class CommandRoleError(app_commands.CheckFailure):  # role check error
    def __init__(self, permitted_roles, formatted_role_list):
        self.permitted_roles = permitted_roles
        self.formatted_role_list = formatted_role_list
        super().__init__(permitted_roles, formatted_role_list, "Role check error raised")

    pass


class GenericError(Exception):  # generic error
    pass


class CustomError(Exception):
    """Error handler that hides the Exception text from the user and shows custom text from source"""

    def __init__(self, message, isprivate=True):
        self.message = message
        self.isprivate = isprivate
        super().__init__(self.message, "CustomError raised")


"""
A primitive global error handler for all app commands (slash & ctx menus)

returns: the error message to the user and log
"""


async def on_generic_error(interaction: Interaction, error):  # an error handler for our custom errors
    try:
        spamchannel = await bot.get_or_fetch.channel(channel_botspam())
        spam_embed = discord.Embed(
            description=f"Error from `{interaction.command.name}` in <#{interaction.channel.id}> called by <@{interaction.user.id}>: ```{error}```",
            color=constants.EMBED_COLOUR_ERROR,
        )
        await spamchannel.send(embed=spam_embed)
    except Exception as e:
        logging.exception(e)

    if isinstance(error, GenericError):
        logging.error(f"Generic error raised: {error}")
        embed = discord.Embed(description=f"❌ {error}", color=constants.EMBED_COLOUR_ERROR)
        try:
            await interaction.followup.send(embed=embed, ephemeral=True)
        except Exception as e:
            logging.exception(e)
            await interaction.followup.send(embed=embed, ephemeral=True)

    elif isinstance(
        error, CustomError
    ):  # this class receives custom error messages and displays either privately or publicly
        message = error.message
        isprivate = error.isprivate
        logging.error(f"Raised CustomError from {error} with message {message}")
        embed = discord.Embed(description=f"❌ {message}", color=constants.EMBED_COLOUR_ERROR)
        if isprivate:  # message should be ephemeral
            try:
                await interaction.followup.send(embed=embed, ephemeral=True)
            except Exception as e:
                logging.exception(e)
                await interaction.followup.send(embed=embed, ephemeral=True)
        else:  # message should be public - use for CCO commands
            try:
                await interaction.followup.send(embed=embed)
            except Exception as e:
                logging.exception(e)
                await interaction.followup.send(embed=embed)

    else:
        logging.error(f"Error {error} was not caught by on_generic_error")


async def on_app_command_error(interaction: Interaction, error: AppCommandError):
    """Error handler for discord.py errors"""
    logging.error(
        f"Error from {interaction.command.name} in {interaction.channel.name} called by {interaction.user.display_name}: {error}"
    )

    try:
        if isinstance(error, CommandChannelError):
            logging.error("Channel check error raised")
            formatted_channel_list = error.formatted_channel_list

            embed = discord.Embed(
                description=f"Sorry, you can only run this command out of: {formatted_channel_list}",
                color=constants.EMBED_COLOUR_ERROR,
            )
            await interaction.followup.send(embed=embed, ephemeral=True)

        elif isinstance(error, CommandRoleError):
            logging.error("Role check error raised")
            permitted_roles = error.permitted_roles
            formatted_role_list = error.formatted_role_list
            if len(permitted_roles) > 1:
                embed = discord.Embed(
                    description=f"**Permission denied**: You need one of the following roles to use this command:\n{formatted_role_list}",
                    color=constants.EMBED_COLOUR_ERROR,
                )
            else:
                embed = discord.Embed(
                    description=f"**Permission denied**: You need the following role to use this command:\n{formatted_role_list}",
                    color=constants.EMBED_COLOUR_ERROR,
                )
            logging.debug("notify user")
            await interaction.followup.send(embed=embed, ephemeral=True)

        elif isinstance(error, CustomError):
            message = error.message
            isprivate = error.isprivate
            logging.error(f"Raised CustomError from {error} with message {message}")
            embed = discord.Embed(description=f"❌ {message}", color=constants.EMBED_COLOUR_ERROR)
            if isprivate:  # message should be ephemeral
                try:
                    await interaction.followup.send(embed=embed, ephemeral=True)
                except Exception as e:
                    logging.exception(e)
                    await interaction.followup.send(embed=embed, ephemeral=True)
            else:  # message should be public - use for CCO commands
                try:
                    await interaction.followup.send(embed=embed)
                except Exception as e:
                    logging.exception(e)
                    await interaction.followup.send(embed=embed)

        elif isinstance(error, GenericError):
            logging.error(f"Generic error raised: {error}")
            embed = discord.Embed(description=f"❌ {error}", color=constants.EMBED_COLOUR_ERROR)
            try:
                await interaction.followup.send(embed=embed, ephemeral=True)
            except Exception as e:
                logging.exception(e)
                await interaction.followup.send(embed=embed, ephemeral=True)

        else:
            logging.error("Othertype error message raised")
            embed = discord.Embed(description=f"❌ Unhandled Error: {error}", color=constants.EMBED_COLOUR_ERROR)
            try:
                await interaction.followup.send(embed=embed, ephemeral=True)
            except Exception as e:
                logging.exception(e)
                await interaction.followup.send(embed=embed, ephemeral=True)

    except Exception as e:
        logging.error(f"An error occurred in the error handler (lol): {e}")
        logging.exception(e)
