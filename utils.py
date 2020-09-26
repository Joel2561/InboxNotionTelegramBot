import json
import logging

logger = logging.getLogger(__name__)

with open('configuration.json') as f:
    config = json.load(f)

TELEGRAM_TOKEN = config["telegram-bot-token"]
NOTION_TOKEN = config["notion-token"]
NOTION_TABLE_URL = config["inbox_table"]["table_url"]


def check_allowed_user(user_id):
    """
    check if allowed user
    :param user_id: telegram user id
    :return True if user is valid , False otherwise
    """
    valid_user = config["allowed_user_id"]
    user_id = str(user_id)
    return user_id == valid_user


def restrict_action(handled_action):
    """
    Wrapper for creating a private bot
    :param handled_action: the action to perform
    """
    def check_private(update, context):
        if not (check_allowed_user(update.message.from_user.id)):
            logging.warning("An unauthorized user attempted to use the bot. username: {}, id: {} .".format(
                update.message.from_user.username, update.message.from_user.id
            ))
            return
        else:
            return handled_action(update, context)

    return check_private
