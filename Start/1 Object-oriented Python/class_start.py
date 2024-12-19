"""
Python Object Oriented Programming by Joe Marini
Using class-level and static methods
"""

class Book:
    #properties defined at the class level are shared by all instances
    BOOK_TYPES = ('HARDCOVER', 'PAPERBACK', 'EBOOK') #(caps as class attribute)
    
    #double-underscore properties are hidden from other classes
    #as this varible is about this class, it should be contained in it
    __booklist = None

    #create a class method (takes class 'cls' as 1st arg not instance 'self')
    @classmethod #use this decorator to make class method
    def get_book_types(cls):
        return cls.BOOK_TYPES

    #Create a static method (doesn't modify state of class or instance)
    #good for if no cls or self attribute needed & func is about the class
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    #instance methods receive a specific object instance as an argument
    #and operate on data specific to that object instance (have self)
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title #title is an instance varible as it is unique to each instance
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f'{booktype} is not a valid booktype!')
        else:
            self.booktype = booktype


#Access the class attribute
print('Book types: ', Book.get_book_types())

#Create some book instances
b1 = Book('Paradise Lost', 'HARDCOVER')
b2 = Book('Invincible', 'PAPERBACK')

#Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)