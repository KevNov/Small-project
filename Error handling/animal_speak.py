# defining animal noises
# noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}

def speak(animals):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    noises = noises.get(animals)
    if noises:
        return noises
    elif type(animals) is not str:
        raise TypeError("That's not a word")
    return("The animal isn't on the list")

print(speak('cat'))
print(speak('pig'))
#print(speak(35))
print(speak('elephant'))