"""
Python Object Oriented Programming by Joe Marini
Using Abstract Base Classes to implement interfaces
"""

from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass
"""This class acts as an interface/contract as it can be used to 
ensure that only the classes that can be jsonified will need to
define a toJSON() function"""

class Circle(GraphicShape, JSONify):
    """having JSONify as the 2nd inherited class means that this subclass
    will have to give a toJSON() definition"""
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
    def toJSON(self):
        return f'{{"Circle": {str(self.calcArea())}}}'


c = Circle(10)
print(c.calcArea())
print(c.toJSON())
