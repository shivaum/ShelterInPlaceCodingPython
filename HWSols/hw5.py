def sum_digits(n):
	if n < 10:
		return n
	return sum_digits(n // 10) + (n % 10)

print(sum_digits(123))

def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total
print( recursive_list_sum([1, 2, [3,4],[5,6]]))