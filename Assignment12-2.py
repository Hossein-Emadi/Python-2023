"""Write a decorator function called timer that measures the execution time of a function and prints the
elapsed time. Apply the timer decorator to a function of your choice and test its functionality."""
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
        return result
    return wrapper

@timer
def my_function():
    # Function code goes here
    time.sleep(2)  # Simulating some time-consuming task

my_function()

        


    
