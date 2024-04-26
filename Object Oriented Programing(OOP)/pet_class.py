# creating pet class using oop

class Pet:

    allowed = ["cat","dog","fish","bird"]

    def __init__(self,name,species):
        if species not in Pet.allowed:
            raise ValueError(f"you can't have {species} in this house")
        self.name = name
        self.species = species

    def set_species(self,species):
        if species not in Pet.allowed:
            raise ValueError(f"you can't have {species} in this house")
        self.species = species

animal = Pet("bruce", "dog")
animal2 = Pet("bryan", "bird")

print(animal2.name, animal2.species)