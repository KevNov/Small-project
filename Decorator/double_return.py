# write a function that double the result 

def double_return(fn):
    def wrapper(*args,**kwargs):
        result = fn(*args,**kwargs)
        return [result,result]
    return wrapper

@double_return 
def add(x, y):
    return x + y

@double_return
def greet(name):
    return f"Hello, my name is {name}"

print(add(3, 7))
print(greet("kevin"))
