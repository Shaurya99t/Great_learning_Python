class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        
    def show_details(self):
        print("The name of Employee is ", self.name)
        print("The age of Employee is ", self.age)
        print("The salary of Employee is ", self.salary)
        print("The gender of Employee is ", self.gender) 
             
n=str(input("Enter the Employee"))
e1 = Employee("shaurya", 22, 122223, "male")
e1.show_details()
e2 = Employee("pranjal", 21, 128923, "male")
e2.show_details()
e3 = Employee("suraj", 28, 158923, "male")
e3.show_details()
e4 = Employee("ram", 20, 328923, "male")
e4.show_details()
e5 = Employee("sunita", 21, 120923, "female")
e5.show_details()
e6 = Employee("mahima", 20, 100903, "female")
e6.show_details()
e7 = Employee("pushpa", 25, 121923, "male")
e7.show_details()