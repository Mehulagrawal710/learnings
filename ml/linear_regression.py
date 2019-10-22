import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#reading data file
data = pd.read_csv('datasets/headbrain.csv')
print(data.shape)
print(data.head())

#getting x, y values
x = data['Head Size(cm^3)'].values
y = data['Brain Weight(grams)'].values

#taking mean
mean_x = np.mean(x)
mean_y = np.mean(y)

#number of data values
n = len(x)

numer = 0
denom = 0

"""
m(slope) = summation((x-mean(x))*(y-mean(y)))/summation((x-mean(x))^2)
"""
for i in range(n):
	numer += (x[i] - mean_x) * (y[i] - mean_y)
	denom += (x[i] - mean_x) ** 2

# m(slope)
b1 = numer/denom
# c (taken out by y=mx+c)
b0 = mean_y - (b1 * mean_x)

print(b1, b0)

plt.plot(x, y, color='#58b970', label='Regression Line')
plt.scatter(x, y, c='#ef5423', label='Scatter Plot')
plt.legend()
plt.show()