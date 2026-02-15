from typing import Self
from custom_types import *

class CompaniaAerea:

    _nome:str    # noto alla nascita / mutabile / {id}
    _aa:IntG1909     # noto alla nascita / immutabile

    _elenco_nomi:dict[str,'CompaniaAerea'] = {}  

    def __new__(cls, nome:str, aa: IntG1909) -> Self:
        nome = nome.capitalize()
        if nome in cls._elenco_nomi:
            raise ValueError(f"Errore, compania con nome {nome} gia esiste")
        return super().__new__(cls)
    
    def __init__(self, nome: str, aa: IntG1909) -> None:
        if not hasattr(self, "_nome"):
            self._nome = None
            self.setNome = nome
        self._aa = aa

    @property
    def getAa(self) -> IntG1909:
        return self._aa
    
    @property 
    def getNome(self) -> str:
        return self._nome

    @getNome.setter
    def setNome(self, nome) -> None:
        nome = nome.capitalize()
        
        if nome in self._elenco_nomi:
            raise ValueError(f"Errore, compania con nome {nome} gia esiste")
        
        if self._nome is not None:
            del self._elenco_nomi[self._nome]

        self._nome = nome
        self._elenco_nomi[nome] = self

    def __str__(self) -> str:
        return f"Compania aerea: {self.getNome}, anno di fondazione: {self.getAa}"


if __name__ == "__main__":

    c1: CompaniaAerea = CompaniaAerea("lufthansa", IntG1909(1953))
    print(c1)

    # c2: CompaniaAerea = CompaniaAerea("LUFthansa", IntG1909(1953))
    # print(c2)

    c3: CompaniaAerea = CompaniaAerea("luf", IntG1909(1953))
    print(c3)
    c3.nome = "lufthansa"
    print(c3)