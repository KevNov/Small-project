#example of property

class Human:

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    #def get_age(self):
        #return self._age
    
    #def new_age(self,new_age):
        #if new_age >= 0:
            #self._age = new_age
        #else:
            #self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            raise ValueError("Age can't be negative")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

ppl = Human("Bret","walles",46)
#print(ppl._age)
#ppl.new_age(45)
print(ppl.age)
ppl.age = 39
print(ppl.age)
print(ppl.full_name)