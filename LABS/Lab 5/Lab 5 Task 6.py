class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def calculate_bonus(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def display_info(self):
        return f"Name: {self._name}, Salary: ${self._salary:.2f}"


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self._salary * 0.20

    def hire(self):
        return f"{self._name} is hiring a new team member."


class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self._salary * 0.10

    def write_code(self):
        return f"{self._name} is writing code."


class SeniorManager(Manager):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self._salary * 0.30


def print_employee_details(employee):
    print(employee.display_info())
    print(f"Bonus: ${employee.calculate_bonus():.2f}")
    if isinstance(employee, Manager):
        print(employee.hire())
    if isinstance(employee, Developer):
        print(employee.write_code())
    print("-" * 30)
if __name__ == "__main__":
   
    employees = [
        Manager("Urooj Baloch", 100000),
        Developer("Mahnoor Hussain", 90000),
        SeniorManager("Rabia", 200000)
    ]
    for employee in employees:
        print_employee_details(employee)
