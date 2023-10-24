import discord

# regular roles to check
from ptn.colorbot.constants import (
    council_role,
    alumni_role,
    mod_role,
    somm_role,
    conn_role,
    fo_role,
    agent_role,
    cm_role,
    pillar_role,
    cco_role,
    grape_role
)

# The color role functions
from ptn.colorbot.constants import (
    color_council_role,
    color_alumni_role,
    color_mod_role,
    color_somm_role,
    color_conn_role,
    color_fo_role,
    color_agent_role,
    color_cm_role,
    color_pillar_role,
    color_cco_role,
    color_grape_role
)
# functions
from ptn.colorbot.constants import color_roles


def color_permission_check(roles: list):
    """
    Check what colors a user can have based on their roles.

    :param roles: List of discord.Role objects the user has
    :return: List of color role IDs the user can have
    """
    # Transforming the list of Role objects to a set of role IDs
    roles_set = {role.id for role in roles}

    # Mapping roles to their respective color roles
    role_to_color = {
        council_role(): color_council_role(),
        alumni_role(): color_alumni_role(),
        mod_role(): color_mod_role(),
        grape_role(): color_grape_role(),
        somm_role(): color_somm_role(),
        conn_role(): color_conn_role(),
        fo_role(): color_fo_role(),
        agent_role(): color_agent_role(),
        cm_role(): color_cm_role(),
        pillar_role(): color_pillar_role(),
        cco_role(): color_cco_role()
    }

    # Collecting colors for the roles the user has
    allowed_colors = [role_to_color[role] for role in roles_set if role in role_to_color]

    return allowed_colors




async def remove_color(interaction: discord.Interaction, member: discord.Member = None):
    """Removes color roles from a member."""

    # If no member is mentioned, assume the command caller
    if not member:
        member = interaction.user

    # Check for color roles the member has
    roles_to_remove = [role for role in member.roles if role.id in color_roles]

    if roles_to_remove:
        await member.remove_roles(*roles_to_remove)
        print(f"Removed {len(roles_to_remove)} color role(s) from {member.name}.")
    else:
        print("{member.name} has no color roles.")


def is_color_role(role: discord.Role) -> bool:
    """Check if a given role is a color role."""
    return role.id in color_roles
