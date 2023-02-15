#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import __version__ as TG_VER

from api_keys import TELEGRAM_API_KEY
from bot.bot_general_messages import start, help_command
from bot.weather_messages import setup_location, save_location, get_current_weather_data, get_forecast_weather_data_5, \
    get_forecast_weather_data_14

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler, \
    CallbackQueryHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TELEGRAM_API_KEY).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("newlocation", setup_location))
    application.add_handler(CommandHandler("current", get_current_weather_data))
    application.add_handler(CommandHandler("forecast5", get_forecast_weather_data_5))
    application.add_handler(CommandHandler("forecast14", get_forecast_weather_data_14))

    application.add_handler(CallbackQueryHandler(setup_location, pattern='^/newlocation$'))
    application.add_handler(CallbackQueryHandler(get_current_weather_data, pattern='^/current$'))
    application.add_handler(CallbackQueryHandler(get_forecast_weather_data_5, pattern='^/forecast5$'))
    application.add_handler(CallbackQueryHandler(get_forecast_weather_data_14, pattern='^/forcast14$'))

    application.add_handler(MessageHandler(filters.LOCATION, save_location))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
