from typing import Self
from custom_types import *

class Aeroporto:

    _codice:CodiceAeroporto    # noto alla nascita / immutabile / {id}
    _nome:str    # noto alla nascita / mutabile
    _elenco_codici: dict[str,'Aeroporto'] = {}     

    def __new__(cls, nome: str, codice:CodiceAeroporto) -> Self:
        if codice in cls._elenco_codici:
            raise ValueError(f"Errore, aeroporto con nome {codice} gia esiste")
        return super().__new__(cls)

    def __init__(self, nome:str, codice:CodiceAeroporto) -> None:
        self._codice = codice
        self._elenco_codici[codice] = self
        self.setNome = nome

    @property
    def getCodice(self) -> CodiceAeroporto:
        return self._codice

    @property
    def getNome(self) -> str:
        return self._nome
    
    @getNome.setter
    def setNome(self, nome:str) -> None:
        self._nome = nome.capitalize()
    
    def __str__(self) -> str:
        return f"Aeroporto: '{self.getNome}', codice: {self.getCodice}"
    
    def __repr__(self) -> str:
        return f"Aeroporto('{self.getNome}', {self.getCodice})"
    

if __name__ == "__main__":

    a1:Aeroporto = Aeroporto("Leonardo da Vinci", CodiceAeroporto("fco"))
    print(a1)

    # a2:Aeroporto = Aeroporto("leonardo da Vinci", CodiceAeroporto("fco"))
    # print(a2)

    a3:Aeroporto = Aeroporto("vicino casa mia", CodiceAeroporto("vcm"))
    print(a3)     #  ?? chi controlla input ??

    a3.codice = CodiceAeroporto("fco")
    print(a3)

    elenco_aeroporti:set = {a1, a3}
    print(elenco_aeroporti)
