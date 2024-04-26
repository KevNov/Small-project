from random import random

def flip_coin():
    # generate random number between 0-1
    r = random()

    if r > 0.5:
        return ("heads")
    else:
        return ("tails")
    
print(flip_coin())
