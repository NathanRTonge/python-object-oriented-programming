"""
Python Object Oriented Programming by Joe Marini
Implementing default values in data classes
"""

from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(10,30))


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str
    author: str = 'No Author'
    pages: int = 0
    price: float = field(default_factory= price_func)
    # attributes w/ no default must come first
    #the defualt_factory can be used to return a default from a function

b1 = Book('1984')
print(b1)
print('')

b1 = Book("War and Peace", "Leo Tolstoy", 1225)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234)
print(b1)
print(b2)