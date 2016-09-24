players = [
  {
    'name': 'Paul Millsap',
    'position': 'PF',
    'avgMinutesPlayed': 36,
    'avgPoints': 16.4,
    'avgRebounds': 9.4,
    'starter': True
  },
  {
    'name': 'Jeff Teague',
    'position': 'PG',
    'avgMinutesPlayed': 28.6,
    'avgPoints': 15.6,
    'avgRebounds': 1.9,
    'starter': True
  },
  {
    'name': 'Al Horford',
    'position': 'C',
    'avgMinutesPlayed': 32,
    'avgPoints': 13.2,
    'avgRebounds': 6.8,
    'starter': True
  },
  {
    'name': 'Kent Bazemore',
    'position': 'SF',
    'avgMinutesPlayed': 31.8,
    'avgPoints': 12,
    'avgRebounds': 6.6,
    'starter': True
  },
  {
    'name': 'Kyle Korver',
    'position': 'SG',
    'avgMinutesPlayed': 32.4,
    'avgPoints': 11.2,
    'avgRebounds': 4.9,
    'starter': True
  },
  {
    'name': 'Dennis Schroder',
    'position': 'PG',
    'avgMinutesPlayed': 18.3,
    'avgPoints': 10.7,
    'avgRebounds': 1.8,
    'starter': False
  },
  {
    'name': 'Kris Humphries',
    'position': 'PF',
    'avgMinutesPlayed': 14.7,
    'avgPoints': 9.7,
    'avgRebounds': 5.7,
    'starter': False
  },
  {
    'name': 'Mike Scott',
    'position': 'PF',
    'avgMinutesPlayed': 17.6,
    'avgPoints': 7.0,
    'avgRebounds': 3.6,
    'starter': False
  },
  {
    'name': 'Thabo Sefolosha',
    'position': 'SF',
    'avgMinutesPlayed': 18.9,
    'avgPoints': 4.8,
    'avgRebounds': 3.9,
    'starter': False
  },
  {
    'name': 'Mike Muscala',
    'position': 'PF',
    'avgMinutesPlayed': 7.4,
    'avgPoints': 2.7,
    'avgRebounds': 1.9,
    'starter': False
  },
  {
    'name': 'Tim Hardaway Jr.',
    'position': 'SG',
    'avgMinutesPlayed': 9.7,
    'avgPoints': 2.2,
    'avgRebounds': 1.0,
    'starter': False
  },
  {
    'name': 'Lamar Patterson',
    'position': 'SG',
    'avgMinutesPlayed': 5.0,
    'avgPoints': 1.5,
    'avgRebounds': 1.3,
    'starter': False
  },
  {
    'name': 'Kirk Hinrich',
    'position': 'SG',
    'avgMinutesPlayed': 4.5,
    'avgPoints': 0.8,
    'avgRebounds': 0.7,
    'starter': False
  }
];

# Example loop
# for player in players:
#   for key, value in player.iteritems():
#     print key + ' - ' + str(value) #Same as player[key]


# * Print the average playing time of the players.
# * Print the average playing time of the starters.
# * Print the average playing time of the bench players.
# * Create an array of the names of each player.
# * Create an array of the names of the players who average more than 10 points per game.
# * Create an array of the names of the players who average more than 5 rebounds per game.
# * Who is the player with the most points per minute played? Write a program to find that out.
# * Based on this data, what is the average points score for the team as a whole?

total_avg_play = 0

# print "average playing time of the players:"
# for player in players:
#   total_avg_play += player['avgMinutesPlayed']
# avg_time = total_avg_play / len(players)
# print avg_time

# print "average playing time of starters:"
# for player in players:
#   if (player['starter']):
#       total_avg_play += player['avgMinutesPlayed']
# avg_time = total_avg_play / len(players)
# print avg_time

# print "average playing time of benched:"
# for player in players:
#   if player['starter'] == False :
#       total_avg_play += player['avgMinutesPlayed']
# avg_time = total_avg_play / len(players)
# print avg_time

# print "Player names: "
# player_array = []
# for player in players:
#   player_array.append(player['name'])
# print player_array

# print "More than 10 points a game:"
# player_array = []
# for player in players:
#   if player['avgPoints'] > 10:
#     player_array.append(player['name'])
# print player_array

# print "Most rebounds per game: "
# player_array = []
# for player in players:
#   if player['avgRebounds'] > 5:
#     player_array.append(player['name'])
# print player_array

# print "player with the most points per minute played: "
# player_mvp = ''
# player_mvp_ppm = 0
# for player in players:
#   ppm = player['avgPoints'] / player['avgMinutesPlayed']
#   if ppm > player_mvp_ppm:
#     player_mvp = player['name']
#     player_mvp_ppm = ppm
# print player_mvp + ': ' + str(player_mvp_ppm)

print "average points score for the team as a whole: "
points_total = 0
for player in players:
  points_total += player['avgPoints']
print points_total



