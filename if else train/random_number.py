from random import randint

num = randint(1,50)


if num >= 1 and num <= 10:
    print("green")
elif num >= 11 and num <= 20:
    print("blue")
elif num >= 21 and num <= 30:
    print("red")
elif num >= 31 and num <= 40:
    print("orange")
else:
    print("purple")