from typing import Self
from custom_types import *


class Volo:

    _codice: CodiceVolo    # noto dalla nascita / immutabile / {id}
    _durata: IntGZ     # noto dalla nascita / mutabile

    _elenco_codici: dict[CodiceVolo,'Volo'] = {}

    def __new__(cls, codice:CodiceVolo, durata: IntGZ) -> Self:
        if codice in cls._elenco_codici:
            raise ValueError(f"Errore, volo con nome {codice} gia esiste")
        return super().__new__(cls)

    def __init__(self, codice: CodiceVolo, durata: IntGZ) -> None:
        self._codice = codice
        self._elenco_codici[codice] = self
        self.setDurata = durata

    @property
    def getCodice(self) -> CodiceVolo:
        return self._codice
   
    @property
    def getDurata(self) -> IntGZ:
        return self._durata
    
    @getDurata.setter
    def setDurata(self, durata) -> None:
        self._durata = durata    

    def __str__(self) -> str:
        return f"Codice volo: {self.getCodice}, durata: {self.getDurata} minuti"

if __name__ == "__main__":

    v1:Volo = Volo(CodiceVolo("aa756"), IntGZ(120))
    print(v1)

    # v2:Volo = Volo(CodiceVolo("AA756"), IntGZ(120))
    # print(v2)

    v3:Volo = Volo(CodiceVolo("Aa755"), IntGZ(120))
    print(v3)
    v3.codice = CodiceVolo("aa746")
    print(v3)

