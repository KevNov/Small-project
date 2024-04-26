def multiply_all_num(*nums):
    total = 1
    for val in nums:
        total = total * val
    return total

print(multiply_all_num(1,2,3,4,5,6))

def sum_all_num(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_num(2,3,4,5,6,7,8))
