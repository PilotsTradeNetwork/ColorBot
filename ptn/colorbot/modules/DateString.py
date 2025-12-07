"""
Module to return formatted date strings.

Depends on: none
"""

import time

# import libraries
from datetime import datetime
from ptn.colorbot.bot import bot


# get date and time
def get_formatted_date_string():
    bot.logger.debug("Called get_formatted_date_string")
    """
    Returns a tuple of the Elite Dangerous Time and the current real world time.

    :rtype: tuple
    """
    posix_time_string = int(time.time())
    bot.logger.debug(f"POSIX time is {posix_time_string}")

    dt_now = datetime.utcnow()

    current_time_string = dt_now.strftime("%Y%m%d_%H%M%S")
    bot.logger.debug(f"Current time string: {current_time_string}")

    return current_time_string, posix_time_string
