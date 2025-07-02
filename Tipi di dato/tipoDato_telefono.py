from typing import Self
import re

class Telefono(str):

    def __new__(cls, tel:str | Self | int) -> Self:

        value: str = super().__new__(cls, tel)

        if not re.fullmatch(r'^\d{10}$', value):
            raise ValueError(f"{value} non è un numero di telefono italiano valido")
        return value
    
    def __str__(self) -> str:
        return f"Telefono: {super().__str__()}"
    
    def __repr__(self) -> str:
        return f"Telefono({super().__str__()})"


if __name__ == "__main__":

    t1: Telefono = Telefono(3888777766)
    print(t1)

    t2: Telefono = Telefono("3888777766")
    print(t2)

    # t3: Telefono = Telefono(388877776)
    # print(t3)

    # t4: Telefono = Telefono("3888777m66")
    # print(t4)

    elenco:set = {t1, t2}
    print(elenco)