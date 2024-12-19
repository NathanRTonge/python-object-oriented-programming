"""
Python Object Oriented Programming by Joe Marini
Using Abstract Base Classes to enforce class constraints
"""
#imports abstract base class functionality
from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    
    #@abstact method tells the code that each subclass
    #must have its own definition
    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        #pi r^2
        return 3.14159 * (self.radius**2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    
    def calcArea(self):
        return self.side**2

# g = GraphicShape()
#As GraphicShape inherits directly from 
#AbstarctBaseClass, it cannot be created by user 


c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
