import io
import os
from importlib import util
from pathlib import Path

from setuptools import setup

NAMESPACE = "ptn"
COMPONENT = "colorbot"

here = Path().absolute()

# Bunch of things to allow us to dynamically load the metadata file in order to read the version number.
# This is really overkill but it is better code than opening, streaming and parsing the file ourselves.

metadata_name = f"{NAMESPACE}.{COMPONENT}._metadata"
spec = util.spec_from_file_location(metadata_name, os.path.join(here, NAMESPACE, COMPONENT, "_metadata.py"))
metadata = util.module_from_spec(spec)
spec.loader.exec_module(metadata)

# load up the description field
with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name=f"{NAMESPACE}.{COMPONENT}",
    version=metadata.__version__,
    packages=[
        "ptn.colorbot",  # core
        "ptn.colorbot.botcommands",  # user interactions
        "ptn.colorbot.modules",  # various helper modules
        "ptn.colorbot.classes",  # classes used by the bot
    ],
    description="Pilots Trade Network Color Bot",
    long_description=long_description,
    author="Tug Nuggy",
    url="",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "colorbot=ptn.colorbot.application:run",
        ],
    },
    license="None",
    keyword="PTN",
    project_urls={
        "Source": "https://github.com/PilotsTradeNetwork/colorbot",
    },
    python_required=">=3.10",
)
