from tabulate import tabulate

class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def get_details(self):
        return [self.name, self.age, self.salary, self.gender]

# Create an empty list to store employees
employees = []

while True:
    name = input("Enter the name of the employee (or 'q' to quit): ")
    
    if name.lower() == 'q':
        break

    age = int(input("Enter the age of the employee: "))
    salary = float(input("Enter the salary of the employee: "))
    gender = input("Enter the gender of the employee: ")

    # Create an Employee object and add it to the list
    employee = Employee(name, age, salary, gender)
    employees.append(employee)

# Display employee details in a table
if employees:
    headers = ["Name", "Age", "Salary", "Gender"]
    data = [employee.get_details() for employee in employees]
    table = tabulate(data, headers, tablefmt="grid")
    print(table)
else:
    print("No employee records to display.")
