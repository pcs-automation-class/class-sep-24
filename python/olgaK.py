# calculator
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Enter the operation (+, -, *, /): ")
#
# match operation:
#     case "+":
#         print(num1 + num2)
#     case "-":
#         print(num1 - num2)
#     case "*":
#         print(num1 * num2)
#     case "/":
#         print(num1 / num2)
#     case _:
#         print("Try again.")

#converter
# print("What to convert?")
# print("1. °F to °C")
# print("2. °C to °F")
# print("3. mi to km")
# print("4. km to mi")
# choice = int(input("Enter your choice: "))
# print("-" * 20)
# n = result = 0
#
# match choice:
#     case 1:
#         n = float(input("Enter your °F: "))
#         result = round(((n - 32) * 5 / 9), 1)
#         print(f"{n}°F is equal to {result}°C")
#
#     case 2:
#         n = float(input("Enter your °C: "))
#         result = round((n * 9 / 5 + 32), 1)
#         print(f"{n}°C is equal to {result}°F")
#
#     case 3:
#         n = float(input("Enter your mi: "))
#         result = round(n * 1.60934, 2)
#         print(f"{n}mi is equal to {result}km")
#
#     case 4:
#         n = float(input("Enter your km: "))
#         result = round(n / 1.60934, 2)
#         print(f"{n}km is equal to {result}mi")
#
#     case _:
#         print("Enter a number from 1 to 4")

# grade analyzer

# input of grades
def input_grades(num_students):
    grades = []
    for i in range(num_students):
        grade = float(input(f"Enter grade for student {i + 1}: "))
        grades.append(grade)
    return grades


# find the highest grade
def find_highest_grade(grades):
    return max(grades)


# find the lowest grade
def find_lowest_grade(grades):
    return min(grades)


# find the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)


num_students = 5
grades = input_grades(num_students)

highest = find_highest_grade(grades)
lowest = find_lowest_grade(grades)
average = calculate_average(grades)

print(f"\nHighest grade: {highest}")
print(f"Lowest grade: {lowest}")
print(f"Average grade: {average}")




