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
print("What to convert?")
print("1. °F to °C")
print("2. °C to °F")
print("3. mi to km")
print("4. km to mi")
choice = int(input("Enter your choice: "))
print("-" * 20)
n = result = 0

match choice:
    case 1:
        n = float(input("Enter your °F: "))
        result = round(((n - 32) * 5 / 9), 1)
        print(f"{n}°F is equal to {result}°C")

    case 2:
        n = float(input("Enter your °C: "))
        result = round((n * 9 / 5 + 32), 1)
        print(f"{n}°C is equal to {result}°F")

    case 3:
        n = float(input("Enter your mi: "))
        result = round(n * 1.60934, 2)
        print(f"{n}mi is equal to {result}km")

    case 4:
        n = float(input("Enter your km: "))
        result = round(n / 1.60934, 2)
        print(f"{n}km is equal to {result}mi")

    case _:
        print("Enter a number from 1 to 4")