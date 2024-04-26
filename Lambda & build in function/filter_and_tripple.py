# filter a list of number that can be divided by 4 and multiply that num by 3

def triple_and_filter(nums):
    return list(filter(lambda n: n % 4 == 0, map(lambda n: n * 3, nums)))

print(triple_and_filter([1,2,3,4])) 
print(triple_and_filter([6,8,10,12]))