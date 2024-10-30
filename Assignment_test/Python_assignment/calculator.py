def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero not allowed"

print("Simple calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter the corresponding choice (1/2/3/4): ")

if operation == "1":
    result = num1 + num2
    print(f"The result of addition is: {result}")

elif operation == "2":
    result = num1 - num2
    print(f"The result of subtraction is: {result}")

elif operation == "3":
    result = num1 * num2
    print(f"The result of multiplication is: {result}")

elif operation == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print(f"Error: Cannot divide by zero")

else:
    print("Invalid operation, please select 1, 2, 3 or 4")
    
