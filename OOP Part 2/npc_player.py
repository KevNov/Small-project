# ceate an inheritence oop 

class Player:

    def __init__(self,name,HP,level):
        self.name = name
        self.HP = HP
        self.level = level

class NPC(Player):

    def __init__(self, name, HP, level,catchphrase):
        super().__init__(name, HP, level)
        self.catchphase = catchphrase

    def speech(self):
        return f"{self.name} catchphrase is {self.catchphase}"
    
p1 = NPC("Austin",600,35,"Don't u dare die")
p2 = NPC("Bob",750,40,"Hooola")

print(p1.name,p2.name)
print(p1.HP,p2.HP)
print(p1.level,p2.level)
print(p1.speech())
print(p2.speech())


