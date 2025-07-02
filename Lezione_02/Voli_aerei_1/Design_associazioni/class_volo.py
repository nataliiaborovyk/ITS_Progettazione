from typing import Self
from tipoDato_intGZ import IntGZ
from tipoDato_codiceVolo import CodiceVolo


class Volo:

    __codice: CodiceVolo    # noto dalla nascita / immutabile / {id}
    __durata: IntGZ     # noto dalla nascita / mutabile

    _elenco_codici: dict = {}

    def __new__(cls, codice:CodiceVolo, durata: IntGZ) -> Self:
        if codice in cls._elenco_codici:
            raise ValueError(f"Errore, volo con nome {codice} gia esiste")
        return super().__new__(cls)

    def __init__(self, codice: CodiceVolo, durata: IntGZ) -> None:
        self.__codice = codice
        self._elenco_codici[codice] = self
        self.setDurata = durata

    @property
    def getCodice(self) -> CodiceVolo:
        return self.__codice
   
    @property
    def getDurata(self) -> IntGZ:
        return self.__durata
    
    @getDurata.setter
    def setDurata(self, durata) -> None:
        self.__durata = durata    

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

