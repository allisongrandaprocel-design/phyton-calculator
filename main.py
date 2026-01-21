def show_menu():
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

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
        return "Error: division by zero is not allowed"

print("Python Calculator")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

show_menu()
option = input("Option: ")

if option == "1":
    print("Result:", add(num1, num2))
elif option == "2":
    print("Result:", subtract(num1, num2))
elif option == "3":
    print("Result:", multiply(num1, num2))
elif option == "4":
    print("Result:", divide(num1, num2))
else:
    print("Invalid option")



