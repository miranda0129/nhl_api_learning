import requests
from pprint import pprint

print('scheduled games for the week, will show if currently live and score')
games_now_url = 'https://api-web.nhle.com/v1/score/now'
games_response = requests.get(games_now_url)
games_dict = games_response.json()
#pprint(games_dict)



print('DET schedule for the season')
schedule_url = 'https://api-web.nhle.com/v1/club-schedule-season/DET/now'
scedule_response = requests.get(schedule_url)
schedule_dict = scedule_response.json()
#pprint(schedule_dict)

print('details of specific game, DET vs CHI Wed Sep 25')
game_score_url = 'https://api-web.nhle.com/v1/gamecenter/2024010031/boxscore'
game_score_response = requests.get(game_score_url)
game_score_dict = game_score_response.json()
pprint(game_score_dict)

