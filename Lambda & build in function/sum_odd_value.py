# sum all odd value that exist in this list below

def sum_odd_value(nums):
    return sum(num for num in nums if num % 2 != 0)

print(sum_odd_value([1,2,3,4,5,6,7]))
print(sum_odd_value([3,17,18,43]))
print(sum_odd_value([2,4,6]))
