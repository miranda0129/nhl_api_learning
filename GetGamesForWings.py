import requests
from pprint import pprint

pprint('2024-2025 Detroid Red Wings Game Schedule')


#nhl games scheduled for DET
schedule_url = 'https://api-web.nhle.com/v1/club-schedule-season/DET/now'
scedule_response = requests.get(schedule_url)
schedule_dict = scedule_response.json()

for item in schedule_dict['games']:
    print('Game Date: ', item['gameDate'])
    print('Game Time: ', item['startTimeUTC'])
    print('State: ', item['gameState'])
    print('GameId: ', item['id'])
    #pprint(item)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

