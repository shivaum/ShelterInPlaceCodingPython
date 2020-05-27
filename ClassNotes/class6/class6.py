# and - hello - FALSE
# and - sand - TRUE

def is_substring(str1, str2):
	if str1 in str2:
		return True
	return False

print(is_substring("and", "sand"))

# dictionary
# key: value
# string: int
# int: string
# float: list

dictionary = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1995
}

print(dictionary)
print(dictionary["year"])
print(dictionary.get("brand"))

dictionary["year"] = 2020

print(dictionary)

for key in dictionary:
	print(dictionary[key])

for value in dictionary.values():
	print(value)

for key, value in dictionary.items():
	print(key, value)

students = ["Bob", "Jill", "Joe", "Sue"]
grades = [85, 98, 75, 91]

def create_dictionary(list1, list2):
	my_dict = {}
	for student, grade in zip(list1, list2):
		# print(student)
		# print(grade)
		my_dict[student] = grade
	return my_dict

student_dict = create_dictionary(students, grades)
print(student_dict)

# find student with highest grade
def highest_grade(student_dict):
	max_grade = 0
	max_student = ""
	for student, grade in student_dict.items():
		if (grade > max_grade):
			max_grade = grade
			max_student = student
	print(max_student, "had the highest grade with a", max_grade)

highest_grade(student_dict)

# Bob - 85
# max_grade = 85
# max_student = "Bob"

# Jill - 98
# max_grade = 98
# max_student = "Jill"

# Joe - 75
# max_grade = 98
# max_student = "Jill"
