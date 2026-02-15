
from __future__ import annotations
from typing import Any

from associazione_cit_naz import *
from custom_types import *


class Citta:

    _nome:str      # noto alla nascita / mutabile
    _abitanti:IntGEZ     # noto alla nascita / mutabile
    _cit_naz: cit_naz._link   # noto alla nascita / mutabile

    def __init__(self, nome:str, abitanti:IntGEZ, nazione: 'Nazione') -> None:
        self.set_nome(nome)
        self.set_abitanti(abitanti) 
        self._cit_naz = nazione.crea_link_citta_naz(self) # perche vincoli 1..1
        #self.setCitNaz(nazione)
        # self._cit_naz = cit_naz._link(self, nazione) 
    
    def get_nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome:str) -> None:
        self._nome = nome.capitalize()
    
    def get_abitanti(self) -> IntGEZ:
        return self._abitanti
    
    def set_abitanti(self, abitanti:IntGEZ) -> None:
        self._abitanti = abitanti

    def cit_naz(self) -> cit_naz._link:
        return self._cit_naz
    
    def set_cit_naz(self, nazione: 'Nazione') -> cit_naz._link:
        self._cit_naz = nazione.crea_link_citta_naz(nazione)       #cosa si fa con il vecchio link???
    
    def __hash__(self) -> int: 
        return hash((self._nome, self._abitanti))
    
    def __eq__(self, other:Any) -> bool:
        if other is None or not isinstance(other, Citta):
            return False
        if hash(self) != hash(other):
            return False
        return self._nome == other._nome and self._abitanti == other._abitanti

    def __str__(self) -> str:
        return f"Citta: {self.get_nome()}, abitanti: {self.get_abitanti()}, nazione {self.cit_naz()}"

    def __repr__(self) -> str:
        return f"Citta('{self.get_nome()}', {self.get_abitanti()}, {self.cit_naz()})"
    

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
           
            self.set_nome(nome)
            self._cit_naz = set()   #perche i vincoli sono  0..*   , se fosse 1..* dovrei aggiungere link come atributo del __init__
       
    def get_nome(self)  -> str:
        return self._nome
        
    def set_nome(self, nome) -> None:
        nome = nome.capitalize()
        
        if nome in self._elenco_nazioni:
            raise ValueError(f"Errore, la nazione con nome {nome} gia esiste")
        
        if self._nome is not None:
            del self._elenco_nazioni[self._nome]

        self._nome = nome
        self._elenco_nazioni[nome] = self

    def crea_link_citta_naz(self, citta: 'Citta') -> cit_naz._link:
        link: cit_naz._link = cit_naz._link(citta, self)  #prima citta e poi nazione come nel init cit_naz._link
        self.add_citta_naz(link)
        return link

    def add_citta_naz(self, link: cit_naz._link) -> None:
        self._cit_naz.add(link)

    def cit_naz(self) -> frozenset[cit_naz._link]:
        return frozenset(self._cit_naz)

    def __str__(self) -> str:
        return f"Nazione: {self.get_nome()}, citta: {self.cit_naz()}"
    
    def __repr__(self) -> str:
        return f"Nazione({self.get_nome()}, citta: {self.cit_naz()})"
    

class CompaniaAerea:

    _nome:str    # noto alla nascita / mutabile / {id}
    _aa:IntG1909     # noto alla nascita / immutabile
    _elenco_nomi:dict = {}  

    def __new__(cls, nome:str, aa: IntG1909) -> Self:
        nome = nome.capitalize()
        if nome in cls._elenco_nomi:
            raise ValueError(f"Errore, compania con nome {nome} gia esiste")
        return super().__new__(cls)
    
    def __init__(self, nome: str, aa: IntG1909) -> None:
        if not hasattr(self, "_nome"):
            self._nome = None
            self.set_nome(nome)
        self._aa = aa

    def get_aa(self) -> IntG1909:
        return self._aa

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome) -> None:
        nome = nome.capitalize()
        
        if nome in self._elenco_nomi:
            raise ValueError(f"Errore, compania con nome {nome} gia esiste")
        
        if self._nome is not None:
            del self._elenco_nazioni[self._nome]

        self._nome = nome
        self._elenco_nomi[nome] = self

    def __str__(self) -> str:
        return f"Compania aerea: {self.get_nome()}, anno di fondazione: {self.get_aa()}"
    

class Aeroporto:

    _codice:CodiceAeroporto    # noto alla nascita / immutabile / {id}
    _nome:str    # noto alla nascita / mutabile
    _elenco_codici: dict = {}     

    def __new__(cls, nome: str, codice:CodiceAeroporto) -> Self:
        if codice in cls._elenco_codici:
            raise ValueError(f"Errore, aeroporto con nome {codice} gia esiste")
        return super().__new__(cls)

    def __init__(self, nome:str, codice:CodiceAeroporto) -> None:
        self._codice = codice
        self._elenco_codici[codice] = self
        self.set_nome(nome)

    def get_codice(self) -> CodiceAeroporto:
        return self._codice

    def get_nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome:str) -> None:
        self._nome = nome.capitalize()
    
    def __str__(self) -> str:
        return f"Aeroporto: '{self.get_nome()}', codice: {self.get_codice()}"
    
    def __repr__(self) -> str:
        return f"Aeroporto('{self.get_nome()}', {self.get_codice()})"
    

class Volo:

    _codice: CodiceVolo    # noto dalla nascita / immutabile / {id}
    _durata: IntGZ     # noto dalla nascita / mutabile

    _elenco_codici: dict = {}

    def __new__(cls, codice:CodiceVolo, durata: IntGZ) -> Self:
        if codice in cls._elenco_codici:
            raise ValueError(f"Errore, volo con nome {codice} gia esiste")
        return super().__new__(cls)

    def __init__(self, codice: CodiceVolo, durata: IntGZ) -> None:
        self._codice = codice
        self._elenco_codici[codice] = self
        self.set_durata(durata)

    def get_codice(self) -> CodiceVolo:
        return self._codice
   
    def get_durata(self) -> IntGZ:
        return self._durata
    
    def set_durata(self, durata) -> None:
        self._durata = durata    

    def __str__(self) -> str:
        return f"Codice volo: {self.get_codice()}, durata: {self.get_durata()} minuti"
    

class cit_naz:

    class _link:

        _citta: 'Citta'
        _nazione: 'Nazione'

        def __init__(self, citta: 'Citta', nazione: 'Nazione') -> None:
            self._citta = citta
            self._nazione = nazione

        def get_citta(self) -> 'Citta':
            return self._citta
        
        def get_nazione(self) -> 'Nazione':
            return self._nazione
        
        def __str__(self) -> str:
            return f"Link(Citta: {self._citta.get_nome()} - Nazione: {self._nazione.get_nome()})"
        
        def __repr__(self) -> str:
            return F"cit_naz._link({self._citta.get_nome()}, {self._nazione.get_nome()})"