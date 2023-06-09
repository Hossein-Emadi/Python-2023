"""Create a closure function called calculator that performs basic arithmetic operations. The closure
should return a function that takes two numbers and performs a specified operation on them."""
def calculator():
    def operate(x,y,o):
        if o=="+":
            return x+y
        elif o=="-":
            return x-y
        elif o=="*":
           return x*y
        elif o=="/":
            return x/y
    return operate
closure=calculator()
print(closure(6,3,"/"))

        


    
