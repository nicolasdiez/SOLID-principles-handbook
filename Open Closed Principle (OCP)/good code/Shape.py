from abc import ABC, abstractmethod

class Shape(ABC):
    # abstract method as part of the absctract class (ABC). Method is not defined in parent class, let the chilren define it.
    @abstractmethod
    def area (self):
        pass