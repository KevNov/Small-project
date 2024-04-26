# Implement your is_all_strings function below:

def is_all_strings(lst):
    return all([type(word) == str for word in lst])
    
print(is_all_strings(['a', 'b', 'c']))
print(is_all_strings([2,'a', 'b', 'c']))
print(is_all_strings(('hello', 'goodbye')))

# Now write function about intergers

def is_all_intergers(nums):
    return any([type(val) == int for val in nums ])

print(is_all_intergers([1,2,'hello','abc']))
print(is_all_intergers([3.5,8,4,7.659]))