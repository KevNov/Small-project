#dec syntax @

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you")
        fn()
        print("Have a great day")
    return wrapper

@be_polite
def greet():
    print("My name is Alan")

@be_polite
def rage():
    print("Fuck you asshole")


# you dont have to set
# greet = be_polite(greet)

greet()
rage()
