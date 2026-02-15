from typing import Self
import re

class CodiceVolo(str):

    def __new__(cls, cod: str | Self) -> Self:
        codice:str = cod.upper().strip()
        if not re.fullmatch(r'^[A-Z]{2}\d{1,4}$', codice):
            raise ValueError(f"Errore, {codice} non è un codice di volo")
        return super().__new__(cls, codice)
    
    def __str__(self) -> str:
        return  super().__str__()  # oppure str(self)
    
    def __repr__(self) -> str:
        return f"CodiceVolo({ super().__str__()})"
    
if __name__ == "__main__":

    c1:CodiceVolo = CodiceVolo("sd435")
    print(c1)

    # c2:CodiceVolo = CodiceVolo("sda435")
    # print(c2)

    c3:CodiceVolo = CodiceVolo("SD435")
    print(c3)

    c4:CodiceVolo = CodiceVolo(c1)
    print(c4)

    print(c1 == c3)

    elenco:set = {c1, c3, c4}
    print(elenco)