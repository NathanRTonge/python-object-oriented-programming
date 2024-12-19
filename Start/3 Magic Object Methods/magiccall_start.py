"""
Python Object Oriented Programming by Joe Marini course example
Using the __call__ magic method
"""

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs £{self.price}"

    #The __call__ method can be used to call the object like a function
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    #when object() is called passes in 3 attributes and redefines object attributes

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

#Call the object as if it were a function
print(b1)

print('')

b1('As It Happened', 'Clement Atlee', 12.99)
print(b1)