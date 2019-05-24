n = int(input("n: "))
print(0, 1, end=" ")
for i in range(3, n+1):
	print(round(0.4472*(1.6180)**i), end=" ")