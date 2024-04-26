from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f"player score: {player_wins} computer score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    player = input("player1, Make your move!!").lower()
    if player == "quit" or player == "q":
        break
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"computer plays {computer}")

    if player == computer:
        print("it's a tie")
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            player_wins += 1
        elif computer == "paper":
            print("cpu wins!")
            computer_wins += 1
    elif player == "paper": 
        if computer == "rock":
            print("player wins!")
            player_wins += 1
        elif computer == "scissors":
            print("cpu wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("cpu wins!")
            computer_wins += 1
        elif computer == "paper":
            print("player wins!")
            player_wins += 1
    else:
        print("please enter a valid option")

print(f"FINAL SCORE... player score: {player_wins} computer score: {computer_wins}")
