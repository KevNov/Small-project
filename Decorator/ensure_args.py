from functools import wraps

def ensure_No_kwargs(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed!!")
        return fn(*args,**kwargs)
    return wrapper

@ensure_No_kwargs
def greet(name):
    print(f"hello there, my name is {name}")

greet(name="adam")