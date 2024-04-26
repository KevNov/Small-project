# create a function using map that divided all of tha number on list by 2

def divided_num(nums):
    return list(map(lambda x: x / 2, nums))

print(divided_num([2,4,6,8]))
print(divided_num([40,50,70,90]))
