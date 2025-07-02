from typing import Self
from typing import *

def build_int_ge_v(n:int) -> Type:

    class IntGZV(int):

        def __new__(cls, v: Self | int | float | str | bool) -> Self:

            value: int = super().__new__(cls, v)

            if value <= n:
                raise ValueError(f"Valore {v} deve essere maggiore di {n}")
            return value
        
        def __str__(self) -> str:
            return f"Anno di fondazione: {int(self)}"
    
        def __repr__(self) -> str:
            return f"IntG1909({int(self)})"
        
    return IntGZV