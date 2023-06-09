#Give the Vehicle class a method seating_capacity() that will take capacity as an argument and 
#return the string "The seating capacity of (name of the vehicle) is (capacity)."
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