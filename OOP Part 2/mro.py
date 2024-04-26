# Methode resolution order

class A:
    def do_something(self):
        print("Methode defined in: A")

class B(A):
    def do_something(self):
        print("Methode defined in: B")

class C(A):
    def do_something(self):
        print("Methode defined in: C")

class D(B,C):
    def do_something(self):
       print("Methode defined in: D")
       super().do_something() 

#print(D.__mro__)
#print(D.mro())
#help(D)
thing = D()
print(thing.do_something())

# the order = D-B-C-A-Object
        