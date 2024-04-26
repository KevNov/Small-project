# filter a number from a certain list

def odd_number(nums):
    return list(filter(lambda n: n %2 != 0, nums))

print(odd_number(list(range(2,15))))
print(odd_number([24,25,33,37,43,56]))
