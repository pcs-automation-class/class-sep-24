
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
#     print(answer, "is greater than 7")

# if answer < 5:
#     print(answer, "is less than 5")
# if answer == 5:
#     print(answer, "is equal to 5")
# if answer <= 6:
#     print(answer, "is equal to 6")
# if answer == 7:
#     print(answer, "is equal to 7")
# else:
#     print(answer, "is greater than 7")

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
# if compare is not True:
#     print(answer)
#     if compare is True:
#         print("The answer is 5")
#
# if answer == answer:
#     print("The answer is 5")



# and
# True True = True
# True False = False
# False True = False
# False False = False

# or
# True True = True
# True False = True
# False True = True
# False False = False

# not
# False = True
# True = False
#
# if a < b and a > c or a ==5:
#     True and False
#     False or True
#     True
#     pass
#
# if a == 5 or a < b and a > c:
#     True and False
#     True or False
#     True
#     pass


# answer = int(input("Enter a number: "))

# for
# for i in range(10):
#     print(i)
#
# for char in "Python":
#     print(char)
#
# for x in range(1, answer + 1):
#     if x == 2:
#         # break
#         continue
#     print(x)


# while
# while True:
#     print(answer)
#     # answer = answer - 1
#     answer -= 1
#     if answer == 0:
#         break
#     print("in loop")

# while answer > 0:
#     print(answer)
#     answer -= 1
#     print("in loop")

# while True:
#     first = float(input("Enter first number: "))
#     second = float(input("Enter second number: "))
#     sign = input("Enter sign (+, -, *, /): ")
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
#     if input("Would you like to stop? (y/n): ").lower() == "y":
#         break
#
# print("Done")
#
#
while True:
    answer = input("\nChoose what do you want to convert? \n1 - C -> F, \n2 - F -> C, \n3 - Km -> Miles, "
                   "\n4 - Miles -> Km or \nq to exit:  ")
    if answer == "1":
        print("C -> F")
    elif answer == "2":
        print("F -> C")

    if answer == "q":
        break

# name = "Andrey"
# # print(name)
# print(f"Thank you {name} for using this program!")
