"""
Constants used throughout colorbot.

Depends on: nothing
"""

# libraries
import ast
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Define whether the bot is in testing or live mode. Default is testing mode.
_production = ast.literal_eval(os.environ.get('PTN_COLORBOT_SERVICE', 'False'))

# define paths
TESTING_DATA_PATH = os.path.join(os.getcwd())  # defines the path for use in a local testing environment
DATA_DIR = os.getenv('PTN_COLORBOT_DATA_DIR', TESTING_DATA_PATH)

# Get the discord token from the local .env file. Deliberately not hosted in the repo or Discord takes the bot down
# because the keys are exposed. DO NOT HOST IN THE PUBLIC REPO.
# load_dotenv(os.path.join(DATA_DIR, '.env'))
load_dotenv(os.path.join(DATA_DIR, '.env'))

# define bot token
TOKEN = os.getenv('COLORBOT_DISCORD_TOKEN_PROD') if _production else os.getenv('COLORBOT_DISCORD_TOKEN_TESTING')

# define bot object
bot = commands.Bot(command_prefix='c!', intents=discord.Intents.all())

# Production variables
PROD_DISCORD_GUILD = 800080948716503040  # PTN server ID
PROD_CHANNEL_BOTSPAM = 801258393205604372  # PTN bot-spam channel
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

# Production color roles
PROD_COLOR_COUNCIL_ROLE = 1
PROD_COLOR_ALUMNI_ROLE = 2
PROD_COLOR_MOD_ROLE = 3
PROD_COLOR_SOMM_ROLE = 4
PROD_COLOR_CONN_ROLE = 5
PROD_COLOR_FO_ROLE = 6
PROD_COLOR_AGENT_ROLE = 7
PROD_COLOR_CM_ROLE = 8
PROD_COLOR_PILLAR_ROLE = 9
PROD_COLOR_CCO_ROLE = 10
PROD_COLOR_GRAPE_ROLE = 11

# Testing variables
TEST_DISCORD_GUILD = 682302487658496057  # PANTS server ID
TEST_CHANNEL_BOTSPAM = 1166219023952920616  # PANTS bot spam channel
TEST_COUNCIL_ROLE = 1166198689388314714  # PTN Council role
TEST_ALUMNI_ROLE = 1166198733453672478  # PTN Alumni role
TEST_MOD_ROLE = 1166198849975627866  # PTN Mod role
TEST_SOMM_ROLE = 1166198981148291102  # PTN Sommelier role
TEST_CONN_ROLE = 1166199033883271330  # PTN Connoisseur role
TEST_FO_ROLE = 1166199159028723793  # PTN Faction Operative role
TEST_AGENT_ROLE = 1166199210471870534  # PTN Agent role
TEST_CM_ROLE = 1166199261092925532  # PTN Community Mentor role
TEST_PILLAR_ROLE = 1166199367171051640  # PTN Community Pillar role
TEST_CCO_ROLE = 1166199450516066376  # PTN Certified Carrier Owner role
TEST_GRAPE_ROLE = 1166208298496819313

# Testing color roles
TEST_COLOR_COUNCIL_ROLE = 1166207049986740344
TEST_COLOR_ALUMNI_ROLE = 1166207095960510536
TEST_COLOR_MOD_ROLE = 1166207314982883418
TEST_COLOR_SOMM_ROLE = 1166207417390989433
TEST_COLOR_CONN_ROLE = 1166207470822228058
TEST_COLOR_FO_ROLE = 1166207565932265582
TEST_COLOR_AGENT_ROLE = 1166207666859819100
TEST_COLOR_CM_ROLE = 1166207713580171294
TEST_COLOR_PILLAR_ROLE = 1166207776838668429
TEST_COLOR_CCO_ROLE = 1166207845868507237
TEST_COLOR_GRAPE_ROLE = 1166207975178903613

# Embed colours
EMBED_COLOUR_ERROR = 0x800000  # dark red
EMBED_COLOUR_QU = 0x00d9ff  # que?
EMBED_COLOUR_OK = 0x80ff80  # we're good here thanks, how are you?

# random gifs and images
error_gifs = [
    'https://media.tenor.com/-DSYvCR3HnYAAAAC/beaker-fire.gif',  # muppets
    'https://media.tenor.com/M1rOzWS3NsQAAAAC/nothingtosee-disperse.gif',  # naked gun
    'https://media.tenor.com/oSASxe-6GesAAAAC/spongebob-patrick.gif',  # spongebob
    'https://media.tenor.com/u-1jz7ttHhEAAAAC/angry-panda-rage.gif'  # panda smash
]


# images and icons used in embeds


# define constants based on prod or test environment
def bot_guild():
    return PROD_DISCORD_GUILD if _production else TEST_DISCORD_GUILD


guild_obj = discord.Object(bot_guild())


def channel_botspam():
    return PROD_CHANNEL_BOTSPAM if _production else TEST_CHANNEL_BOTSPAM


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


def color_council_role():
    return PROD_COLOR_COUNCIL_ROLE if _production else TEST_COLOR_COUNCIL_ROLE


def color_alumni_role():
    return PROD_COLOR_ALUMNI_ROLE if _production else TEST_COLOR_ALUMNI_ROLE


def color_mod_role():
    return PROD_COLOR_MOD_ROLE if _production else TEST_COLOR_MOD_ROLE


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


any_moderation_role = [council_role(), mod_role()]
any_elevated_role = [council_role(), mod_role(), alumni_role(), somm_role(), conn_role(), fo_role(), agent_role(),
                     cm_role(), pillar_role(), cco_role(), grape_role()]
color_roles = [
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

async def get_guild():
    """
    Return bot guild instance for use in get_member()
    """
    return bot.get_guild(bot_guild())
