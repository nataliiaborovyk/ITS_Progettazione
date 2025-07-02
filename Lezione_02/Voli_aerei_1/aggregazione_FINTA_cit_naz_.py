from class_citta import Citta
from tipoDato_intGEZ import IntGEZ
from typing import Self

class Nazione:

    __nome: str # noto alla nascita / mutabile / {id}
    _elenco_nazioni: dict = {}
    _elenco_citta: set[Citta]  # noto alla nascita / mutabile

    def __new__(cls, nome:str, elenco_citta:set[Citta]) -> Self:
        nome = nome.capitalize()
        if nome in cls._elenco_nazioni:
            raise ValueError(f"Errore, nazione con nome {nome} gia esiste")
        return super().__new__(cls)


    def __init__(self, nome:str, elenco_citta:set[Citta])  -> None:
        if not hasattr(self, "__nome"):  # controllo se un ogetto ha attributo  nome
            self.__nome = None
            self.setNome = nome
            self._elenco_citta = set(elenco_citta)

    @property              #  decoratore  .nome == .getNome()
    def getNome(self)  -> str:
        return self.__nome

    @getNome.setter          
    def setNome(self, nome) -> None:
        nome = nome.capitalize()
        
        if nome in self._elenco_nazioni:
            raise ValueError(f"Errore, la nazione con nome {nome} gia esiste")
        
        if self.__nome is not None:
            del self._elenco_nazioni[self.__nome]

        self.__nome = nome
        self._elenco_nazioni[nome] = self

    def cit_naz(self) -> frozenset[Citta]:
        return frozenset(self._elenco_citta)
    
    def add_citta(self, c: Citta) -> None:
        self._elenco_citta.add(c)

    def __str__(self) -> str:
        return f"Nazione: {self.getNome}, elenco delle citta appartenenti: {self.cit_naz()}"
    
    def __repr__(self) -> str:
        return f"Nazione({self.getNome})"
    
if __name__ == "__main__":

    n1: Nazione = Nazione("italia", {Citta("Roma", IntGEZ(2746789))})
    print(n1)

    n1.add_citta(Citta("Milano", IntGEZ(1422630)))
    
    print(n1.cit_naz())
   
    print(n1._elenco_citta)   #!!!!!!!!!

    x = n1.cit_naz()
    print(x.pop())



    # n2: Nazione = Nazione("ITALIA")
    # print(n2)

    # n3: Nazione = Nazione("1111")   # un problema
    # print(n3)    

 # solo alcuni utenti (admin) possono creare o cambiare il nome ???? 

    # n4: Nazione = Nazione("ital")
    # print(n4)
    # n4.nome = "Italia"
    # print(n4)
    # n4._nome = "Italia"
    # print(n4)


