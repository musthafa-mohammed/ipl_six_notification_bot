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
                        if_six_hit_bool = True



    return if_six_hit_bool


print(if_six_hit())


