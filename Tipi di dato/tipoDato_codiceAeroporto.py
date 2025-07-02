from typing import Self
import re

class CodiceAeroporto(str):

    def __new__(cls, cod: str | Self) -> Self:
        codice:str = cod.upper().strip()
        if not re.fullmatch(r'^[A-Z]{3,4}$', codice):
            raise ValueError(f"Errore, {codice} non è un codice di aeroporto")
        return super().__new__(cls, codice)
    
    def __str__(self) -> str:
        return  super().__str__()   # oppure str(self)
    
    def __repr__(self) -> str:
        return f"CodiceAeroporto({ super().__str__()})"
    
if __name__ == "__main__":

    c1:CodiceAeroporto = CodiceAeroporto("fco")
    print(c1)

    # c2:CodiceAeroporto = CodiceAeroporto("f1o")
    # print(c2)

    c3:CodiceAeroporto = CodiceAeroporto("FCO")
    print(c3)

    c4:CodiceAeroporto = CodiceAeroporto("LIrf")
    print(c4)

    c5:CodiceAeroporto = CodiceAeroporto(c1)
    print(c5)
   
    print(c1 == c3)

    elenco:set = {c1, c3, c4, c5}
    print(elenco)