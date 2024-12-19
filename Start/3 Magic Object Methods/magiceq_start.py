"""
Python Object Oriented Programming by Joe Marini
Using the __eq__ and __lt__/__ge__ magic methods
"""

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    #The __eq__ method checks for equality (== bool) between two objects
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError('Can\'t compare book and non-book')
        #if other object isn't book, raises value error

        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)
        #equates each attribute of object with other object and returns True if all equal

    #The __ge__ establishes >= relationship with another obj
    def __ge__(self,value):
        if not isinstance(value, Book):
            raise ValueError('Can\'t compare book and non-book')
        
        return self.price >= value.price

    #The __lt__ establishes < relationship with another obj
    def __lt__(self,value):
        if not isinstance(value, Book):
            raise ValueError('Can\'t compare book and non-book')
        
        return self.price < value.price



b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

#Check for equality
print(b1 == b3)
print(b1 == b2)
#print(b2 == 5)

print('')

#Check for greater and lesser value
print(b1 >= b2)
print(b1 < b2)

print('')

#Now we can sort them too
books = [b1, b2, b3, b4]

books.sort()
#.sort() uses the < sign to sort a list from smallest to biggest value

print(*(book.title for book in books))
print([book.title for book in books])
print(*(f'{book.title}: £{book.price}\n' for book in books))
#prints the title of each book 
