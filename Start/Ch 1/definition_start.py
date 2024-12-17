# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


#create a basic class
class Book:
    def __init__(self,title): #initialsier func
        self.title = title


#create instances of the class
book1 = Book('1984')
book2 = Book('Animal Farm')


#print the class and property
print(book1)
print(book1.title)