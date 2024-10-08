# import math
from math import sqrt

# print(math.sqrt(20))
print(sqrt(25))


# # List
#
# student_1 = "Andrey"
# student_2 = "Olga"
# student_3 = "Maksim"
#
# #              0         1        2        3     4
# students = ["Andrey", "Olga", "Maksim", "Bob", "New"]
# #              -5       -4       -3       -2     -1
# ages = [23, 21, 34, 55, 43]

#             0       1     2     3     4    ___________5__________
#                                                  0          1
# student = ["Andrey", 34, "Blue", 12.0, True, ["English", "Russian", [1,2]]]

# student = ["Andrey", 34, "Blue", 12.0, True]
#
# list_1 = [1, "we", []]
#
# print(student)
# print(len(student))
#
# student.append("Olga")
# print(student)
# print(len(student))

# if student[5][0] == "English":
#     pass

# print('3' + "5")


#
# students = ["Andrey", "Olga", "Maksim", "Bob", "New", "New2"]
#
# # for student in students:
# #     print(student)
#
# for index in range(len(students)):  # range(6)
#     print(index, students[index])
#
# print("Done")

# one = []
# print(type(one))
#
# two = list()
# print(type(two))

# answers = []

# answers.append(input("Enter First name: "))
# answers.append(input("Enter Last name: "))
# answers.append(input("Enter age: "))

# answers = [input("Enter First name: "),
#            input("Enter Last name: "),
#            input("Enter age: ")]
# print(answers)

# students = ["Andrey", "Olga", "Maksim", "Bob", "New", "New2"]
# print(students)
# students[0], students[1] = students[1], students[0]
# print(students)
# a = "Andrey"
# b = "Baykov"
#
# print(a, b)
#
# a, b = b, a
# print(a, b)

# Tuple
# full_name = ["Andrey", "Baykov", "Baykov"]
# print(full_name)
# print(type(full_name))

# full_name_tuple = ("Andrey", "Baykov")
# print(full_name_tuple[1])
# print(type(full_name_tuple))

# full_name_to_tuple = tuple(full_name)
# print(full_name_to_tuple)
# print(type(full_name_to_tuple))
#
# full_name_to_list = list(full_name_to_tuple)
# print(full_name_to_list)
# print(type(full_name_to_list))

# Set
# name_set = {"Andrey", "Baykov", "Baykov"}
# print(name_set)
# print(type(name_set))
#
# name_set.add("New")
# print(name_set)
# print(type(name_set))
#
# name_set.remove("Andrey")
# print(name_set)
# print(type(name_set))

# list_of_value = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0,
#         0, 0, 0, 0]
#
# values_to_set = set(list_of_value)
# print(values_to_set)
#
# unique_values = list(values_to_set)
# print(unique_values)
# print(type(unique_values))

# # Dictionary
# student = {
#     # key       :  value
#     'first_name': 'Andrey',
#     'last_name': 'Smith',
#     "email": 'andrey@gmail.com',
#     'age': 25,
#     0: 'new',
#     1: 'new 2'
# }
#
#
# print(student)
# print(student[0])
#
# student['first_name'] = "Bob"
# print(student)
#
# student['middle_name'] = "MC"
# print(student)
#
# print(student.keys())
#
# for key, value in student.items():
#     print(key, value)
