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
#     answer = input("\nChoose what to convert? \n1 - C -> F, \n2 - F -> C, \n3 - Km -> Ml, \n4 - Ml -> Km \nor q to exit: ")
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





































