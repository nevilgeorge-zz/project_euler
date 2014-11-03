# Problem 9
# both solutions work

limit = 1000

# def find_pyth_triple(limit):
# 	for a in range(1, limit):
# 		for b in range(1, limit - a):
# 			c = limit - a - b
# 			if c ** 2 == a ** 2 + b ** 2:
# 				return a * b * c

# 	return 0

# print find_pyth_triple(limit)


def find_pyth_triple(limit):
	for a in range(1, limit):
		for b in range(1, limit - a):
			c = (a ** 2 + b ** 2) ** 0.5
			if a + b + c == 1000:
				return int(a * b * c)

	return 0

print find_pyth_triple(limit)