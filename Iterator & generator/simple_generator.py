# creating a example of a generator

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(11)
next(counter)

for c in counter:
    print(c)
