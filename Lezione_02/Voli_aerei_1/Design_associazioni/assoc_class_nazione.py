from associazione_cit_naz import *

from typing import Self
from typing import Any

class Nazione:

    _nome: str # noto alla nascita / mutabile / {id}
    _elenco_nazioni: dict = {}
    _cit_naz: set = set[cit_naz._link]   #noto alla nascita / mutabile

    def __new__(cls, nome:str) -> Self:
        nome = nome.capitalize()
        
        if nome in cls._elenco_nazioni:
            raise ValueError(f"Errore, nazione con nome {nome} gia esiste")
        
        return super().__new__(cls)

    def __init__(self, nome:str)  -> None:
        
        if not hasattr(self, "_nome"):  # controllo se un ogetto ha attributo _nome
            self._nome = None
           
            self.setNome(nome)
            self._cit_naz = set()   #perche i vincoli sono  0..*   , se fosse 1..* dovrei aggiungere link come atributo del __init__
       
    def getNome(self)  -> str:
        return self._nome
        
    def setNome(self, nome) -> None:
        nome = nome.capitalize()
        
        if nome in self._elenco_nazioni:
            raise ValueError(f"Errore, la nazione con nome {nome} gia esiste")
        
        if self._nome is not None:
            del self._elenco_nazioni[self._nome]

        self._nome = nome
        self._elenco_nazioni[nome] = self

    def creaLinkCitta(self, citta: 'Citta') -> cit_naz._link:
        link: cit_naz._link = cit_naz._link(citta, self)  #prima citta e poi nazione come nel init cit_naz._link
        self.addCittNaz(link)
        return link

    def addCittNaz(self, link: cit_naz._link) -> None:
        self._cit_naz.add(link)

    def cit_naz(self) -> frozenset[cit_naz._link]:
        return frozenset(self._cit_naz)

    def __str__(self) -> str:
        return f"Nazione: {self.getNome()}, citta: {self.cit_naz()}"
    
    def __repr__(self) -> str:
        return f"Nazione({self.getNome()}, citta: {self.cit_naz()})"
    
if __name__ == "__main__":

    from assoc_class_citta import Citta

    n1: Nazione = Nazione("italia")
    print(n1)
    print(n1.cit_naz())   

    c1:Citta = Citta("Roma", IntGEZ(2746789), n1)
    n1.creaLinkCitta(c1)  #come argomento va oggetto e non stringa
    print(n1)



    # n2: Nazione = Nazione("ITALIA")
    # print(n2)

    # n3: Nazione = Nazione("1111")   # un problema
    # print(n3)    

 # solo alcuni utenti (admin) possono creare o cambiare il nome ???? 

    # n4: Nazione = Nazione("ital")
    # print(n4)
    # n4.setNome("Italia")
    # print(n4)
    # n4.setNome("Italia")
    # print(n4)

