#Define a function called generate_evens
def generate_evens(numlist):
    return [num for num in numlist if num % 12 == 0]

print(generate_evens(list(range(1,51))))
print(generate_evens(list(range(60,121))))

