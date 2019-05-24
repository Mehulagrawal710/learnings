import math
def is_prime(x):
    if x is 0 or x is 1:
        return False
    if x is 2 or x is 3:
        return True
    if x%2 is 0 or x%3 is 0:
    	return False
    z = int(math.sqrt(x)) + 1
    for i in range(5, z, 2):
    	if x % i == 0:
    		return False
    return True

for i in range(100):
	print(i, is_prime(i))