#Write the method seating_capacity() again with capacity as its argument in the Bus class, 
#and using the keyword super() and the inherited method, return the same string, 
#but set the default capacity to 50.Hint: The mystery_function below has a default value of x
#set to 5.
"""def mystery_function(x = 5):
         return x
mystery_function() -> Output: 5
mystery_function(10) -> Output: 10"""

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
    color="white"
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)
b=Bus("Volvo",100,1000)
print(b.name,b.max_speed,b.mileage,b.color)
print(b.seating_capacity())