class Employee:
    def __init__(self):
        self.name = ""
        self.salary = 0.0
        self.tax_percentage = 2.0  # Default tax percentage

    def get_data(self):
        self.name = input("Enter employee name: ")
        self.salary = float(input("Enter monthly salary: "))
        self.tax_percentage = float(input("Enter tax percentage: "))

    def salary_after_tax(self):

        tax_amount = (self.tax_percentage / 100) * self.salary
        remaining_salary = self.salary - tax_amount
        return remaining_salary
    def update_tax_percentage(self,new_tax_percentage):
        self.tax_percentage = new_tax_percentage
        print("Tax percentage updated to",self.tax_percentage,"%")
employee = Employee()
employee.get_data()
print("Salary after tax:",employee.salary_after_tax())
new_tax = float(input("Enter new tax percentage: "))
employee.update_tax_percentage(new_tax)

print("Salary after new tax percentage:",employee.salary_after_tax())
