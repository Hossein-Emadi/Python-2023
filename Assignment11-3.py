"""Write a Python function called calculate_average that accepts a variable number of arguments
(numbers) and returns the average of those numbers. Test the function with different sets of 
numbers."""

def calculate_average(*args):
    i =0
    sum =0
    for j in args:
        i+=1
        sum+=j
    return sum/i
print(calculate_average(1,4,5,10,25,81))