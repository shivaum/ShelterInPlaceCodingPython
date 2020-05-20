# n = 0 1 2 3 4 5 6 7
#     0 1 1 2 3 5 8 13

def fib(n):
	if n <= 1:
		return n
	return fib(n - 1) + fib(n - 2)

# fib(3) n = 3
# fib(2) 			+ fib(1)
# fib(1) + fib(0)   + 1
# 1     +    0      + 1
# 2

# 4! - 4 * 3 * 2 * 1 = 24
# 7! - 7 * 6 * 5 * 4 * 3 * 2 * 1

# n = 4
# range(1, 5)
# 1 2 3 4
# product = 1

# 1st 
# product *= 1 - product = 1

# 2nd
# product *= 2 - product = 2

# 3rd
# product *= 3 - product = 6

# 4th
# product *= 4 - product = 24

def factorial(n):
	product = 1
	for num in range(1, n+1):
		product *= num
	return product

# print(factorial(15))

def factorialRec(n):
	#base case
	if n == 1:
		return n
	else:
		return n * factorialRec(n - 1)

# fR(4)
# 4 * fR(3)
#      3 * fR(2)
#           2 * fR(1)
# 			     1
# 4 * 3 * 2 * 1

# num = int(input("Enter a number: "))
# if num < 0:
# 	print("Cannot find factorial on a negative number")
# elif num == 0:
# 	print("Factorial of 0 is 1")
# else:
# 	print("Factorial of", num, "is", factorialRec(num))

# given two strings, return a string in the form
# shortlongshort
# example combine("a", "bbb") -> abbba
# "hello", "hi" -> hihellohi

def combine(str1, str2):
	length1 = len(str1)
	length2 = len(str2)
	if (length1 > length2):
		return str2 + str1 + str2
	elif (length1 == length2):
		return str1 + str2
	else:
		return str1 + str2 + str1

# print(combine("hi", "ab"))


# hello -> 5
# hi -> 2

def length(str1):
	count = 0
	for letter in str1:
		count += 1
	return count

# swap first three characters of both strings
# return both strings with space between them
# str1 = "abcde"
# str2 = "xyz123"
# xyzde abc123

# a b c
# 0 1 2

# print(str1[:2])
# print(str1[2:])

# str1 = abc
# str2 = xyz

# new_str1 = xy + c
# new_str2 = ab + z

def mix_up(str1, str2):
	new_str1 = str2[:3] + str1[3:]
	new_str2 = str1[:3] + str2[3:]

	return new_str1 + " " + new_str2

# print(mix_up("abcde", "xyz123"))

# The sum of the squares of the first ten natural numbers is,

# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,

# (1+2+...+10)2=552=3025

# Hence the difference between the sum of the squares 
# of the first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum 
# of the squares of the first one hundred natural numbers and the square of the sum.

def euler6():
	sum_of_squares = 0
	square_of_sum = 0
	for num in range(1, 101):
		sum_of_squares += num ** 2
		square_of_sum += num
	square_of_sum = square_of_sum ** 2
	print (sum_of_squares)
	print(square_of_sum)
	return (square_of_sum - sum_of_squares)

print(euler6())



