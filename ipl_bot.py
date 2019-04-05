import telegram



subscriber_list = []
bot = telegram.Bot(token="893131928:AAFtc2fiFDBn5tRdmp17RunwyLozMOqMw7Y")
while True:
    updates = bot.get_updates()
    chat_id = bot.get_updates()[-1].message.chat_id
    if not chat_id in subscriber_list:
        subscriber_list.append(chat_id)
        