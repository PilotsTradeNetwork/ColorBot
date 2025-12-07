import logging
from typing import Optional

import discord
from discord import Guild, Role, Thread
from discord.abc import GuildChannel
from discord.errors import NotFound

from ptn.colorbot.bot import bot

# functions
# The color role functions
# regular roles to check
from ptn.colorbot.constants import bot_guild, color_roles, council_role, mod_role, role_to_color


def color_permission_check(roles: list):
    """
    Check what colors a user can have based on their roles.

    :param roles: List of discord.Role objects the user has
    :return: List of color role IDs the user can have
    """
    # Transforming the list of Role objects to a set of role IDs
    roles_set = {role.id for role in roles}

    # Collecting colors for the roles the user has
    allowed_colors = [role_to_color[role] for role in roles_set if role in role_to_color]

    # flag mods and councilors
    is_mod_council = council_role() in roles_set or mod_role() in roles_set

    return allowed_colors, is_mod_council


async def remove_color(interaction: discord.Interaction, member: discord.Member = None):
    """Removes color roles from a member."""

    # If no member is mentioned, assume the command caller
    if not member:
        member = interaction.user

    # Check for color roles the member has
    roles_to_remove = [role for role in member.roles if role.id in color_roles]

    if roles_to_remove:
        await member.remove_roles(*roles_to_remove)
        logging.info(f"Removed {len(roles_to_remove)} color role(s) from {member.name}.")
    else:
        logging.info(f"{member.name} has no color roles.")


def is_color_role(role: discord.Role) -> bool:
    """Check if a given role is a color role."""
    return role.id in color_roles


def highest_role(member: discord.Member, functional_roles: list):
    """Return the highest functional role a member has based on its position in the Discord role list."""

    # Get the actual role objects from the guild using their IDs
    guild_roles = [role for role in member.guild.roles if role.id in functional_roles]

    # Sort the guild roles by position in descending order (highest position first)
    sorted_roles = sorted(guild_roles, key=lambda x: x.position, reverse=True)

    # Iterate through the sorted roles and check if the member has each role
    for role in sorted_roles:
        if role in member.roles:
            return role.id

    return None
