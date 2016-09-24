# 1.    Write a function that takes a list of numbers as a parameter.
# Return the sum of all the numbers. Bonus: Add an error handler that returns the message, 
# The list must include only numbers if any non-numbers are included. You 
# will need to research a means to tell what data type an element is.
# 2.    Write a function that will take a list of numbers and returns
# all combinations of those numbers. Print them off to the screen on a new line.

# [9:24]  
# Bonus: Do permutations

#define a function that takes a list of numbers as a parameters
# assuming the list takes integers
# assuming that it is a list
# get some of the list and add the elements together
# bonus: check each element to see if it is an integer or not
# bonus: the list has floats inside
# steps: 
# 	loop through each eleement in list
# 	define variable called sum
#	add elements to a variable called sum
# import math
# import itertools

# the_list = [3,2,7,-9,40]

# def sum_of_num(list):
# 	sum = 0
# 	for i in range(0, len(list)):
# 		if (type(list[i]) is int):
# 			sum += list[i]
# 			# print sum
# 		elif (type(list[i]) is float):
# 			return "The list must include only whole numbers"
# 		else:
# 			return "This list must only include numbers"
# 	return sum

# print sum_of_num(the_list)

# take a list that returns all combinations of that list
#

# def comb_of_num(my_list):
# 	for i in range(1, len(my_list)):
# 		for x in itertools.combinations(my_list, i):
# 			print x

# 	print my_list

# print comb_of_num(the_list)

# 3.    Choose one of the array sorting algorithms:
# a.    bubble sort
# b.    selection sort
# c.    merge sort
# d.    quick sort

# and implement it.

# Your function will take in an array argument, and it will sort that array
#  in-place - as in, it will modify the array that is being sorted. For example:

# arr = [45, 3, 8, 2, 9, 10, 11]
# bubble_sort(arr)
# arr[2, 3, 8, 9, 10, 11, 45]
# Bonus: You are not allow to use:

# 1. append()
# 2. insert()
# 3. del
# 4. slicing
# 5. any other weird stuff other than arr[i], arr[i] = value, and len(arr).

# merge sort
# need to separate 


def merge_sort(alist):
	print ("splitting", alist)
	if (len(alist) > 1):
		mid = len(alist)//2
		leftlist = alist[:mid]
		rightlist = alist[mid:]

		merge_sort(leftlist)
		merge_sort(rightlist)

		x = 0
		y = 0
		z = 0

		while x < len(leftlist) and y < len(rightlist):
			if (leftlist[x] < rightlist[y]):
				alist[z] = leftlist[x]
				x = x + 1
			else:
				alist[z] = rightlist[y]
				y = y + 1
			z = z + 1

		while x < len(leftlist):
			alist[z] = leftlist[x]
			x = x + 1
			z = z + 1

		while y < len(rightlist):
			alist[z] = rightlist[y]
			y = y + 1
			z = z + 1

	print("merging", alist)

alist = [54,26,93,17,77,31,44,55,20]
merge_sort(alist)
print(alist)






