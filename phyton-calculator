# CALCULATOR IN PYTHON
def calculator():
    print("CALCULATOR IN PYTHON")
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid Numbers.")
        return #Exit the function if there is an error

    print("Select an operation: ")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    
    opcion = input("Option: ")

    if opcion == "1":
        print("RESULT: ", a + b)
    elif opcion == "2":
        print("RESULT: ", a - b)    
    elif opcion == "3":
        print("RESULT: ", a * b)
    elif opcion == "4":
        if b != 0:
            print("RESULT: ", a / b)
        else:
            print("You cannot divide by 0.")
    else:
        print("Invalid option.")

#This calls the function and executes everything above.
if __name__ == "__main__":
    calculator()
    



