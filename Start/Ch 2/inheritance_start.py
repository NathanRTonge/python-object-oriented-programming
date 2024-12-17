"""
Python Object Oriented Programming by Joe Marini
Understanding class inheritance

Instead of repeatin self.title = title, self.price = price etc.,
we can use inheritance and the super() func to condense the code
"""

#This creates a super class that all others will draw from
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

#A subclass that includes the publisher and period of release
class Periodical(Publication):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

#All other subcasses can inherit code from those above with the 
#super().__init__() func
class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title,price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)


b1 = Book("Brave New World", "Aldous Huxley", 311, 12.00)
n1 = Newspaper("NY Times", "New York Times Company", 6.00, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
