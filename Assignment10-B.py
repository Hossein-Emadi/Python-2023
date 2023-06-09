#Using another class variable to count the number of buses and an "if" condition,
#set the color of all Buses to red when at least 5 of them are created.

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
    numberOfBus = 0
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color="white"
        Bus.numberOfBus += 1
        print(f"The number of Bus is now {Bus.numberOfBus}")
        if Bus.numberOfBus>5:
            self.color="red"
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)
b=Bus("Volvo",100,1000)
print(b.name,b.max_speed,b.mileage,b.color)
print(b.seating_capacity())
print("_____________________")
c=Bus("Iveco",80,800)
print(c.name,c.max_speed,c.mileage,c.color)
print(c.seating_capacity(40))
print("_____________________")
d=Bus("Man",90,900)
print(d.name,d.max_speed,d.mileage,d.color)
print(d.seating_capacity(45))
print("_____________________")
e=Bus("Benz",120,2000)
print(e.name,e.max_speed,e.mileage,e.color)
print(e.seating_capacity(55))
print("_____________________")
f=Bus("BMW",115,1500)
print(f.name,f.max_speed,f.mileage,f.color)
print(f.seating_capacity(53))
print("_____________________")
g=Bus("Tesla",125,2500)
print(g.name,g.max_speed,g.mileage,g.color)
print(g.seating_capacity(58))
print("_____________________")
h=Bus("Super",135,3500)
print(h.name,h.max_speed,h.mileage,h.color)
print(h.seating_capacity(60))