"""Create a class called Rectangle with attributes width and height. Implement the
__str__() and __eq__() special methods for the Rectangle class. Test the string
representation and equality comparison of Rectangle objects."""
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}"
    def __eq__(self, other):
        if type(self) is type(other):
            return self.width == other.width and self.height == other.height
        return False
        
rectangle1 = Rectangle(3, 4)
rectangle2 = Rectangle(3, 5)
rectangle3 = Rectangle(3, 4)

print(rectangle1)
print(rectangle1 == rectangle2) 
print(rectangle1 == rectangle3)

        


    
