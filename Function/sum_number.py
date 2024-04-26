def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

print(sum_even_numbers([1,2,3,4,5,6,7,8,9,10]))

# count dolar sign
def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count

print(count_dollar_signs("$uper $size $suck"))




