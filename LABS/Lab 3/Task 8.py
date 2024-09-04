try:
    n1 = int(input("Enter the first integer: "))
    n2 = int(input("Enter the second integer: "))
    div = n1 / n2
    print(f"The result of {n1} divided by {n2} is {div}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
