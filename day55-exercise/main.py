


def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"It returned {result}")
    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)

print(a_function(1, 2, 3))
