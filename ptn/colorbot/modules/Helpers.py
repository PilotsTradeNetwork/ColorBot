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

    :param roles: List of role IDs the user has
    :return: List of color role IDs the user can have
    """
    # Using sets for faster lookup
    roles_set = {role.id for role in roles}

    # Council members can have any color
    if council_role() in roles_set:
        print('Has council role')
        return [
            color_council_role(),
            color_alumni_role(),
            color_mod_role(),
            color_somm_role(),
            color_conn_role(),
            color_fo_role(),
            color_agent_role(),
            color_cm_role(),
            color_pillar_role(),
            color_cco_role(),
            color_grape_role()
        ]

    # Council alumni can have any color but council
    if alumni_role() in roles_set:
        return [
            color_alumni_role(),
            color_mod_role(),
            color_somm_role(),
            color_conn_role(),
            color_fo_role(),
            color_agent_role(),
            color_cm_role(),
            color_pillar_role(),
            color_cco_role(),
            color_grape_role()
        ]

    # Mod can have any role but the council ones
    if mod_role() in roles_set:
        return [
            color_mod_role(),
            color_somm_role(),
            color_conn_role(),
            color_fo_role(),
            color_agent_role(),
            color_cm_role(),
            color_pillar_role(),
            color_cco_role(),
            color_grape_role()
        ]

    allowed_colors = []

    # Grape, Somm, Conn hierarchy
    if grape_role() in roles_set:
        allowed_colors.extend([color_grape_role(), color_somm_role(), color_conn_role()])
    elif somm_role() in roles_set:
        allowed_colors.extend([color_somm_role(), color_conn_role()])
    elif conn_role() in roles_set:
        allowed_colors.append(color_conn_role())

    # FO, Agent hierarchy
    if fo_role() in roles_set:
        allowed_colors.extend([color_fo_role(), color_agent_role()])
    elif agent_role() in roles_set:
        allowed_colors.append(color_agent_role())

    # CM, Pillar hierarchy
    if cm_role() in roles_set:
        allowed_colors.extend([color_cm_role(), color_pillar_role()])
    elif pillar_role() in roles_set:
        allowed_colors.append(color_pillar_role())

    # CCO role (with no paired roles)
    if cco_role() in roles_set:
        allowed_colors.append(color_cco_role())

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
