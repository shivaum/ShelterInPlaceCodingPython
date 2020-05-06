num = input("Enter a number: ")
num2 = input("Enter a number: ")
noun = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
adj = input("Enter a adj: ")

res = "This is my Mad Lib: " + "Caitlyn has " + num + " " + noun + " and " + num2 + " " + adj + " " + noun2;
print(res)

res = res[20: len(res)]
print(res)

finalWord = res[-len(noun2):len(res)]
print(finalWord)