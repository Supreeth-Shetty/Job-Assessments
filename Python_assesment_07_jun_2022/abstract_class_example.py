from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Processing laptop")

class Desktop(Computer):
    def process(self):
        print("Processing desktop")

try:
    comp = Computer()
except TypeError as e:
    print(f"Error : {e}\nThis is an abstract class hence cannot be instantiated directly")

compLap = Laptop()
compLap.process()

compDex = Desktop()
compDex.process()

print(f"\n{'#'*120}")
print("""Notes
0. Python by default does not support creating abstract class, so we have to import ABC from abc module which stands for abstract base class .
1. The abstract class is a class that cannot be directly instantiated it requires child class.
2. The abstract class should have atleast 1 abstract method.
3. The abstract method should be defined with the @abstractmethod decorator.

Abstract class can be used to define an interface or a blue print for the child class which inherites abstract class.""")

