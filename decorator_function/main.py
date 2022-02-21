import time



def decorator_function(function):
    def wrapper_function():
        current_time = time.time()
        function()
        print(f"{function.__name__} took {time.time() - current_time:.4f} seconds to run.")
    return wrapper_function

@decorator_function
def speed_calc_decorator():
    pass

@decorator_function
def fast_function():
    for i in range(10000000):
        i * i

@decorator_function
def slow_function():
    for i in range(100000000):
        i * i

speed_calc_decorator()
fast_function()
slow_function()