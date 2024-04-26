def max_magnitude(nums):
    return max(abs(num) for num in nums)

print(max_magnitude([300, 20, -900]))
print(max_magnitude([10, 11, 12]))
print(max_magnitude([-5, -1, -89]))
print(max_magnitude([-5, 1.75, -89.24, 20.3]))