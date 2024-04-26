# abs: return the absolute value of a number, in toher word turn every interger (negative or positive) into positive num

print(abs(-3.5))
print(-3.5)
print(abs(4))
print(abs(-7.28))

# sum: basicly sum all of number that exsist in a list (sum gonna start from left to right)

print(sum([2,4,6]))
# the optional start can be put in the right side of the list
print(sum([1,2,3,4,5], 20))
#it can also sum up float type of number
print(sum((1.5,2.6,4.77)))

print(sum(val for val in [2,4,7,10,13,17,28] if val % 2 == 0))

# ronud: a function that's used to returned a rounded number to ndigit precision after the decimal point

print(round(1.2345, 2))
print(round(23.76459, 3))
print(round(23.76459, None))