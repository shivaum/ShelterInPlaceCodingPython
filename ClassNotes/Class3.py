"""print("hello world!")
x = 1
s = "This is a string."

new_str = s[10:16]
print(new_str)

s += " another string"
print(s)"""

# x = int(input("Please enter an integer: "))
# # x += 2
# # x = x + 2
# if x < 0:
# 	print("the value is less than 0")
# elif x == 0:
# 	print("x is 0")
# elif x >= 1:
# 	print("x greater than or equal to 1")
# else:
# 	print("above 1")

# s = input("here is a word: ")
# if s > "banana":
# 	print("cat is greater than banana")


arr = [1, 2, 3, 4, 5]
# # print(arr)
# # print(arr[2:5])
# print(len(arr))

# for i in arr:
# 	print(i)

# x = 1
# for i in range(1,5):
# 	x += 1
# 	print(x)

# words = ["cat", "dog", "bird"]
# for word in words:
# 	print(word)

# print(words[0])
# print(words[1])
# print(words[2])

# 0 + 1 + 2 + 3
# print(sum(arr))

# arr = list(range(1, 100, 10))
# print(arr)

# determine if n is a prime number
n = int(input("input a number: "))
temp = False
for x in range(2, n):
	if (n % x == 0):
		print(n, 'equals', x, '*', n//x)
		temp = True
		break
if (temp == False):
	print(str(n) + " is a prime number")






