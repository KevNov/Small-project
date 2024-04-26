# calculate citizen ages using OOP 

from datetime import date

class Citizen:

    @classmethod
    def calculate_age(cls,name,birth_date):
        return cls(name, date.today().year - birth_date)
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        return f"{self.name}'s age is {self.age}"
    
people = Citizen.calculate_age(input("what's ur name?"), int(input("when did you born?")))
print(people.show())
