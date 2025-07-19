from typing import Self
class FloatGez(float):
    def __new__(cls, v: Self | int | float | str | bool) -> Self:
        value: float = super().__new__(cls, v)   # creo un oggetto float
        if value < 0:
            raise ValueError(f"Errore, il valore deve essere >= 0")
        return value