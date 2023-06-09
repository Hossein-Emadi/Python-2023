#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__ ( self,name , max_speed , mileage ):
        self.name=name
        self.max_speed = max_speed
        self.mileage = mileage
    def seating_capacity(self,capacity):
       return"The seating capacity of " + str(self.name) +" is " +str(capacity)+ " person."
a=Vehicle("Porsche",200,500)
print(a.name,a.max_speed,a.mileage)
print(a.seating_capacity(4))
print("_____________________")
class Bus(Vehicle):
    """def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed = max_speed
        self.mileage = mileage"""
    """def seating_capacity(self, capacity):
        return"The seating capacity of " + str(self.name) +" is " +str(capacity)+ " person." """
b=Bus("Volvo",100,1000)
print(b.name,b.max_speed,b.mileage)
print(b.seating_capacity(40))