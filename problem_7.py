# Problem 7

def find_nth_prime(n, limit=125000):
	if limit % 2 == 0:
		limit += 1
	primes = [True] * limit
	primes[0] = None
	primes[1] = None
	count = 0

	for ind, val in enumerate(primes):
		if val is True:
			# sieve out non-primes by multiples of known primes
			# slice array in strides of the index and replace them with False
			primes[ind*2::ind] = [False] * (((limit - 1)//ind) - 1)
			count += 1

		if count == n:
			return ind
	return False

print find_nth_prime(10001)