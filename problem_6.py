# Problem 6
# pass in value through command line

import sys
value = int(sys.argv[1])

def sum_of_squares(i):
	total = 0
	for i in range(1, i + 1):
		total += i ** 2

	return total

def square_of_sum(i):
	total = 0
	for i in range(1, i + 1):
		total += i

	total = total ** 2
	return total

def sum_square_diff(n):
	# find the sum of the squares
	first = sum_of_squares(n)
	second = square_of_sum(n)

	return second - first

print sum_square_diff(value)
