import math
def prime_factors(x):
	MAXN = 100001
	spf = [0 for i in range(MAXN)]
	spf[1] = 1
	for i in range(2, MAXN):
		spf[i] = i
	for i in range(4, MAXN, 2):
		spf[i] = 2
	for i in range(3, int(math.sqrt(MAXN))+1):
		if (spf[i] == i):
			for j in range(i * i, MAXN, i):
				if (spf[j] == j):
					spf[j] = i
	ret = list()
	while (x != 1):
		ret.append(spf[x])
		x = x // spf[x]
	return ret

#x = int(input())
x = 45
p = prime_factors(x)
print(p)