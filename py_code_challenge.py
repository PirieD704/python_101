# 1.
full_name = "David Pirie"
age = 27

# 2.
my_array = []
my_array.append(full_name)
my_array.append(age)
print (my_array)

# 3.
def say_hello():
	print "Hello!"
say_hello()

# 4.
split_name = full_name.split()
print split_name

# 5. 
def say_name():
	print "Hello, " + split_name[0]
say_name()

# 6.
def my_age(age):
	print age
my_age(my_array[1])

# 7.
def sum_odd_numbers():
	sum = 0
	for i in range(1, 5000):
		if(i % 2 != 0):
			sum += i
	print sum
sum_odd_numbers()