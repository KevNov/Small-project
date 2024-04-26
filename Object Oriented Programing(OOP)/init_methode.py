# creating oop using __init__ methode

class user:
    def __init__(self,first,foods,ages):
        self.name = first
        self.foods = foods
        self.age = ages

user1 = user("ihrom","katsu",35)
user2 = user("budi","nasgor",47)

print(user1.name, user1.age)
print(user2.name, user2.age)


