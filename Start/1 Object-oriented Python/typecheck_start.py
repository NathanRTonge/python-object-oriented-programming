"""
Python Object Oriented Programming by Joe Marini
Checking class types and instances
"""

class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


#Create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

#Use type() to inspect the object type
print(type(b1)) #gives type book
print(type(n2)) #gives type newspaper
print('')

#Compare two types together
print(type(b1) == type(b2)) #will give True as both books
print(type(b1) == type(n1)) #gives False as 1 newspaer other book
print('')

#Use isinstance(object, Class) to compare an instance to a type
print( isinstance(b1,Book) ) #True
print( isinstance(n1,Newspaper) ) #True
print( isinstance(n2,Book) ) #False
print( isinstance(n2,object) ) #True
#for object, all classes are a subclass of object so this will always be True