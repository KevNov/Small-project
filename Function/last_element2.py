# returning the last element from a list

def last_element(l):
    if l:
        return l[-1]
    return None

print(last_element([1,2,3,5,7,9]))
print(last_element(["apple","banana","cherry","mango"]))
print(last_element([]))