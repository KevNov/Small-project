# create oop code that maka chicken poop an egg

class Chicken:
    total_eggs = 0

    def __init__(self,name,species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs
    
c1 = Chicken("peter", "cochin")
c2 = Chicken("oggy", "sussex")

print(c1.lay_egg())
print(c2.lay_egg())
print(c1.lay_egg())
print(Chicken.total_eggs)
print(c2.lay_egg())
print(c1.lay_egg())
print(c2.lay_egg())
print(Chicken.total_eggs)