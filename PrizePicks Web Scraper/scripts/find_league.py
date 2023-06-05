import sys

# takes in a string representing a prize picks league and returns the string version of the league id for the request

def find_league(league_argv):
  print('\
  ---------------------\n\
  Searching for lines for {0}\n\
  ---------------------'.format(league_argv)
  )
  LEAGUES = [
    ('NFL', '9'),
    ('NFL1H', '35'),
    ('MLB', '2'),
    ('MLBLIVE', '231'),
    ('Soccer', '8'),
    ('NBASZN', '173'),
    ('PGA', '1'),
    ('Tennis', '5'),
    ('CFB', '15'),
    ('NHLSZN', '236')
  ]

  available_leagues = ''
  league_found = False
  for league in LEAGUES:
    available_leagues += '\n{0}'.format(league[0], )
    if str(league_argv) == league[0]:
      league_id = league[1]
      league_found = True

  if league_found == True:
    return league_id
  else:
    sys.exit('Please supply a valid league name. Valid league names include: {0}'.format(available_leagues))

