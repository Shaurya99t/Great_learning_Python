class Vehicle:
    def __init__(self,milage,cost):
        self.milage=milage
        self.cost=cost
    def show_details(self):
        print("I am a vehicle")
        print("The milage is",self.milage)
        print("The cost is ",self.cost)
v1=Vehicle(300,3000)
# v1.show_details()
class Car(Vehicle):
    def show_car_details(self):
         print("I am a car")
c1 = Car(10,74870)
c1.show_details()
c1.show_car_details()
class Car(Vehicle):
    def __init__(self, milage, cost,gear,hp):
        super().__init__(milage, cost)
        self.gear=gear
        self.hp=hp
    def show_car_details(self):
        print("I am car")
        print("Number of gears are",self.gear)
        print("Number of hourse power are",self.hp)
c1=Car(200,507967,4,200)
c1.show_car_details()