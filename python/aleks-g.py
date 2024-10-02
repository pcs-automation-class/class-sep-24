#simple calculator with operations

a = float(input("Please enter a value: "))
b = float(input("Please enter b value: "))
operation = input("Please enter operation type (+ , - , *, /): ")


def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"


result = calculator(a, b, operation)

print("Answer is: ", result)
