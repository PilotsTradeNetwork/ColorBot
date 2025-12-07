"""
Constants used throughout colorbot.

Depends on: nothing
"""

# libraries
import os

from dotenv import load_dotenv

# define paths
TESTING_DATA_PATH = os.getcwd()  # defines the path for use in a local testing environment
DATA_DIR = os.getenv("PTN_DATA_DIR", TESTING_DATA_PATH)

# Get the discord token from the local .env file. Deliberately not hosted in the repo or Discord takes the bot down
# because the keys are exposed. DO NOT HOST IN THE PUBLIC REPO.
load_dotenv(os.path.join(DATA_DIR, ".env"))

# random gifs and images
error_gifs = [
    "https://media.tenor.com/-DSYvCR3HnYAAAAC/beaker-fire.gif",  # muppets
    "https://media.tenor.com/M1rOzWS3NsQAAAAC/nothingtosee-disperse.gif",  # naked gun
    "https://media.tenor.com/oSASxe-6GesAAAAC/spongebob-patrick.gif",  # spongebob
    "https://media.tenor.com/u-1jz7ttHhEAAAAC/angry-panda-rage.gif",  # panda smash
]
