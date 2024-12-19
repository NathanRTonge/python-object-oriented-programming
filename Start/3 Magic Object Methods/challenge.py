"""
Python Object Oriented Programming by Joe Marini course example
# Programming challenge: add methods for comparison and equality

Challenge: use a magic method to make stocks and bonds sortable
# Stocks should sort from low to high on price
# Bonds should sort from low to high on yield
"""

from abc import ABC, abstractmethod


class Asset(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def __str__(self):
        pass


class Stock(Asset):
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.company = company
        self.ticker = ticker
    
    def __lt__(self, othr_stock):
        return self.price < othr_stock.price
    
    def __str__(self):
        return f'{self.ticker}: {self.company} -- ${self.price:.2f}'


class Bond(Asset):
    def __init__(self, price, desc, duration, yieldamt):
        super().__init__(price)
        self.desc = desc
        self.duration = duration
        self.yieldamt = yieldamt

    def __lt__(self, othr_bond):
        return self.yieldamt < othr_bond.yieldamt
    
    def __str__(self):
        return f'{self.desc} : {self.duration}yr : ${self.price:.2f} : \
{self.yieldamt}%'


# ~~~~~~~~~ TEST CODE ~~~~~~~~~
stocks = [
    Stock("MSFT", 342.0, "Microsoft Corp"),
    Stock("GOOG", 135.0, "Google Inc"),
    Stock("META", 275.0, "Meta Platforms Inc"),
    Stock("AMZN", 120.0, "Amazon Inc")
]

bonds = [
    Bond(95.31, "30 Year US Treasury", 30, 4.38),
    Bond(96.70, "10 Year US Treasury", 10, 4.28),
    Bond(98.65, "5 Year US Treasury", 5, 4.43),
    Bond(99.57, "2 Year US Treasury", 2, 4.98)
]

stocks.sort()
bonds.sort()

for stock in stocks:
    print(stock)
print("-----------")
for bond in bonds:
    print(bond)
