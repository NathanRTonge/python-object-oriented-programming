"""
Python Object Oriented Programming by Joe Marini
Using instance methods and attributes
"""

class Book:
    #the "init" function is called when the instance is created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title

        #Add properties
        self.author = author
        self.pages = pages
        self.price = price
        #these are instence atributes ase they are only used by the specific instance

        self.__secret = 'secret stuff'
        #anything with __ is hidden

    #Create instance methods
    def getprice(self): #getter method
        if hasattr(self,'_discount'):
        #has attribute func, if object has this attribute, returns True
            return self.price - (self.price*self._discount)
            #returns price of book - discount
        return self.price
    
    def setdiscount(self,amount):
        self._discount = amount #_ to show that it is a local attribute
        #discount %


#Create some book instances
book1 = Book("War and Peace", 'Leo Tolstoy', 1225, 39.95)
book2 = Book('Road to Wigan Pier', 'George Orwell', 221, 12.99)

#Print the price of book1
print(book1.getprice())
print('')

#Try setting the discount
print(book2.getprice())
book2.setdiscount(0.25)
print(book2.getprice())
print('')

#properties with double underscores are hidden by the interpreter
print(book1._Book__secret) #by using._Class__secret, hidden varibles can be seen
print(book1.__secret) #trying to access directly will give error