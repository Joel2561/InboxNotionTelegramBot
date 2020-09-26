from notion.client import NotionClient
from utils import NOTION_TOKEN, NOTION_TABLE_URL
from requests.exceptions import HTTPError


def check_connectivity():
    """
        Return True if Token is valid, False otherwise
        """

    try:
        NotionClient(token_v2=NOTION_TOKEN)
        return True
    except HTTPError:
        return False


def is_valid_table():
    """
    Return True if table is valid
    """
    client = NotionClient(token_v2=NOTION_TOKEN)
    try:
        client.get_collection_view(NOTION_TABLE_URL)
        return True
    except AssertionError:
        return False


def write_to_table(url, description):
    """
    Add data to table: True if done, False if not
    :param url:
    :param description:
    :return:
    """

    if not check_connectivity():
        return False
    else:
        client = NotionClient(token_v2=NOTION_TOKEN)
        if not is_valid_table():
            return False
        else:
            cv = client.get_collection_view(NOTION_TABLE_URL)
            row = cv.collection.add_row()
            row.name = description
            row.files = url
            # add here attributes
            return True
