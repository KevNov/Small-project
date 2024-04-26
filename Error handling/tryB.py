# handling error using command "try", "except", "else" and "finally"

while True:
    try:
        num = int(input("please type any number: "))
    except:
        print("That isn't a number")
    else:
        print("good job on typing that number")
        break
    finally:
        print("RUNS NO MATTER WHAT")

# try:
# 	num = int(input("please enter a number: "))
# except:
# 	print("That's not a number!")
# else:
# 	print("I'M IN THE ELSE!")
# finally:
# 	print("RUNS NO MATTER WHAT!")
    