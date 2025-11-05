from typing import Self

class IntGEZ(int):
    def __new__(cls, v: Self | int | float | str | bool) -> Self:
        
        value: int = super().__new__(cls, v)

        if value < 0:
            raise ValueError(f"Errore, il valore deve essere >= 0")
        return value
    
    def __str__(self) -> str:
        return str(int(self))
    
    def __repr__(self) -> str:
        return f"IntGEZ({int(self)})"
  