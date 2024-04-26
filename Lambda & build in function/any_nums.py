# create a function where it can detect any numbers

def any_number(data):
    return any(type(d) == int for d in data)

print(any_number(["dog","cat","duck"]))
print(any_number([2,3,"apple","banana","cherry"]))
print(any_number(["toyota","honda","lexus"]))