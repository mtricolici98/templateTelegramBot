from telegram import Update
from telegram.ext import ContextTypes

from bot.bot_general_messages import send_menu
from services.user_location_service import create_or_update_user_location, get_user_location
from weather.weather import get_weather


def _validate_not_updating_location(context):
    store_procedure = context.chat_data.get('storing_location')
    if store_procedure:
        raise Exception('You didn\'t finish setting up your location, please reply with a location.')


async def setup_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.chat_data['storing_location'] = True
    cb_query = update.callback_query
    if cb_query:
        # In caz ca avem callback query (adica rulam din buton, modificam mesajul existent)
        await cb_query.answer()
        await cb_query.edit_message_text('Hey, reply with a new location now!')
    else:
        # In caz ca nu avem callback query (adica rulam din comanda) trimitem un mesaj nou.
        await update.effective_chat.send_message('Hey, reply with a new location now!')


def format_weather_message(data: dict):
    return f'It is {data["weather"]} with a temperature of {data["temp"]} at your location.'


async def get_current_weather_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        _validate_not_updating_location(context)
        location_data = get_user_location(update.effective_user.id)
        weather_data = get_weather(dict(lat=location_data.lat, lon=location_data.lon))
        msg = format_weather_message(weather_data)
        await update.effective_chat.send_message(msg)
        await send_menu(update, context)
    except Exception as ex:
        await update.message.reply_text(str(ex))


async def get_forecast_weather_data_5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_chat.send_message('Not implemented')


async def get_forecast_weather_data_14(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_chat.send_message('Not implemented')


async def save_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    store_procedure = context.chat_data.get('storing_location')
    if not store_procedure:
        await update.effective_chat.send_message('You sent me a location, but I don\'t know what to do with it.')
        return
    location = update.effective_message.location
    if not location:
        return
    create_or_update_user_location(update.effective_user.id, location.latitude, location.longitude)
    context.chat_data['storing_location'] = False
    await update.effective_chat.send_message('Got it, here is some current weather data for your location.')
    await get_current_weather_data(update, context)
