from __future__ import annotations

from datetime import date
from custom_types import *

from typing import *


class Impiegato:
    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita
    _nascita: date # immutabile, noto alla nascita
    _stipendio: Importo # noto alla nascita
    
    _afferenza: _afferenza | None # da assoc. 'afferenza' [0..1], possibilmente non noto alla nascita

    def __init__(self, nome:str, cognome:str, nascita:date, stipendio:Importo,
                 dipartimento_aff: Dipartimento | None = None, data_afferenza: date | None=None) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)

        self._afferenza = None
        self.set_link_afferenza(dipartimento_aff, data_afferenza)

    def set_link_afferenza(self, dipartimento_aff: Dipartimento | None = None, data_afferenza:date | None = None) -> None:
        
        if dipartimento_aff is None and data_afferenza is None:
           
            # Se afferiva a un dipartimento, devo rimuoverlo da esso
            if self._afferenza is not None:
                self.remove_link_afferenza()
           
            # Altrimenti link non esiste
            self._afferenza = None
       
        elif (dipartimento_aff is None) != (data_afferenza is None):
            raise ValueError("dipartimento e data di afferenza devono essere entrambi None o entrambi non None")
        
        #creo link afferenza
        else:
            self._afferenza = dipartimento_aff.creaLinkAfferenza(self, data_afferenza)

    def remove_link_afferenza(self) -> None:
        if self._afferenza is not None:
            dipartimento = self.get_link_afferenza().get_dipartimento()
            dipartimento._remove_link_impiegato(self.get_link_afferenza())
            self._afferenza = None

    def get_link_afferenza(self) -> _afferenza:
        return self._afferenza

    def get_nome(self) -> str:
        return self._nome

    def get_cognome(self) -> str:
        return self._cognome

    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def set_cognome(self, cognome:str) -> None:
        self._cognome = cognome

    def get_nascita(self) -> date:
        return self._nascita

    def get_stipendio(self) -> Importo:
        return self._stipendio

    def set_stipendio(self, stipendio:Importo) -> None:
        self._stipendio = stipendio

    def __str__(self) -> str:
        if self._afferenza:
            afferenza: str = f"che afferisce al dip. {self._afferenza.get_dipartimento().get_nome()} dal {self._afferenza.get_data_afferenza()}" 
        else:
            afferenza = ""
        return f"Impiegato {self.get_nome()} {self.get_cognome()} {afferenza}"


class Dipartimento:
    _nome: str # noto alla nascita
    _telefono: Telefono # noto alla nascita

    _elenco_impiegati: set[_afferenza] # da assoc. 'afferenza' [0..*] certamente non noti alla nascita

    def __init__(self, nome:str, telefono:Telefono) -> None:
        self.set_nome(nome)
        self.set_telefono(telefono)
        self._elenco_impiegati = set()

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def set_telefono(self, telefono:Telefono) -> None:
        self._telefono = telefono

    def get_telefono(self) -> Telefono:
        return self._telefono

    def get_impiegati(self) -> frozenset[_afferenza]:
        return frozenset(self._elenco_impiegati)
    
    def creaLinkAfferenza(self, impiegato: Impiegato, data_afferenza:date) -> _afferenza:
        if impiegato.get_link_afferenza():
            impiegato.get_link_afferenza().get_dipartimento()._remove_link_impiegato(impiegato.get_link_afferenza())
        l:_afferenza = _afferenza(impiegato, self, data_afferenza)
        self._add_impiegato(l)
        impiegato._afferenza = l
        return l

    def _add_impiegato(self, afferenza: _afferenza) -> None:
        self._elenco_impiegati.add(afferenza)

    def _remove_link_impiegato(self, afferenza: _afferenza) -> None:
        if afferenza in self._elenco_impiegati:
            self._elenco_impiegati.remove(afferenza)
        else:
            raise ValueError("il link non è presente nel dipartimento")
        
    def remove_impiegato(self, impiegato:Impiegato) -> None:
        link: _afferenza = impiegato.get_link_afferenza()
        if link in self._elenco_impiegati:
            self._elenco_impiegati.remove(link)
            impiegato._afferenza = None
        else:
            raise ValueError(f"Impiegato {impiegato} non lavora a {self}")
    
    def __str__(self) -> str:
        if self._elenco_impiegati == set():
            impiegati:str = "Nessuno"
        else:
            impiegati:str = "\n".join(f"{i}" for i in self._elenco_impiegati)
        return f"Dipartimento: {self._nome} \nImpiegati: {impiegati}"



class _afferenza:
    _impiegato: Impiegato # ovviamente noto alla nascita e immutabile
    _dipartimento: Dipartimento # ovviamente noto alla nascita e immutabile
    _data_afferenza: date # immutabile, noto alla nascita

    def __init__(self, impiegato:Impiegato, dipartimento:Dipartimento, data_afferenza: date) -> None:
        self._impiegato = impiegato
        self._dipartimento = dipartimento
        self._data_afferenza = data_afferenza

    def get_impiegato(self) -> Impiegato:
        return self._impiegato

    def get_dipartimento(self) -> Dipartimento:
        return self._dipartimento

    def get_data_afferenza(self) -> date:
        return self._data_afferenza

    def __hash__(self) -> int:
        return hash((self.get_impiegato(), self.get_dipartimento()))

    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) \
            or hash(self) != hash(other):
            return False
        return (self.get_impiegato(), self.get_dipartimento()) == \
            (other.get_impiegato(), other.get_dipartimento())
    
    def __str__(self) -> str:
        return f"{self._impiegato.get_nome()} {self._impiegato.get_cognome()} lavora nel dip. {self._dipartimento.get_nome()} dal {self._data_afferenza}"

    def __repr__(self) -> str:
        return str(self)

class Progetto:
    _nome: str # noto alla nascita
    _budget: Importo
    _elenco_impiegati: dict[Impiegato, date]

    def __init__(self, nome:str, budget:Importo, impiegato:Impiegato | None) -> None:
        self.set_nome(nome)
        self.set_budget(budget)
        
    def creaLinkImpProg(self, impiegato:Impiegato, date:date) -> _imp_prog:
        if impiegato not in self._elenco_impiegati:
            self._elenco_impiegati
            
    

    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome

    def set_budget(self, budget:Importo) -> None:
        self._budget = budget

    def budget(self) -> Importo:
        return self._budget
    
class _imp_prog:
    _impiegato: Impiegato
    _progetto: Progetto
    _data: date

    def __init__(self, impiegato:Impiegato, progetto:Progetto, data:date) -> None:
        self._impiegato = impiegato
        self._progetto = progetto
        self._data = data

    def get_impiegato(self) -> None:
        return self._impiegato
    
    def get_data(self) -> None:
        return self._data

    def get_progetto(self) -> None:
        return self._progetto