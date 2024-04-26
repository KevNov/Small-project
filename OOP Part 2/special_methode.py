#STILL NEED TO LEARN MORE ABOUT THIS

class Human:

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
    
    def __repr__(self):
        return f"Human named {self.first} {self.last}"
    
    def __len__(self):
        return self.age
    
    def __add__(self,other):
        if isinstance(other,Human):
            return Human(first='newborn', last=self.last, age=0)
        return "You can't add that"

    def __mul__(self,other):
        if isinstance(other,int):
            return [self for i in range(other)]
        return "CAN'T MULTIPLY"

p1 = Human("diana","wattson",45)
p2 = Human("barry","alexanderson", 35)
#print(p1)
#print(len(p1))

#print(p1 + p2)
print(p2 * 3)