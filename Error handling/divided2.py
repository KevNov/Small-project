# handling error in divided function

def divided(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("dont divided by zero!!")
    except TypeError:
        print("only type a number, dont used a alphabet or string")
    else:
        print(f"the result of {a} divided by {b} is {result}")

print(divided(5,0))
print(divided("a", 8))
print(divided(15,40))
