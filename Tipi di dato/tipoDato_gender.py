from enum import *

class Gender(StrEnum):
    donna = auto()
    uomo = auto()

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"Gender({self.name})"

