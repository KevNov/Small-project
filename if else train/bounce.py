# ask about age
# 18-21 wear a wristband
# 21+ allowed to drink
# too young, sorry

age = input("How old are you: ")
age = int(age)

if age != "":
    if age >= 18 and age < 21:
        print("You may enter, but wear wristband!")
    elif age >= 21:
        print("You can enter and drink!")
    else:
        print("sorry, you're too young")
else:
    print("please enter your age!")

