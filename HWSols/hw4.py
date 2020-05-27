# Write a Python function named max 
# that takes in two numbers and 
#returns the larger number out of the two 
def max(a, b):
	if (a >= b):
		return a
	else:
		return b

my_num = max(7, 28)
print(my_num)

# def min(a,b):
# 	if (a <= b):
# 		return a
# 	else:
# 		return b

# Write a Python function named product 
# that takes in an array of numbers and 
# returns the total product of all the numbers

def product(arr):
	total = 1
	for num in arr:
		total *= num
	return total

result = product([3, 2, 2])
print(result)

# Write a Python function named even_nums 
# that takes an array of numbers and 
# returns an array that only contains the even numbers from that original array

def even_nums(arr):
	return_arr = []
	for num in arr:
		if num % 2 == 0:
			return_arr.append(num)
	return return_arr

result = even_nums([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(result)

