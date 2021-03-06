print "David P"
# Arrays... psyche. Lists.
animals = ['wolf', 'giraffe', 'hippo']
print animals[-1]

# How do we push to the array/list?
animals.append("croc")
# print animals

# What about deleting?
animals.remove("wolf")
# print animals

# We can insert at any position with ... insert
animals.insert(0,'zebra')
print animals

#remove via del
del animals[0]
print animals

# Pop, is just good old Pop
dc_class = ['Summer', 'Jackson', 'Danny', 'Dave', 'Jt', 'Eric', 'Paige', 'Brett', 'Danielle', 'Alex', 'Dan', 'Shirlette']
# will sort, but not change the actual array
# print sorted(dc_class)
# will sort, and change the list
# dc_class.sort()
# will reverse the indeces and change the list
dc_class.reverse()
#len method, will work like .length in JS
# print len(dc_class)

# Indentation matters to Python!
for student in dc_class:
	print student

for i in range(1,10):
	print i

for i in range(1, len(dc_class)):
	print i

# a function is not called a function. It's defined by: def
def sayHello():
	print "Hello"

sayHello()

def say_hello_with_name(name):
	print "Hello, " + name

say_hello_with_name("David")

#make squares
squares = []
for i in range(1,11):
	# Two * is square
	square = i**2
	# Push that square onto the list
	squares.append(square)
print squares

#Random list of digits
digits = [12,235,15,213,42,23,3245,2342,2352,234,2,28,34141,12341]
# Max and min
print min(digits)
print max(digits)
print sum(digits)

squares = [i**2 for i in range(1,11)]
print squares

# step = the incrament
print range(1,11,2)

# slice in python is all about the :
dc_team = ["Max", "Jake", "Rob", "Toby", "Natalie"]
team_part = dc_team[1:3]
print team_part
team_part = dc_team[1:-1]
print team_part
team_part = dc_team[:1]
print team_part
team_part = dc_team[2:]
print team_part
# Will keep a connnect so both will change when one does
team_copy = dc_team
print team_copy
print dc_team
#make a new list, independent
team_copy = list(dc_team)
team_copy.append("DeAnn")
print team_copy
print dc_team

team_copy = dc_team[:]
team_copy.append("DeAnn")
print team_copy
print dc_team






