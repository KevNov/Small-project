def displayed_name(first, last):
    print(f"my first name is {first} and my last name is {last}, nice to meet y'all")

names = {"first" : "kevin", "last": "suryadi" }
print(displayed_name(**names))
