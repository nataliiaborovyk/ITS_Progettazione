
from __future__ import annotations
from typing import Any

from associazione_cit_naz import *

from assoc_class_nazione import Nazione
from tipoDato_intGEZ import IntGEZ

class Citta:

    _nome:str      # noto alla nascita / mutabile
    _abitanti:IntGEZ     # noto alla nascita / mutabile
    _cit_naz: cit_naz._link   # noto alla nascita / mutabile

    def __init__(self, nome:str, abitanti:IntGEZ, nazione: 'Nazione') -> None:
        self.setNome(nome)
        self.setAbitanti(abitanti) 
        self._cit_naz = nazione.creaLinkCitta(self) # perche vincoli 1..1
        #self.setCitNaz(nazione)
        # self._cit_naz = cit_naz._link(self, nazione) 
    
    def getNome(self) -> str:
        return self._nome
    
    def setNome(self, nome:str) -> None:
        self._nome = nome.capitalize()
    
    def getAbitanti(self) -> IntGEZ:
        return self._abitanti
    
    def setAbitanti(self, abitanti:IntGEZ) -> None:
        self._abitanti = abitanti

    def cit_naz(self) -> cit_naz._link:
        return self._cit_naz
    
    def setCitNaz(self, nazione: 'Nazione') -> cit_naz._link:
        self._cit_naz = nazione.creaLinkCitta(nazione)       #cosa si fa con il vecchio link???
    
    def __hash__(self) -> int: 
        return hash((self._nome, self._abitanti))
    
    def __eq__(self, other:Any) -> bool:
        if other is None or not isinstance(other, Citta):
            return False
        if hash(self) != hash(other):
            return False
        return self._nome == other._nome and self._abitanti == other._abitanti

    def __str__(self) -> str:
        return f"Citta: {self.getNome()}, abitanti: {self.getAbitanti()}, nazione {self.cit_naz()}"

    def __repr__(self) -> str:
        return f"Citta('{self.getNome()}', {self.getAbitanti()}, {self.cit_naz()})"
    
if __name__ == "__main__":
    

    n1: Nazione = Nazione("Italia")

    c1:Citta = Citta("Roma", IntGEZ(2746789), n1)
    print(c1)

    c2:Citta = Citta("roma", IntGEZ(2746789), n1)
    print(c2)

    c3:Citta = Citta("1111", IntGEZ(2746789), n1)  # ??? chi controlla creazione dei oggetti ???
    print(c3)

    print(c1 == c2)

    elenco_citta:set = {c1, c2}   # ??? due oggetti uguali possono esistere o devo inserire eq e hash ???
    print(elenco_citta)