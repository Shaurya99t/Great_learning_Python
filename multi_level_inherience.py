class Parent:
    def __init__(self):
        self.name = None

    def assign_name(self, name):
        self.name = name

    def show_name(self):
        return self.name

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.age = None

    def assign_age(self, age):
        self.age = age

    def show_age(self):
        return self.age

class Grandchild(Child):
    def __init__(self):
        super().__init__()
        self.gender = None

    def assign_gender(self, gender):
        self.gender = gender

    def show_gender(self):
        return self.gender

g1 = Grandchild()
g1.assign_name("shaurya")
g1.assign_age(19)
g1.assign_gender("male")

name = g1.show_name()
age = g1.show_age()
gender = g1.show_gender()

print("Name:", name)
print("Age:", age)
print("Gender:", gender)
