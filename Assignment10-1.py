#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes. (__init__)
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        print(self.max_speed,self.mileage)
a=Vehicle(120,1000)

#otherweise:
"""class vehicle:
    max_speed=0
    mileage=0"""