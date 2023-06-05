import csv
import requests

from create_player_list import create_player_list
from create_stat_list import create_stat_list
from find import find

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Dnt': '1',
    'cache-control': 'max-age=0',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'application/geo+json',
    'Accept-Language': 'en',
    'origin': 'https://app.prizepicks.com'
}

payload = {
    'per_page': '1000',
    'single_stat': 'true',
}

# Making the initial request
initial_request = requests.get('https://partner-api.prizepicks.com/projections', params=payload, headers=HEADERS, timeout=30)
# Parsing the response JSON
pp_data = initial_request.json()

# Creating a list of players and stats available for the request
player_list = create_player_list(pp_data['included'])
stat_list = create_stat_list(pp_data['included'])

# List to store all lines
all_lines = []

# Iterate over the stats that lines are set for
for stat in stat_list:
    # Filter all of the returned data down to the current stat
    filtered_data = list(filter(lambda d: d['attributes']['stat_type'] == stat, pp_data['data']))
    
    # For each player in the filtered data, find the player's name from the
    # player list using the player_id, then create a dict for that line with the
    # player's name and line. Then append that line dict to the all_lines list
    for player in filtered_data:
        player_id = player['relationships']['new_player']['data']['id']
        player_index = find(player_list, 'id', player_id)
        player_name = player_list[player_index]['name']
        line = {
            'player': player_name,
            'stat': stat,
            'line': player['attributes']['line_score']
        }
        all_lines.append(line)

# Grab the keys for the CSV file, then write the CSV file to the output folder
keys = all_lines[0].keys()
with open('output.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_lines)
