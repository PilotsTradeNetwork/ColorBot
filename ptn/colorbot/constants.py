"""
Constants used throughout colorbot.

Depends on: nothing
"""

# libraries
import ast
import logging
import os
import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Define whether the bot is in testing or live mode. Default is testing mode.
_production = ast.literal_eval(os.environ.get("PTN_COLORBOT_SERVICE", "False"))

# define paths
TESTING_DATA_PATH = os.getcwd()  # defines the path for use in a local testing environment
DATA_DIR = os.getenv("PTN_COLORBOT_DATA_DIR", TESTING_DATA_PATH)

# Get the discord token from the local .env file. Deliberately not hosted in the repo or Discord takes the bot down
# because the keys are exposed. DO NOT HOST IN THE PUBLIC REPO.
# load_dotenv(os.path.join(DATA_DIR, '.env'))
load_dotenv(os.path.join(DATA_DIR, ".env"))

# define bot token
TOKEN = os.getenv("COLORBOT_DISCORD_TOKEN_PROD") if _production else os.getenv("COLORBOT_DISCORD_TOKEN_TESTING")

# Production variables
PROD_DISCORD_GUILD = 800080948716503040  # PTN server ID
PROD_CHANNEL_BOTSPAM = 801258393205604372  # PTN bot-spam channel
PROD_CHANNEL_BOTDEV = 878541974838312970  # PTN Colorbot Dev Channel
PROD_COUNCIL_ROLE = 800091021852803072  # PTN Council role
PROD_ALUMNI_ROLE = 1086777372981858404  # PTN Alumni role
PROD_MOD_ROLE = 813814494563401780  # PTN Mod role
PROD_SOMM_ROLE = 838520893181263872  # PTN Sommelier role
PROD_CONN_ROLE = 1105144902645448915  # PTN Connoisseur role
PROD_FO_ROLE = 948206870491959317  # PTN Faction Operative role
PROD_AGENT_ROLE = 948206174099103754  # PTN Agent role
PROD_CM_ROLE = 863521103434350613  # PTN Community Mentor role
PROD_PILLAR_ROLE = 863789660425027624  # PTN Community Pillar role
PROD_CCO_ROLE = 800091463160430654  # PTN Certified Carrier Owner role
PROD_GRAPE_ROLE = 1103957333467475968  # PTN Old Grape role
PROD_PATH_ROLE = 1257039137366605865  # PTN Pathfinder role
PROD_SPEC_ROLE = 1252708985501515967  # PTN Specialist role

# Production color roles
PROD_COLOR_ALUMNI_ROLE = 1166839581103095948
PROD_COLOR_SOMM_ROLE = 1166838603024969728
PROD_COLOR_CONN_ROLE = 1166839452904198244
PROD_COLOR_FO_ROLE = 1166838799423246357
PROD_COLOR_AGENT_ROLE = 1166839184007372870
PROD_COLOR_CM_ROLE = 1166838704325795921
PROD_COLOR_PILLAR_ROLE = 1166839065073700995
PROD_COLOR_CCO_ROLE = 1166838944109957240
PROD_COLOR_GRAPE_ROLE = 1166846264713941122
PROD_COLOR_PATH_ROLE = 1257331399636025375
PROD_COLOR_SPEC_ROLE = 1257331565126484019

# Testing variables
TEST_DISCORD_GUILD = 818174236480897055  # PANTS server ID
TEST_CHANNEL_BOTSPAM = 1422738543146569790  # PANTS bot spam channel
TEST_CHANNEL_BOTDEV = 1422738543146569790  # PANTS Colorbot Dev Channel
TEST_COUNCIL_ROLE = 877586918228000819  # PTN Council role
TEST_ALUMNI_ROLE = 1156729563188035664  # PTN Alumni role
TEST_MOD_ROLE = 903292469049974845  # PTN Mod role
TEST_SOMM_ROLE = 849907019502059530  # PTN Sommelier role
TEST_CONN_ROLE = 1105144147582656663  # PTN Connoisseur role
TEST_FO_ROLE = 1155985589200502844  # PTN Faction Operative role
TEST_AGENT_ROLE = 1242963395519713320  # PTN Agent role
TEST_CM_ROLE = 877586763672072193  # PTN Community Mentor role
TEST_PILLAR_ROLE = 903289927184314388  # PTN Community Pillar role
TEST_CCO_ROLE = 822999970012463154  # PTN Certified Carrier Owner role
TEST_GRAPE_ROLE = 1257320493539917935  # PTN Old Grape role
TEST_PATH_ROLE = 1257318927277756616  # PTN Pathfinder role
TEST_SPEC_ROLE = 1257318954951643198  # PTN Specialist role

# Testing color roles
TEST_COLOR_ALUMNI_ROLE = 1422738963998703668
TEST_COLOR_SOMM_ROLE = 1422739451456651425
TEST_COLOR_CONN_ROLE = 1422739534541754461
TEST_COLOR_FO_ROLE = 1422739631190966362
TEST_COLOR_AGENT_ROLE = 1422739709314207844
TEST_COLOR_CM_ROLE = 1422739779770122312
TEST_COLOR_PILLAR_ROLE = 1422739853279498323
TEST_COLOR_CCO_ROLE = 1422739956882866227
TEST_COLOR_GRAPE_ROLE = 1422740028349743194
TEST_COLOR_PATH_ROLE = 1422740084448563240
TEST_COLOR_SPEC_ROLE = 1422740133035380768

# Embed colours
EMBED_COLOUR_ERROR = 0x800000  # dark red
EMBED_COLOUR_QU = 0x00D9FF  # que?
EMBED_COLOUR_OK = 0x80FF80  # we're good here thanks, how are you?

# random gifs and images
error_gifs = [
    "https://media.tenor.com/-DSYvCR3HnYAAAAC/beaker-fire.gif",  # muppets
    "https://media.tenor.com/M1rOzWS3NsQAAAAC/nothingtosee-disperse.gif",  # naked gun
    "https://media.tenor.com/oSASxe-6GesAAAAC/spongebob-patrick.gif",  # spongebob
    "https://media.tenor.com/u-1jz7ttHhEAAAAC/angry-panda-rage.gif",  # panda smash
]


# images and icons used in embeds


# define constants based on prod or test environment
def bot_guild():
    return PROD_DISCORD_GUILD if _production else TEST_DISCORD_GUILD


guild_obj = discord.Object(bot_guild())


def channel_botspam():
    return PROD_CHANNEL_BOTSPAM if _production else TEST_CHANNEL_BOTSPAM


def channel_botdev():
    return PROD_CHANNEL_BOTDEV if _production else TEST_CHANNEL_BOTDEV


def council_role():
    return PROD_COUNCIL_ROLE if _production else TEST_COUNCIL_ROLE


def alumni_role():
    return PROD_ALUMNI_ROLE if _production else TEST_ALUMNI_ROLE


def mod_role():
    return PROD_MOD_ROLE if _production else TEST_MOD_ROLE


def somm_role():
    return PROD_SOMM_ROLE if _production else TEST_SOMM_ROLE


def conn_role():
    return PROD_CONN_ROLE if _production else TEST_CONN_ROLE


def fo_role():
    return PROD_FO_ROLE if _production else TEST_FO_ROLE


def agent_role():
    return PROD_AGENT_ROLE if _production else TEST_AGENT_ROLE


def cm_role():
    return PROD_CM_ROLE if _production else TEST_CM_ROLE


def pillar_role():
    return PROD_PILLAR_ROLE if _production else TEST_PILLAR_ROLE


def cco_role():
    return PROD_CCO_ROLE if _production else TEST_CCO_ROLE


def grape_role():
    return PROD_GRAPE_ROLE if _production else TEST_GRAPE_ROLE


def path_role():
    return PROD_PATH_ROLE if _production else TEST_PATH_ROLE


def spec_role():
    return PROD_SPEC_ROLE if _production else TEST_SPEC_ROLE


def color_alumni_role():
    return PROD_COLOR_ALUMNI_ROLE if _production else TEST_COLOR_ALUMNI_ROLE


def color_somm_role():
    return PROD_COLOR_SOMM_ROLE if _production else TEST_COLOR_SOMM_ROLE


def color_conn_role():
    return PROD_COLOR_CONN_ROLE if _production else TEST_COLOR_CONN_ROLE


def color_fo_role():
    return PROD_COLOR_FO_ROLE if _production else TEST_COLOR_FO_ROLE


def color_agent_role():
    return PROD_COLOR_AGENT_ROLE if _production else TEST_COLOR_AGENT_ROLE


def color_cm_role():
    return PROD_COLOR_CM_ROLE if _production else TEST_COLOR_CM_ROLE


def color_pillar_role():
    return PROD_COLOR_PILLAR_ROLE if _production else TEST_COLOR_PILLAR_ROLE


def color_cco_role():
    return PROD_COLOR_CCO_ROLE if _production else TEST_COLOR_CCO_ROLE


def color_grape_role():
    return PROD_COLOR_GRAPE_ROLE if _production else TEST_COLOR_GRAPE_ROLE


def color_spec_role():
    return PROD_COLOR_SPEC_ROLE if _production else TEST_COLOR_SPEC_ROLE


def color_path_role():
    return PROD_COLOR_PATH_ROLE if _production else TEST_COLOR_PATH_ROLE


any_moderation_role = [council_role(), mod_role()]
any_elevated_role = [
    council_role(),
    mod_role(),
    alumni_role(),
    somm_role(),
    conn_role(),
    fo_role(),
    agent_role(),
    cm_role(),
    pillar_role(),
    cco_role(),
    grape_role(),
    spec_role(),
    path_role(),
]
color_roles = [
    color_alumni_role(),
    color_somm_role(),
    color_conn_role(),
    color_fo_role(),
    color_agent_role(),
    color_cm_role(),
    color_pillar_role(),
    color_cco_role(),
    color_grape_role(),
    color_path_role(),
    color_spec_role(),
]

functional_roles = [
    alumni_role(),
    grape_role(),
    somm_role(),
    conn_role(),
    fo_role(),
    agent_role(),
    cm_role(),
    pillar_role(),
    cco_role(),
    spec_role(),
    path_role(),
]

# Mapping of functional roles to color roles
role_to_color = {
    alumni_role(): color_alumni_role(),
    grape_role(): color_grape_role(),
    somm_role(): color_somm_role(),
    conn_role(): color_conn_role(),
    fo_role(): color_fo_role(),
    agent_role(): color_agent_role(),
    cm_role(): color_cm_role(),
    pillar_role(): color_pillar_role(),
    cco_role(): color_cco_role(),
    path_role(): color_path_role(),
    spec_role(): color_spec_role(),
}

# define the logger for discord client and asyncpraw.
# TODO: use PTNLogger and extend to all MAB Logging
log_handler = logging.StreamHandler(sys.stdout)

loglevel_input = os.getenv("COLOR_BOT_LOG_LEVEL", "INFO")
match loglevel_input:
    case "CRITICAL":
        LOG_LEVEL = logging.CRITICAL

    case "ERROR":
        LOG_LEVEL = logging.ERROR

    case "INFO":
        LOG_LEVEL = logging.INFO

    case "DEBUG":
        LOG_LEVEL = logging.DEBUG

    case _:
        LOG_LEVEL = logging.INFO
