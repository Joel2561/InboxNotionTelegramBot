# InboxNotionTelegramBot
This bot is intended to be a simple demo on how to write data to Notion tables through Telegram bot.
It also built to be a "private" bot, defensively checking for the user_id to allow only one user to use the bot.

This demo uses the amazing unofficial Notion API (https://github.com/jamalex/notion-py) 

## How it works
The implementation consists on an inbox saving URL and a relevant description to a given Notion Table.
After the user selects the **\url** command, the bot will first ask for an URL and then a description.
 
As a simple demo, the tables headers are the one of the basic Notion table that you obtain by selecting "Table" 
on a new empty page.  If you wanted to work with different headers name, you will have to modify the code in **notion_writer.py**

Only one allowed user will be able to work with the bot. The bot will work any other user-id that is not the one configured.
 
## How to run
First, you need to configure the configuration.json files . See **Parameters** section.

After that, simply run:
```
    python bot.py
```


## Parameters
In order to run the bot, you will have to set the parameters in **configuration.json**. 

### Precautions
**configuration.json** file will contain the telegram bot token and the Notion token:

> Do not share or upload anywhere this file, since anyone that sees this information will have 
to access your bot or Notion account.  

Also

> for a real persistent application please consider other safer methods to store tokens

A simple alternative in described here: https://towardsdatascience.com/how-to-hide-your-api-keys-in-python-fb2e1a61b0a0

----

### Configuration
In **configuration.json**:

- **telegram-bot-token**: Your telegram bot token. To create a token, please follow official procedure: 
https://core.telegram.org/bots#6-botfather

- **notion-token**: Notion-v2 token. If you can find it following, for example, this guide. 
https://www.redgregory.com/notion/2020/6/15/9zuzav95gwzwewdu1dspweqbv481s5 

- **table_url**: The Notion table URL. 

- **allowed_user_id**: the id of the telegram user that will use the bot. (= your telegram id).
The simpler way to find it is ask it to the following bot: https://t.me/userinfobot
