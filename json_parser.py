import json
import urllib.request

match_json = {}

#This dictionary stores the following
# match_id : { old_batsman_1_id,old_batsman_2_id,old_batsman_1_sixes,old_batsman_2_sixes,new_batsman_1_id,new_batsman_2_id,new_batsman_1_sixes,new_batsman_2_sixes }
matches_and_batsman = {}


def if_six_hit():
    with urllib.request.urlopen("https://www.cricbuzz.com/match-api/livematches.json") as url:
        match_json = json.loads(url.read().decode())
    for match_id,match in match_json['matches'].items():
        if match['series']['name'] == "CSA T20 Challenge 2019":
            if not match_id in matches_and_batsman:
                #matches_and_batsman[match_id] = { old_batsman_1_id,old_batsman_2_id,old_batsman_1_sixes,old_batsman_2_sixes,new_batsman_1_id,new_batsman_2_id,new_batsman_1_sixes,new_batsman_2_sixes}
                pass
            if 'score' in match:
                batsman1 = match['score']['batsman'][0]
                batsman2 = match['score']['batsman'][1]

                current_batsamn_1 = batsman1['id']
                current_batsamn_2 = batsman2['id']


                # if batsman1['id'] != current_batsamn_1:
                #     print("New batsamn 1")
                print(batsman1)
                print(batsman2)


if_six_hit()


