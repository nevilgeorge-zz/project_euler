# Problem 1

import sys
limit = int(sys.argv[1])

result = 1
for i in range(1, limit):
	if i % 3 == 0 or i % 5 == 0:
		result += 1

print result
