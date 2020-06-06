def merge(l):
	l.sort()
	merged = [l[0]]
	for x in l:
		a = merged[-1][0]
		b = merged[-1][1]
		c = x[0]
		d = x[1]
		###########################
		if d>b:
			if c>b: merged.append(x)
			else: merged[-1][1] = d
		###########################
	return merged

print(merge([[2, 4], [1, 2], [3, 5]]))
print(merge([[2,3],[1,3],[5,8],[4,6],[5,7]]))