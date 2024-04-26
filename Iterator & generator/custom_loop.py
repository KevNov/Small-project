#custom for loop

def my_for(iterable,func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            print("END OF THE LOOP")
            break
        else:
            func(thing)

def multiply(x):
    print(x*3)

my_for("lmao", print)
my_for([1,2,3,4,5], multiply)
