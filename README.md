# ColorBot
A Discord bot to handle user color changes.

## Overview
Bot to handle the customization of user colors based on a user's role

## Target functions
- SlashCommand: `/color`: change a user's display color based on their roles
- SlashCommand `/reset_member_color`: reset a user's display color to their highest eligible role
- SlashCommand `/reset_all_member_roles`: reset all user's display colors to their highest eligible roles
## Architecture
- Discord.py 2.x

## First-Time Setup
- Clone the repository locally
- Set up Python 3.10+ venv
- Run the following commands inside the venv to complete installation:

    `pip install -e .`

    `pip install git+https://github.com/PilotsTradeNetwork/PTN-Library`
 
- Start the bot with

    `python .\ptn\colorbot\application.py`