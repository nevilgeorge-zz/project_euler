# Problem 5

# SLOW RUNTIME

# 20 covers 2, 4, 5, 10, 20
# 19 covers 19
# 18 covers 3, 6, 9, 18
# 17 covers 17
# 16 covers 8, 16
# 15 covers 15
# 14 covers 7, 14
# 13 covers 13
# 12 covers 12
# 11 covers 11

def find_smallest_multiple(limit):
	found = False
	start = limit
	while not found:

		for i in range(1, limit + 1):
			if start % i == 0:
				found = True
			else:
				found = False
				break
		if found:
			return start
			break
		start += limit

print find_smallest_multiple(20)
