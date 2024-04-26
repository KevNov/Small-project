print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("player1, Make your move!!")
player2 = input("player2, Make your move!!")


if player1 == "Rock" and player2 == "Scissors":
    print("player1 wins!")
elif player1 == "Rock" and player2 == "Paper":
    print("player2 wins!")
elif player1 == "Paper" and player2 == "Rock":
    print("player1 wins!")
elif player1 == "Papers" and player2 == "Scissors":
    print("player1 wins!")
elif player1 == "Scissors" and player2 == "Rock":
    print("player2 wins!")
elif player1 == "Scissors" and player2 == "Paper":
    print("player1 wins!")
elif player1 == player2:
    print("it's a tie")
else:
    print("something went wrong")
