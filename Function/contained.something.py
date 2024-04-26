# check if this list contain a value that u want

def contain_value(*args):
    if "Bloodborne" in args and "kevin" in args:
        return "Kevin loves to play bloodborne"
    return "he never played any game"

print(contain_value(1,"blue",False,"meh"))
print(contain_value("kevin", True, 33, "Bloodborne"))
