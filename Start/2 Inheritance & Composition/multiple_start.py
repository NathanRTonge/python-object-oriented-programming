"""
Python Object Oriented Programming by Joe Marini
Understanding multiple inheritance (from many classes)
"""

class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = 'Class A'


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = 'Class B'


class C(A, B):
    def __init__(self):
        super().__init__()
    
    def showprops(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)

c = C()
c.showprops()
#We see that Class A's name wins out, but why?

print(C.__mro__) 
#The class attribute __mro__ shows us the order for which attribute
#definitions are looked for, as C was deffined as C(A, B), it looks
#in A first and gets the name from their