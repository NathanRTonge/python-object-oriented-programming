"""
Python Object Oriented Programming by Joe Marini
Using data classes to represent data objects
"""
from dataclasses import dataclass

@dataclass #must use @dataclass decorator
class Book:
    #must use type annotations to tell data class what each varible's type is
    title: str 
    author: str
    pages: int
    price: float
    #the order matters, as it is the order that is passed into the decorator's __init__

    def bookinfo(self):
        return f'{self.title}, by {self.author} for £{self.price}'
    #can add functions like a regular class
"""Dataclasses are very useful when the only use of a class is to store
data"""

# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# access fields
print(b1.title)
print(b2.author)
print('')

# print the book itself - dataclasses implement __repr__/__str__ automatically
print(b1)
print(b2)
print('')

# comparing two dataclasses - they implement __eq__ automatically
print(b1 == b2)
print(b1 == b3)
print('')

# change some fields
print(b1.bookinfo())
b1.title = 'Animal Farm'
b1.price = 11.99
b1.author = 'George Orwell'
print(b1.bookinfo())