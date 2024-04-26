num_list = list(range(2,13))
print(num_list)

square = map(lambda x: x**2, num_list)
print(list(square))
for nums in square:
    print(nums)


citizen = ["haidar", "kevin", "faiz", "dion"]
people = map(lambda name : name.upper(), citizen)
print(list(people))