import logging
from utils import restrict_action
from notion_writer import check_connectivity, is_valid_table, write_to_table
from telegram.ext import ConversationHandler

logger = logging.getLogger(__name__)

URL_URL, URL_DESCRIPTION = range(2)


@restrict_action
def start(update, context):
    """
    Start only if one of the allowed users.
    Also check if token is valid and table url is ok
    """

    if not check_connectivity():
        update.message.reply_text("Token not valid")
    elif not is_valid_table():
        update.message.reply_text("Table not valid. Be sure you have pasted the Table url")
    else:
        update.message.reply_text(r"All is good to go! Digit /url to start saving links")


@restrict_action
def ask_new_url(update, context):
    logger.debug("Asking new URL")
    update.message.reply_text('please send me the URL  to be saved to Notion')
    return URL_URL


@restrict_action
def get_url(update, context):
    logger.debug("get_url function")
    text = update.message.text
    context.user_data['url'] = text
    logger.debug("storing {}".format(text))
    update.message.reply_text(
        'Ok. Now give me a brief description')
    return URL_DESCRIPTION


@restrict_action
def get_description(update, context):
    logger.debug("get_description function")
    description = update.message.text

    done = write_to_table(context.user_data['url'], description)
    if done:
        update.message.reply_text(
            'Successfully uploaded')
    else:
        update.message.reply_text('Could not upload: try /start to diagnose')
    return ConversationHandler.END


@restrict_action
def cancel(update, context):
    logger.debug("cancelling data")
    user_data = context.user_data
    if 'url' in user_data:
        del user_data['url']
    return ConversationHandler.END
