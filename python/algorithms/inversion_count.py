###################################################################################
#simple_method: Time Complexity - O(n^2)
def simple_method(a, n):
	count = 0
	for i in range(n-1):
		for j in range(i+1, n):
			if a[i]>a[j]:
				count += 1
	return count

###################################################################################
#divide_and_conquer_method: Time Complexity - O(nLog(n))
def merge(a, temp_arr, left, mid, right):
	inv_count = 0
	i = left
	j = mid+1
	k = left

	while i<=mid and j<=right:
		if a[i]<=a[j]:
			temp_arr[k] = a[i]
			i += 1
			k += 1
		else:
			temp_arr[k] = a[j]
			inv_count += (mid-i+1)
			j += 1
			k += 1

	while i<=mid:
		temp_arr[k] = a[i]
		i += 1
		k += 1

	while j<=right:
		temp_arr[k] = a[j]
		j += 1
		k += 1

	for i in range(left, right+1):
		a[i] = temp_arr[i]

	return inv_count

def merge_sort(a, temp_arr, left, right):
	inv_count = 0
	if left<right:
		mid = (left+right)//2
		left_inv = merge_sort(a, temp_arr, left, mid)
		right_inv = merge_sort(a, temp_arr, mid+1, right)
		merge_inv = merge(a, temp_arr, left, mid, right)
		inv_count = left_inv+right_inv+merge_inv
	return inv_count

def divide_and_conquer_method(a, n):
	temp_arr = [0 for i in range(n)]
	return merge_sort(a, temp_arr, 0 ,n-1)

###################################################################################

a = [1, 20, 6, 4, 5]
n = len(a)
ans1 = simple_method(a, n)
ans2 = divide_and_conquer_method(a, n)
print("No. of inversions in the array(simple method): ", ans1)
print("No. of inversions in the array(divide & conquer): ", ans2)