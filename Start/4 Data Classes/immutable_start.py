"""
Python Object Oriented Programming by Joe Marini
Creating immutable data classes
"""

from dataclasses import dataclass


@dataclass(frozen= True)  #The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def newval(self, newval):
        self.value2 = newval


obj1 = ImmutableClass()
obj2 = ImmutableClass('not default', 50)
print(obj1.value1, obj1.value2)
print(obj2.value1, obj2.value2)

#attempting to change the value of an immutable class throws an exception
##obj1.value1 = 'Changed data'

#even functions within the class can't change anything
##obj2.newval(20)