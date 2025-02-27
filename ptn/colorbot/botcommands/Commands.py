# discord.py
import asyncio

import discord
from discord import app_commands
from discord.app_commands import describe
from discord.ext import commands

# import bot
from ptn.colorbot.bot import bot

# local constants
from ptn.colorbot._metadata import __version__
import ptn.colorbot.constants as constants
from ptn.colorbot.constants import council_role, mod_role, functional_roles
# local modules
from ptn.colorbot.modules.ErrorHandler import on_app_command_error, CustomError, on_generic_error
from ptn.colorbot.modules.Helpers import color_permission_check, remove_color, is_color_role, highest_role


class Commands(commands.Cog):
    def __init__(self, bot: commands.Cog):
        self.bot = bot

    def cog_load(self):
        tree = self.bot.tree
        self._old_tree_error = tree.on_error
        tree.on_error = on_app_command_error

    def cog_unload(self):
        tree = self.bot.tree
        tree.on_error = self._old_tree_error

        # ping command to check if the bot is responding

    @commands.command(name='ping', aliases=['hello', 'ehlo', 'helo'],
                      help='Use to check if colorbot is online and responding.')
    @commands.has_any_role(*constants.any_moderation_role)
    async def ping(self, ctx):
        print(f"{ctx.author} used PING in {ctx.channel.name}")
        embed = discord.Embed(
            title="🟢 COLOR BOT ONLINE",
            description=f"🌈<@{bot.user.id}> connected, version **{__version__}**.",
            color=constants.EMBED_COLOUR_OK
        )
        await ctx.send(embed=embed)

        # command to sync interactions - must be done whenever the bot has appcommands added/removed

    @commands.command(name='sync', help='Synchronise colorbot interactions with server')
    @commands.has_any_role(*constants.any_moderation_role)
    async def sync(self, ctx):
        print(f"Interaction sync called from {ctx.author.display_name}")
        async with ctx.typing():
            try:
                bot.tree.copy_global_to(guild=constants.guild_obj)
                await bot.tree.sync(guild=constants.guild_obj)
                print("Synchronised bot tree.")
                await ctx.send("Synchronised bot tree.")
            except Exception as e:
                print(f"Tree sync failed: {e}.")
                return await ctx.send(f"Failed to sync bot tree: {e}")

    @app_commands.command(name='color', description='Changes your desired display color')
    @commands.has_any_role(*constants.any_elevated_role)
    @describe(role='the desired role you want the color from')
    async def color(self, interaction: discord.Interaction, role: discord.Role):
        print(f'Color change called from {interaction.user.display_name}')
        guild = interaction.guild
        user = interaction.user
        allowed_colors = color_permission_check(user.roles)
        print(allowed_colors)

        if not is_color_role(role):
            try:
                raise CustomError('That role isn\'t a color role!')
            except Exception as e:
                return await on_generic_error(interaction=interaction, error=e)

        # check if user is allowed to have the color
        if role.id not in allowed_colors:
            try:
                raise CustomError('You don\'t have access to that role!')
            except Exception as e:
                return await on_generic_error(interaction=interaction, error=e)

        else:
            # remove any other colors
            await remove_color(interaction=interaction, member=user)
            await user.add_roles(role)

            embed = discord.Embed(title=f'✅ Gave you the {role.name} color!', color=constants.EMBED_COLOUR_OK)
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name='reset_member_color', description='Admin command for reseting a member\'s color')
    @commands.has_any_role(mod_role(), council_role())
    @describe(member='the member to reset')
    async def reset_member_colors(self, interaction: discord.Interaction, member: discord.Member):
        guild = interaction.guild

        functional_role_list = []
        for role_id in functional_roles:
            role = discord.utils.get(guild.roles, id=role_id)
            if role:
                functional_role_list.append(role)

        top_role = highest_role(member, functional_roles)
        if top_role:
            print(top_role)
            color_role_id = constants.role_to_color.get(top_role)
            color_role = guild.get_role(color_role_id)
            print(color_role)
            if color_role:
                await remove_color(interaction=interaction, member=member)
                await member.add_roles(color_role)
                embed = discord.Embed(description=f"✅ Reset <@{member.id}>'s color!", color=constants.EMBED_COLOUR_OK)
                await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            try:
                raise CustomError('That user is not elevated!')
            except Exception as e:
                return await on_generic_error(interaction=interaction, error=e)

    @app_commands.command(name='reset_all_members_color',
                          description='Admin command for resetting all member\'s colors')
    @commands.has_any_role(constants.council_role())
    async def reset_member_all_colors(self, interaction: discord.Interaction):

        # Notify user the process is starting
        initial_message = discord.Embed(title=f'🔄 Starting to reset all elevated members\' colors...',
                                        color=constants.EMBED_COLOUR_OK)
        await interaction.response.send_message(embed=initial_message, ephemeral=True)

        # Define a separate asynchronous task for the main operation
        async def reset_colors():
            guild = interaction.guild

            functional_role_list = []
            for role_id in functional_roles:
                role = discord.utils.get(guild.roles, id=role_id)
                if role:
                    functional_role_list.append(role)

            processed_members = set()  # Keep track of members who had their color removed

            for role in functional_role_list:
                for member in role.members:
                    if member.id in processed_members:  # Skip if member's color was already processed
                        continue

                    top_role = highest_role(member, functional_roles)
                    if top_role:
                        color_role_id = constants.role_to_color.get(top_role)
                        color_role = discord.utils.get(guild.roles, id=color_role_id)
                        if color_role:
                            await remove_color(interaction=interaction, member=member)
                            await member.add_roles(color_role)
                            processed_members.add(member.id)  # Add member to processed set

            # Notify user the process is complete
            completion_message = discord.Embed(title=f'✅ Finished resetting all elevated members\' colors.',
                                               color=constants.EMBED_COLOUR_OK)
            try:
                await interaction.followup.send(embed=completion_message, ephemeral=True)
            except Exception as e:
                print(f"Error sending completion message: {e}")

        # Launch the main operation as a separate asynchronous task
        await asyncio.create_task(reset_colors())


