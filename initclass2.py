class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def show_details(self):
        print("The name of Employee is ", self.name)
        print("The age of Employee is ", self.age)
        print("The salary of Employee is ", self.salary)
        print("The gender of Employee is ", self.gender)

e3 = Employee("shaurya", 22, 122223, "male")
e3.show_details() 