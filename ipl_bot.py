import telegram
import threading
import time
import json
import urllib.request

match_json = {}

privious_over_details = {}
prevoius_over_last_run = {}

def if_six_hit():
    if_six_hit_bool = False
    with urllib.request.urlopen("https://www.cricbuzz.com/match-api/livematches.json") as url:
        match_json = json.loads(url.read().decode())
    for match_id,match in match_json['matches'].items():
        if match['series']['name'] == "Indian Premier League 2019":
            if 'score' in match:
                prev_over = match['score']['prev_overs']
                if not match_id in  privious_over_details:
                    prevoius_over_last_run[match_id] = prev_over[-2:]
                    privious_over_details[match_id] = prev_over
                else:
                    if prev_over[-2:] == "1" and len(privious_over_details[match_id]) != len(prev_over):
                        privious_over_details[match_id] = prev_over
                        if_six_hit_bool = True
    return if_six_hit_bool



	



subscriber_list = []
bot = telegram.Bot(token="893131928:AAFtc2fiFDBn5tRdmp17RunwyLozMOqMw7Y")
html = ""


def broadcaster():
    while True:
        time.sleep(4)
        print("if six::::"+str(if_six_hit()))
        if if_six_hit():
            for subscriber in subscriber_list:
            #    bot.send_message(chat_id=subscriber, text="I'm sorry Dave I'm afraid I can't do that.",parse_mode=telegram.ParseMode.HTML) 
                print("hi")
broadcaster_thread = threading.Thread(target=broadcaster, args=())
broadcaster_thread.start()

while True:
    updates = bot.get_updates()
    if updates:
        chat_id = bot.get_updates()[-1].message.chat_id
        if not chat_id in subscriber_list:
            subscriber_list.append(chat_id)
        
