# show a non-keyword and keyworded argument in a list
'''
@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1, 2, 3,a="hi",b="bye")

# Should print (on two lines):
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}
'''

from functools import wraps

def show_args(fn):
    @wraps
    def wrapper(*args,**kwargs):
        print(f"Here's the args: {args}")
        print(f"Here's the kwargs: {kwargs}")
        return fn(args,kwargs)
    return wrapper

@show_args
def do_nothing():
    pass



do_nothing(1, 2, 3, a="hi",b="bye")

#still wasn't functioning 