# metadata example

from functools import wraps
# wraps preserved a function's metadata
# when it is 

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"You're about to called {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args,**kwargs)
    return wrapper

@log_function_data
def add(x,y):
    """Adds two number together"""
    return x + y;

#print(add(10,30))

print(add.__doc__)
print(add.__name__)
help(add)

