def create_stat_list(player_data):
  stat_list = []
  stats = list(filter(lambda d: d['type'] == 'stat_type', player_data))

  for stat in stats:
    stat_list.append(stat['attributes']['name'])

  return stat_list
