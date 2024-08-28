def employee(name, sal=10000):
    tax = sal * 0.02
    after_tax = sal - tax
    print(f"Employee Name: ",name)
    print(f"Salary after tax: ",after_tax)


employee("Urooj Baloch")
employee("Mahnoor Hussain", 15000)  
