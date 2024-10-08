# -----------------------Session_6----------------------
# first_name = "Maksym"
# age = 46
# t_short_color = "green"
# shoe_size = 42.0
# is_blue_short = False
# pants_color = None

# print(first_name)
# print(age)
# print(t_short_color)
# print(shoe_size)

# print(type(first_name))
# print(type(age))
# print(type(t_short_color))
# print(type(shoe_size))
# print(type(is_blue_short))
# print(type(pants_color))

# x = "Maksym "
# y = "Kyrychok"
# c = x + y
# print(c)
# print(type(c))

# a = 10
# b = 2.5
# s = "5"
# print(type(float(a)))
# print(type(int(b)))
# print(int(b))
# print(type(str(b)))
# print(type(int(s)))

# name = input("Please enter your name: ")
# first = float(input("Please enter your first number: "))
# second = float(input("Please enter your second number: "))
# third = float(input("Please enter your third number: "))
# result = (first / second) + third
# print(name)
# print(result)


# -----------------------Lesson_7_file----------------------

# answer = int(input("Enter a number: "))

# if answer < 5:
#     print(answer, "is less than 5")
# elif answer == 5:
#     print(answer, "is equal to 5")
# elif answer == 6:
#     print(answer, "is equal to 6")
# elif answer == 7:
#     print(answer, "is equal to 7")
# else:
#     print(answer, "is greater then 7")

# if answer < 5:
#     print(answer, "is less than 5")
# if answer == 5:
#     print(answer, "is equal to 5")
# if answer <= 6:
#     print(answer, "is equal to 6")
# if answer == 7:
#     print(answer, "is equal to 7")
# else:
#     print(answer, "is greater then 7")

# if answer > 5 and answer < 8:
#     print(f"between 5 and 8")
#
# if answer == 5 or answer == 8:
#     print(f"is 5 or 8")

# a = 2
# b = 2
# c = a == b
# print(c)

# compare = answer == 5
# print(compare)
#
# if answer is not True:
#     print(answer)
#
# answer = int(input("Enter a number: "))

# for i in range(10):
#     print(i)

# for char in "Python":
#     print(char)

# for x in range(1, answer+1):
#     print(x)

# for x in range(1, answer +1):
#     if x == 2:
#         # break
#         continue
#     print(x)

# answer = int(input("Enter a number: "))

# while answer > 0:
#     print(answer)
#     answer -= 1
#     # break

# while True:
#     print(answer)
#     answer -= 1
#     if answer == 0:
#         break
#     print("in loop")

# while answer > 0:
#     print(answer)
#     answer -=1
#     print("in loop")

# -----------------Calculator------------------
# while True:
#     first = float(input("Enter first number: "))
#     second = float(input("Enter second number: "))
#     sign = input("Enter a sign (+, -, *, /): ")
#     result = 0
#
#     if sign == "+":
#         result = first + second
#     elif sign == "-":
#         result = first - second
#     elif sign == "*":
#         result = first * second
#     elif sign == "/":
#         result = first / second
#     else:
#         print("Invalid input")
#     print(result)
#
#     if input("Would you like to stop? (Y/N): ").lower() == "y":
#         break
# print("Done")
# -----------------------------------------------

# ------------------Converter--------------------
# while True:
#     answer = input(
#     "\nChoose what to convert? \n1 - C -> F, \n2 - F -> C, \n3 - Km -> Ml, \n4 - Ml -> Km \nor q to exit: ")
#     if answer == "1":
#         print("C -> F")
#     elif answer == "2":
#         print("F -> C")
#     elif answer == "3":
#         print("Km -> Ml")
#     elif answer == "4":
#         print("Ml -> Km")
#     if answer == "q":
#         break

# while True:
#     answer = input(
#         "\nChoose what to convert? \n1 - C -> F, \n2 - F -> C, \n3 - Km -> Ml, \n4 - Ml -> Km \nor q to exit: ")
#
#     # Exit the loop if 'q' is entered
#     if answer == "q":
#         break
#
#     # Celsius to Fahrenheit conversion
#     elif answer == "1":
#         celsius = float(input("Enter temperature in Celsius: "))
#         fahrenheit = (celsius * 9 / 5) + 32
#         print(f"{celsius}C is {fahrenheit}F")
#
#     # Fahrenheit to Celsius conversion
#     elif answer == "2":
#         fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#         celsius = (fahrenheit - 32) * 5 / 9
#         print(f"{fahrenheit}F is {celsius}C")
#
#     # Kilometers to Miles conversion
#     elif answer == "3":
#         kilometers = float(input("Enter distance in Kilometers: "))
#         miles = kilometers * 0.621371
#         print(f"{kilometers} Km is {miles} Miles")
#
#     # Miles to Kilometers conversion
#     elif answer == "4":
#         miles = float(input("Enter distance in Miles: "))
#         kilometers = miles * 1.60934
#         print(f"{miles} Miles is {kilometers} Km")
#
#     # If none of the above options are selected, ask again
#     else:
#         print("Invalid option, please try again.")

# --------------------------------Lesson_8_file------------------------------------------

# ----------------------list

# student_1 = 'Andrey'
# student_2 = 'Olga'
# student_3 = 'Maksym'

# students = ['Andrey', 'Olga', 'Maksym', 'Bob', 'New']

# ages = [23, 21, 44, 55, 43]

# student = ['Maksym', 36, 'Green', 12.0, True, ['English', 'Ukrainian', [1, 2]]]

# student = ['Maksym', 36, 'Green', 12.0, True]

# student.append('Olga')

# print(student)
# print(len(student))

# if student[1][0] == 'English':
#     pass

# students = ['Andrey', 'Olga', 'Maksym', 'Bob', 'New', 'New2']
# for x in students:
#     print(x)

# for index in range(len(students)):
#     print(index, students[index])

# print('Done')

# one = []
# print(type(one))

# two = list()
# print(type(two))

# answers = []
# input_1 = input('Enter First name: ')
# input_2 = input('Enter Last name: ')
# input_3 = input('Enter Age: ')
# answers.append(input_1)
# answers.append(input_2)
# answers.append(input_3)

# answers.append(input('Enter First name: '))
# answers.append(input('Enter Last name: '))
# answers.append(input('Enter Age: '))

# answers = [input('Enter First name: '),
#            input('Enter Last name: '),
#            input('Enter Age: ')]
# print(answers)

# a = 1
# b = 2
# print(a, b)
# a, b = b, a
# print(a, b)

# students = ['Andrey', 'Olga', 'Maksym', 'Bob', 'New', 'New2']
# print(students)
# students[0], students[1] = students[1], students[0]
# print(students)

# --------------------------------------Tuple

# full_name = ('Maksym', 'Kyrychok', 'Kyrychok')
# print(full_name)
# print(type(full_name))

# full_name_to_list = list(full_name)
# print(full_name_to_list)
# print(type(full_name_to_list))

# --------------------------------------Set

# name_set = {'Maksym', 'Kyrychok', 'Kyrychok'}
# print(name_set)
# print(type(name_set))

# name_set.add('New')
# print(name_set)
# print(type(name_set))

# name_set.remove('Kyrychok')
# print(name_set)
# print(type(name_set))

# list_file = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0 ,0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 4,
#                   4, 4, 4, 4, 4, 4, 4]
# list_file_to_set_file = set(list_file)
# print(list_file_to_set_file)

# unique_values = list(list_file_to_set_file)
# print(unique_values)
# print(type(unique_values))

# ---------------------------------------Dictionary

# student = {
#     'first_name:': 'Maksym',
#     'last_name:': 'Krychok',
#     'email:': 'email@email.com',
#     'age:': 36,
#     0: 'new',
#     1: 'new2'
# }
# print(student)
# print(student[0])

# student['first_name'] = 'Bob'
# print(student)

# student['middle_name:'] = 'MC'
# print(student)

# print(student.keys())

# for key in student.keys():
#     print(key)

# for key, value in student.items():
#     print(key, value)


# --------------------------------------------------func_file---------------------------------------------------

# def my_print_function(result):
#     print('**********************************')
#     print('Result is:', result)
#     print('----------------------------------')


# a = 1
# b = 2
# c = a + b
# my_print_function(c)

# c = a - b
# my_print_function(c)

# c = a * b
# my_print_function(c)

# c = a / b
# my_print_function(c)


# -----------------Calculator------------------
# while True:
#     first = float(input("Enter first number: "))
#     second = float(input("Enter second number: "))
#     sign = input("Enter a sign (+, -, *, /): ")
#     result = 0

    # if sign == "+":
    #     result = first + second
    # elif sign == "-":
    #     result = first - second
    # elif sign == "*":
    #     result = first * second
    # elif sign == "/":
    #     result = first / second
    # else:
    #     print("Invalid input")
    # print(result)

    # if input("Would you like to stop? (Y/N): ").lower() == "y":
    #     break
# print("Done")

# ----------------------------------func_calculator-----------------------------

class Calculator:

    def add(self, a, b):
        print(a + b)

    def substract(self, a, b):
        print(a - b)

    def multiply(self, a, b):
        print(a * b)

    def devide(self, a, b):
        print(a / b)


while True:
    calc = Calculator()
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operator = input("Enter operator: ")
    if operator == "+":
        calc.add(a, b)
    elif operator == "-":
        calc.substract(a, b)
    elif operator == "*":
        calc.multiply(a, b)
    elif operator == "/":
        calc.devide(a, b)
    else:
        print("Invalid operator")
    if input("Would you like to stop? (Y/N): ").lower() == "y":
        break
    print("Done")
