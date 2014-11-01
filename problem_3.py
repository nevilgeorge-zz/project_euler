# Problem 3

import sys
original = int(sys.argv[1])


def checkPrime(value):
	# check if there is a factor that is not value or 1
	for i in range(value - 1, 1, -1):
		if value % i == 0:
			return False

	return True

def primeFactor(value):
	# a factor cannot be larger than the root of the input
	limit = original ** (0.5)
	limit = int(round(limit))
	# count downwards from the limit because you want to find the largest one
	for i in range(limit, 1, -1):
		if original % i == 0:
			if checkPrime(i):
				return i

print primeFactor(original)