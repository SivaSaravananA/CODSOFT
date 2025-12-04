# Simple Calculator Program
# CODSOFT Internship - Task 1
# Author: Siva Saravanan

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


print("----- Simple Calculator -----")
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    result = add(num1, num2)
    print(f"Result: {result}")

elif choice == "2":
    result = subtract(num1, num2)
    print(f"Result: {result}")

elif choice == "3":
    result = multiply(num1, num2)
    print(f"Result: {result}")

elif choice == "4":
    result = divide(num1, num2)
    print(f"Result: {result}")

else:
    print("Invalid choice. Please select between 1 and 4.")
