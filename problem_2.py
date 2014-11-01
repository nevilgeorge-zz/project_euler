# Problem 2

import sys
limit = int(sys.argv[1])

def even_fib(limit):
	result = 0;
	a = 0
	b = 1
	while b < limit:
		a = b
		b = a + b
		if b % 2 == 0:
			result += b
	return result

print even_fib(limit)
