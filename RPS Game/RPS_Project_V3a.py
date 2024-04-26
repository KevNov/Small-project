from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Please enter your move!! ").lower()
rand_num = randint(0,3)

if rand_num == 0:
    computer = "Rock"
elif rand_num == 1:
    computer = "Paper"
else:
    computer = "Scissors"
print(f"computer plays {computer}")

if player == computer:
    print("It's a tie")
elif player == "Rock":
    if computer == "Paper":
        print ("CPU won")
    elif computer == "Scissors":
        print("Player won")
elif player == "Paper":
    if computer == "Rock":
        print ("Player won")
    elif computer == "Scissors":
        print("CPU won")
elif player == "Scissors":
    if computer == "Paper":
        print ("Player won")
    elif computer == "Rock":
        print("CPU won")
else:
    print("Please, enter a valid option")

