import telegram
import threading
import time
from json_parser import if_six_hit




	



subscriber_list = []
bot = telegram.Bot(token="893131928:AAFtc2fiFDBn5tRdmp17RunwyLozMOqMw7Y")



def broadcaster():
    while True:
        time.sleep(30)
        if if_six_hit():
            for subscriber in subscriber_list:
               bot.send_message(chat_id=subscriber, text="I'm sorry Dave I'm afraid I can't do that.") 

broadcaster_thread = threading.Thread(target=broadcaster, args=())
broadcaster_thread.start()

while True:
    updates = bot.get_updates()
    chat_id = bot.get_updates()[-1].message.chat_id
    if not chat_id in subscriber_list:
        subscriber_list.append(chat_id)
        
