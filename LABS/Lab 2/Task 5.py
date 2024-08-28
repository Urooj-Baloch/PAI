def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact
try:
    n = int(input("Enter a number to find its factorial: "))
    print("Factorial of ",n," is :", factorial(n))
except ValueError:
    print("Please enter a valid integer.")
