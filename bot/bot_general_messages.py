from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

from services.user_location_service import get_user_location


async def send_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Helper function to build the next inline keyboard."""
    try:
        existing_user_location = get_user_location(update.effective_user.id)
    except Exception as ex:
        existing_user_location = None

    keys = [
        [
            InlineKeyboardButton('Setup Location' if not existing_user_location else 'Change location',
                                 callback_data='/newlocation')
        ],
    ]
    if existing_user_location:
        keys.extend([
            [
                InlineKeyboardButton('Get current weather', callback_data='/current'),
            ],
            [
                InlineKeyboardButton('Get 5 days forecast', callback_data='/forecast5'),
                InlineKeyboardButton('Get 14 days forecast', callback_data='/forecast14'),
            ]
        ])
    await update.message.reply_text(
        text='Choose your action',
        reply_markup=InlineKeyboardMarkup(keys)
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
    )
    await update.message.reply_text(
        'Let\'s get started',
    )
    await send_menu(update, context)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text('To configure, please run /newlocation command to set up your location data')
