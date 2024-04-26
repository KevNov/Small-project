# define pet in a cage using oop

class Animal:

    pet_in_cage = 0

    @classmethod
    def displayed_pet_in_cage(cls):
        return f"there are {cls.pet_in_cage} animal in cage"
    
    def __init__(self,name,species,age):
        self.name = name
        self.species = species
        self.age = age
        Animal.pet_in_cage += 1

    def out_from_cage(self):
        Animal.pet_in_cage -= 1
        return f"{self.name} has been release from his cage"
    
    def introduction(self):
        return f"his name are {self.name} he's a {self.species}, ane he's {self.age}"
    
    def fav_food(self,foods):
        return f"{self.name} favourite foods are {foods}"
    

print(Animal.displayed_pet_in_cage())
pet = Animal("bryan","dog", 12)
pet2 = Animal("stich","cat", 8)
pet3 = Animal("rudy","bird",6)
print(Animal.displayed_pet_in_cage())
print(pet.out_from_cage())
print(Animal.displayed_pet_in_cage())

print(pet2.fav_food("fish"))
print(pet3.introduction())


    
