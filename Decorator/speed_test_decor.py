# Let's defined a speed_test decorator
from time import time
from functools import wraps

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start_time = time()
        result = fn(*args,**kwargs)
        end_time = time()
        print(f"Time elapsed: {end_time - start_time}")
        return result
    return wrapper

@speed_test
def sum_num_gen():
    return sum(x for x in range(10000000))

@speed_test
def sum_num_lst():
    return sum([x for x in range(10000000)])


print(sum_num_gen())
print(sum_num_lst())



