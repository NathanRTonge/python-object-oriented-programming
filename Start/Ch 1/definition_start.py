"""
Python Object Oriented Programming by Joe Marini
Basic class definitions
"""

#Create a basic class
class Book:
    def __init__(self,title): #initialsier func
        self.title = title


#Create instances of the class
book1 = Book('1984')
book2 = Book('Animal Farm')


#Print the class and property
print(book1)
print(book1.title)