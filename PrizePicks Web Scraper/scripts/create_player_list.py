from find import find


def create_player_list(player_data):
  player_list = []
  
  # filter player_data down to just player objects
  players = list(filter(lambda d: d['type'] == 'new_player', player_data))
  for player in players:
    
    # check if player is our player_list based on their id
    player_id = player['id']
    is_in_list = find(player_list, 'id', player_id)

    # if not, create a player dict and append it to our player list
    if is_in_list == -1:
      player_dict = {
        'id': player_id,
        'name': player['attributes']['name'],
        'team': player['attributes']['team'],
      }
      player_list.append(player_dict)

  return player_list
