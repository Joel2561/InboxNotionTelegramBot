from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import logging

from utils import TELEGRAM_TOKEN
from handlers import start, ask_new_url, get_url, get_description, cancel
from handlers import URL_URL, URL_DESCRIPTION

logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
updater = None


def start_bot():

    global updater

    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    conversation_url_handler = ConversationHandler(
        entry_points=[CommandHandler('url', ask_new_url)],

        states={
            URL_URL: [MessageHandler(Filters.text, get_url)],
            URL_DESCRIPTION: [MessageHandler(Filters.text, get_description)],

        },

        fallbacks=[MessageHandler(Filters.command, cancel)]
    )

    dispatcher.add_handler(conversation_url_handler)

    updater.start_polling(timeout=30)
    updater.idle()


start_bot()
