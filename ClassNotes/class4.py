# n = int(input("input a number: "))
# temp = False
# for x in range(2, n):
# 	if (n % x == 0):
# 		print(n, 'equals', x, '*', n//x)
# 		temp = True
# 		break
# if (temp == False):
# 	print(str(n) + " is a prime number")

def prime(n):
	for x in range(2,n):
		if (n % x == 0):
			print(n, 'equals', x, '*', n//x)
			return False
	return True

# if prime(n):
# 	print(str(n) + " is a prime number")
# print(prime(n))

# 'hi', 2 -> 'hihi'
# def string_times(temp, n):
# 	s = ""
# 	for i in range(n):
# 		s += temp
# 	return s

# print(string_times("hi", 5))
# print(string_times("add", 4))

# arr = [100, 2, 3, 4, 20]
# if 20 in arr:
# 	print("20 is in the array")

# arr.extend([2, 5])
# arr.remove(20)
# arr.sort()
# arr.insert(2, 50)
# print(arr)
# print(min(arr))

# [1,2,3]
# [1,1,2,3,1] -> True
# def array123(nums):
# 	for i in range(len(nums) - 2):
# 		if (nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3):
# 			return True
# 	return False
# print(array123([1,1, 2, 2]))

# coord = [[1, "hi"], [2, "hello"], [4, 5]]
# #loop thru 2d array
# for s in coord:
# 	print(str(s[0]) + " , " + str(s[1]))

# #singular value from 2d array
# print(coord[0][1])

def foo(x = 10):
	print(x)
	bar(11, x)
	return x + 1

def bar(y, x):
	print(x - y)

# bar(foo(111), 11)
# bar(11, 11)
# foo()

z = foo
# print(z(111))

# fib
#n = 0 1 2 3 4 5 6 7
#    0 1 1 2 3 5 8 13
def fib(n):
	# base case
	if n <= 1:
		return n
	#recursive call
	return fib(n- 1) + fib(n - 2)
# fib(10)
print(fib(4))
# fib(3) +                     fib(2)
# fib(2) +          fib(1)     + fib(1) + fib(0)
# fib(1) + fib(0) + 1          + 1       + 0
# 1 +      0  +      1         + 1       + 0
# 3




















