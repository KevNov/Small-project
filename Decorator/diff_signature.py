def shout(fn):
    def wrapper(*args,**kwargs):
        return fn(*args,**kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"hi ny mane is {name}"

@shout
def order(main, side):
    return f"Hi, i like the {main}, with a side of {side},please"

print(greet("noufal"))
print(order("sushi","sashimi"))