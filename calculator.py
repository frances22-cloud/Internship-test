
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Division by zero is not allowed."
    else:
        return num1 / num2

print("Simple Calculator")
print("Operations: + (add), - (subtract), * (multiply), / (divide)\n")

choice = input("Enter operation (+, -, *, /): ")

if choice not in ['+', '-', '*', '/']:
    print("Invalid operation!")
else:
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number! Please enter numeric values.")
    else:
        if choice == '+':
            print(f"Result: {first_number} + {second_number} = {add(first_number, second_number)}")
        
        elif choice == '-':
            print(f"Result: {first_number} - {second_number} = {subtract(first_number, second_number)}")
        
        elif choice == '*':
            print(f"Result: {first_number} * {second_number} = {multiply(first_number, second_number)}")
        
        elif choice == '/':
            result = divide(first_number, second_number)
            print(f"Result: {first_number} / {second_number} = {result}")