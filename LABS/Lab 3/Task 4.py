try:
    name = input("Enter employee name: ")
    cnic = input("Enter employee CNIC number: ")
    age = input("Enter employee age: ")
    salary = input("Enter employee salary: ")
    if not name or not cnic or not age.isdigit() or not salary.replace('.', '', 1).isdigit():
        raise ValueError("Invalid input. Please make sure all fields are correctly filled.")
    with open('employee_biodata.txt', 'w') as file:
        file.write(f"Name: {name}\n")
        file.write(f"CNIC Number: {cnic}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Salary: {salary}\n")
    contact_number = input("Enter employee contact number: ")
    with open('employee_biodata.txt', 'a') as file:
        file.write(f"Contact Number: {contact_number}\n")
        print("Bio_data added successfully.")
    with open('employee_biodata.txt', 'r') as file:
        content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
except ValueError as e:
    print(f"Error: {e}")
except IOError:
    print("Error: An I/O error occurred while handling the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
