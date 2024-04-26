#number = input()
#number = int(number)

for num in range(1,21):
    if num == 4 or num == 13:
        print("Unlucky number")
    elif num % 2 == 0:
        print("An even number")
    else:
        print("An odd number")
    