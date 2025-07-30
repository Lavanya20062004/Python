try:
     num1 = float(input("Enter the first number: "))
except ValueError:
    print("Invalid input: please enter a valid number.")
    exit(1)
try:
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input: please enter a valid number.")
    exit(1)
operator = input("Enter an operator (+, -, *, /, %): ").strip()
if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit(1)
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
elif operator == '%':
    if num2 == 0:
        print("Error: Modulo by zero is not allowed.")
        exit(1)
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")
else:
    print("Invalid operator. Please use one of +, -, *, /, %.")
