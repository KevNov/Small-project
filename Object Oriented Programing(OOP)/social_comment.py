# defining social comment using oop

class comment:
    def __init__(self,username,text,likes=0):
        self.name = username
        self.text = text
        self.likes = likes

user1 = comment("LowTierGod", "you should kys NOW!!!", 30)
user2 = comment("pitstop", "Mesin is gay", 43)
user3 = comment("r0bocup", "my dick is hard")

print(user1.name,user1.text,user1.likes)
print(user2.name,user2.text,user2.likes)
print(user3.name,user3.text,user3.likes)