'''
2. Debugging Function calls
Problem: Create a decorator to print the function name and the values of it's arguments every time the function is called.
'''

def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kargs_value = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"Calling: {func.__name__} with args {args_value} and kwargs {kargs_value}")
        return func(*args,**kwargs)
    return wrapper


@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Chai",greeting="Haanji ")