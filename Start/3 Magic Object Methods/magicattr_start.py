"""
Python Object Oriented Programming by Joe Marini
Using the __setattribute__, __getattr__ and __getattribute__
magic methods
"""

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs £{self.price:.2f}"


    #__getattribute__ called when an attr is retrieved.
    # Don't directly access the attr name otherwise a recursive loop is created
    def __getattribute__(self, name):
        if name == 'price':
            pri = super().__getattribute__('price')
            dis = super().__getattribute__('_discount')
            return pri - (pri*dis)
        return super().__getattribute__(name)



    #__setattr__ called when an attribute value is set. Don't set the attr
    # directly here otherwise a recursive loop causes a crash
    def __setattr__(self, name, value):
        if name == 'price':
            if type(value) is not float:
                raise ValueError('The \'price\' attribute must be a float')
        return super().__setattr__(name,value)


    #__getattr__ called when __getattribute__ lookup fails - you can
    # pretty much generate attributes on the fly with this method
    def __getattr__(self,name):
        return f'"{name}" attribute doesn\'t exist.'



b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

#b1.price = 38
b1.price = 38.00
print(b1)

print('')

print(b1.bookcover)