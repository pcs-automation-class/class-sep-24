# CLASS 6
import random


# name = input("What is your name?")
# surname = input("What is your surname?")
# town = input("Where do you live?")
# period = input("How long have you liver here?")
# print("Hello, " + name + " " + surname + "! You`ve lived in " + town + " for " + period + " years. ")

# a1 = int(input("Please enter first number"))
# a2 = int(input("Please enter second number"))
# sum = a1 + a2
# dif = a1 - a2
# mult = a1 * a2
# div = a1 / a2
# print("Summary: " + str(sum) + "\n" + "Difference: " + str(dif)+ "\n" + "Multiplication: " + str(mult)+ "\n" + "Division: "+ str(div))

# first_digit = float(input("Please enter a digit"))
# second_digit = float(input("Please enter another digit"))
# digits_div = first_digit / second_digit
# round_div = round(digits_div, 3)
# print(round_div)

# one = int(input("Enter a number: "))
# two = int(input("Enter one more number: "))
# print(one > two)

# one = float(input("Enter a number: "))
# two = float(input("Enter one more number: "))
# print(one == two)

# print("Let`s calculate the discriminant together!")
# b = int(input("Enter b"))
# a = int(input("Enter a"))
# c = int(input("Enter c"))
# D = b*b - 4*a*c
# print("The discriminant is", D)

# More math
#1
# a = 8
# b = 6
# c = (a+b)*(a-b)
# d = a*a-b*b
# print(c==d)

#2
# e = a**3 +b**3
# f = (a+b)*(a**2 - a*b + b**2)
# print(e==f)

#3
# print(a%2)
# print(a%3)
# print(a%1)
# print(a%8)
# print(abs(-a))

#4
#print(-(a/2+a*b)<0)
# print(abs(-(a/2+a*b))<0/b)

# CLASS 7

# new = range(-11,11)
# for i in new:
#     if i <= -1:
#         print(abs(i))
#     else:
#         i +=10
#         print(i)

# while True:
#     actual_mood = input("Is your mood good? Beware it's yes/no question\n").lower()
#     if actual_mood == "yes":
#         print("Great, thanks for the answer")
#     elif actual_mood == "no":
#         print("Don't be sad, there's more to come")
#     else:
#         print("Be careful when you type your answer")
#     if input("Would you like to try again? (yes/no): ").lower() == "no":
#         break
# print(":(")

# month_number = int(input("Enter the month number when you were born\n"))
# if month_number == 1 or month_number == 2 or month_number == 12:
#     print("You were born in winter")
# elif month_number == 3 or month_number == 4 or month_number == 5:
#     print("You were born in spring")
# elif month_number == 6 or month_number == 7 or month_number == 8:
#     print("You were born in summer")
# elif month_number == 9 or month_number == 10 or month_number == 11:
#     print("You were born in fall")
# else:
#     print("Please enter a number from 1 to 12")

# Calculator
#
# while True:
#     number_one = float(input("Enter first number: "))
#     number_two = float(input("Enter second number: "))
#     to_do = input("Enter sign (+, -, *, /): ")
#     result = 0
#
#     if to_do == "+":
#         result = number_one + number_two
#     elif to_do == "-":
#         result = number_one - number_two
#     elif to_do == "*":
#         result = number_one * number_two
#     elif to_do == "/":
#         if number_two == 0:
#             print("Can't divide by zero")
#         else:
#             result = number_one / number_two
#     else:
#         print("input must be a number or digit")
#
#     if result % 2 == 0:
#         print(f"{result} is even")
#     else:
#         print(f"{result} is odd")
#
#     if input("Would you like to stop? (yes/no): ").lower() == "yes":
#         break
#
# print("Calculation result is " + str(result))


#Converter

# while True:
#     option = input("\nWhat would you like to convert? \n1: m/s --> km/h, \n2: km/h --> m/s, \n3: C --> F, "
#                    "\n4: F --> C, \nq to exit \n")
#     if option == "1":
#         m = float(input("How many meters per second?"))
#         result = m * 3.6
#         print(f"{m} m/s equals {result} km/h")
#
#     elif option == "2" :
#         km = float(input("How many kilometers per hour?"))
#         result = round(km * 1000/3600, 2)
#         print(f"{km} m/s equals {result} m/s")
#
#     elif option == "3" :
#         C = float(input("How many degrees Celsius?"))
#         result = C * 1.8 + 32
#         print(f"{C} degrees Celsius equals {result} degrees Fahrenheit")
#
#     elif option == "4" :
#         F = float(input("How many degrees Fahrenheit?"))
#         result = (F - 32)/1.8
#         print(f"{F} degrees Fahrenheit equals {result} degrees Celsius")
#
#     else:
#         print("Please choose one option")
#
#     if option == "q":
#         break

# Updated calculator

# def calculator(a,b, sign):
#     if sign == "+":
#         res = a+b
#     elif sign == "-":
#         res = a-b
#     elif sign == "*":
#         res = a*b
#     elif sign == "/":
#         res = a/b
#     else:
#          return "Input must be a number or digit"
#     return f"The result of calculation is {res}"
# result = calculator(1, 2, "+")
# print(result)

#Guess the number

# def guess_the_number():
#     riddle = random.randint(0, 9)
#     guessed_numbers = []
#     while True:
#         try:
#             attempt = int(input("Please enter a number between 0 and 9: "))
#             guessed_numbers.append(attempt)
#             if attempt < riddle:
#                 print("Need more")
#             elif attempt > riddle:
#                 print("Need less")
#             else:
#                 number_of_attempts = len(guessed_numbers)
#                 print(f"Congratulations! You guessed the number {attempt} after {number_of_attempts} attempts")
#                 break
#         except ValueError:
#             print("It should be a digit")
#
# guess_the_number()


# Min & Max etc

# many = 10
# numbers = []
# for i in range(many):
#     numbers.append(random.randint(1, 99))
#     minimum = min(numbers)
#     maximum = max(numbers)
# print(numbers)
# print(minimum)
# print(maximum)
# print(sum(numbers))
# print(sorted(numbers))

# Duplicate
# list = [1,1,1,2,3,4,5,6,7,7,7,7,7,70]
# print(set(list))


# Much
# words = ["Anna", "Dudnikova", "22", "IT", "the Earth"]
# print(random.choice(words))
# print(sorted(words))
# for index in range(len(words)):
#     print(index, words[index])

# words = ["Anna", "Dudnikova", 22, "22", "IT", "the Earth", [1, "2", 2, 3, "Day", 4, 4, "Night"]]
# random_word = random.choice(words)
#
# if isinstance(random_word, int):
#     rand = str(random_word)
#     print(f"Correct! {rand} is an integer")
# else:
#     print("Nope " + str(random_word) + " is a string")



# More
# list = ["Anna", "Anna", "Dudnikova", 15, "22", "IT", "the Earth", "another 1", 5, 15]
# print(set(list))
#
# for item in list:
#     new = set(item)
#     print(type(item))
#     break
# print((reversed(list)))
# print(set(reversed(list)))

#Dictionary

info = {'day': 'Sunday', 'year': 2024, 'city': 'San Francisco',
        'currency': 'dollar', 'weather': 'windy', 1: 0, 2: True, 0: "False",
        'more': ["a", "B", 123]}
# print(info)
# print(info['city'])
# print(info['year'])
# print(info[1])
# print(info[2])
# print(info[0])
# print(info['more'])
# print(info['more'][0])
# print(info.keys())
info.update({'month': 'October'})
print(info)














