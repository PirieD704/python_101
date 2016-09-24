# Arrays... are changeable. If, for some reason, you wanted an array but it couldn't be changed... enter tuples

# a_list = [1,2,3]
a_tuple = (1,2,3)
# print a_list[2]
print a_tuple[2]
# a_list[2] = 4
# print a_list[2]
# a_tuple[2] = 4
for single_tuple in a_tuple:
	print single_tuple

atlanta_teams = ('falcons', 'hawks', 'atl united', 'silverbacks')
for team in atlanta_teams:
	if team == 'hawks':
		print 'you are cheering for the basketball team ' + team