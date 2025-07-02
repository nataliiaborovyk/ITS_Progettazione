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

    _progetti: dict[Progetto, imp_prog._link] # da assoc. 'imp_prog' [0..*] certamente non noti alla nascita

    def __init__(self, nome:str, cognome:str, nascita:date, stipendio:Importo,
                 dipartimento_aff: Dipartimento | None = None, data_afferenza: date | None=None) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        self.set_link_afferenza(dipartimento_aff, data_afferenza)
        self._progetti = dict()

    def set_link_afferenza(self, dipartimento_aff: Dipartimento | None = None, data_afferenza: date | None=None) -> None:
        if (dipartimento_aff is None) != (data_afferenza is None):
            raise ValueError("Dipartimento e data di afferenza devono essere entrambi None o entrambi non None")


        # Se afferiva a un dipartimento, devo rimuoverlo da esso
        try:
            if self.get_link_afferenza():
                self.get_link_afferenza().dipartimento()._remove_impiegato(self.get_link_afferenza())
        except AttributeError:  # il campo _afferenza non era mai stato settato: questo metodo è stato quindi chiamato dal costruttore
            pass

        if dipartimento_aff: # sono entrambi not None
            self._afferenza = _afferenza(impiegato=self, dipartimento=dipartimento_aff, data_afferenza=data_afferenza)
            dipartimento_aff._add_impiegato(self._afferenza)
        else: # sono entrambi None
            self._afferenza = None

    def get_link_afferenza(self) -> _afferenza:
        return self._afferenza

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def set_cognome(self, cognome:str) -> None:
        self._cognome = cognome

    def nascita(self) -> date:
        return self._nascita

    def stipendio(self) -> Importo:
        return self._stipendio

    def set_stipendio(self, stipendio:Importo) -> None:
        self._stipendio = stipendio

    def progetti(self) -> frozenset[imp_prog._link]:
        return frozenset(self._progetti.values())

    def _add_link_imp_prog(self, l: imp_prog._link) -> None:
        if l.impiegato() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.progetto() in self._progetti:
            raise KeyError("Lavoro già nel progetto")
        self._progetti[l.progetto()] = l

    def _remove_link_imp_prog(self, l: imp_prog._link) -> None:
        if l.impiegato() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.progetto() not in self._progetti:
            raise KeyError("Non lavoravo nel progetto")
        del self._progetti[l.progetto()]


class Dipartimento:
    _nome: str # noto alla nascita
    _telefono: Telefono # noto alla nascita

    _impiegati: set[_afferenza] # da assoc. 'afferenza' [0..*] certamente non noti alla nascita

    def __init__(self, nome:str, telefono:Telefono) -> None:
        self.set_nome(nome)
        self.set_telefono(telefono)
        self._impiegati = set()

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def set_telefono(self, telefono:Telefono) -> None:
        self._telefono = telefono

    def telefono(self) -> Telefono:
        return self._telefono

    def impiegati(self) -> frozenset[_afferenza]:
        return frozenset(self._impiegati)

    def _add_impiegato(self, afferenza: _afferenza) -> None:
        self._impiegati.add(afferenza)

    def _remove_impiegato(self, afferenza: _afferenza) -> None:
        self._impiegati.remove(afferenza)

class _afferenza:
    _impiegato: Impiegato # ovviamente noto alla nascita e immutabile
    _dipartimento: Dipartimento # ovviamente noto alla nascita e immutabile
    _data_afferenza: date # immutabile, noto alla nascita

    def __init__(self, impiegato:Impiegato, dipartimento:Dipartimento, data_afferenza: date) -> None:
        self._impiegato = impiegato
        self._dipartimento = dipartimento
        self._data_afferenza = data_afferenza

    def impiegato(self) -> Impiegato:
        return self._impiegato

    def dipartimento(self) -> Dipartimento:
        return self._dipartimento

    def data_afferenza(self) -> date:
        return self._data_afferenza

    def __hash__(self) -> int:
        return hash((self.impiegato(), self.dipartimento()))

    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) \
            or hash(self) != hash(other):
            return False
        return (self.impiegato(), self.dipartimento()) == \
            (other.impiegato(), other.dipartimento())


class Progetto:
    _nome: str # noto alla nascita
    _budget: Importo
    _coinvolti: dict[Impiegato, imp_prog._link]  # da assoc. 'imp_prog' [0..*], certamente non noti alla nascita

    def __init__(self, nome:str, budget:Importo) -> None:
        self.set_nome(nome)
        self.set_budget(budget)
        self._coinvolti = dict()

    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome

    def set_budget(self, budget:Importo) -> None:
        self._budget = budget

    def budget(self) -> Importo:
        return self._budget

    def coinvolti(self) -> frozenset[imp_prog._link]:
        return frozenset(self._coinvolti.values())

    def is_coinvolto(self, impiegato: Impiegato) -> bool:
        return impiegato in self._coinvolti

    def __contains__(self, item: Any) -> bool:
        if not isinstance(item, Impiegato):
            return False
        return self.is_coinvolto(item)

    def get_link_imp_prog(self, impiegato: Impiegato) -> imp_prog._link:
        if impiegato not in self: # oppure not self.is_coinvolto(impiegato)
            raise KeyError(f"{impiegato.nome()} {impiegato.cognome()} non è coinvolto nel progetto")
        return self._coinvolti[impiegato]

    '''def is_coinvolto_brutto(self, impiegato: Impiegato) -> bool:
        # Funziona perché abbiamo implementato hash e eq di _imp_prog
        l: _imp_prog = _imp_prog(self, impiegato, date.today())
        return l in self._coinvolti'''

    def _add_link_imp_prog(self, l: imp_prog._link) -> None:
        if l.progetto() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.impiegato() in self._coinvolti:
            raise KeyError("Il progetto coinvolge già l'impiegato!")
        self._coinvolti[l.impiegato()] = l

    def _remove_link_imp_prog(self, l: imp_prog._link) -> None:
        if l.progetto() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.impiegato() not in self._coinvolti:
            raise KeyError("L'impiegato non lavorava in questo progetto")
        del self._coinvolti[l.impiegato()]


    def data_coinvolgimento(self, impiegato: Impiegato) -> date:
        try:
            return self._coinvolti[impiegato].data()
        except KeyError:
            raise KeyError("Il progetto non coinvolge l'impiegato!")

    def ultimo_impiegato_coinvolto(self) -> Impiegato:
        if not self.coinvolti():
            raise RuntimeError(f"Il progetto {self.nome()} non ha impiegati coinvolti!")

        date_coinvolgimento: set[date] = set()
        for l in self._coinvolti.values():
            date_coinvolgimento.add(l.data())
        # oppure, usando la list comprehension, date_coinvolgimento = set([l.data() for l in self._coinvolti.values()])
        ultima_data: date = max(date_coinvolgimento)

        for imp in self._coinvolti:
            if self.data_coinvolgimento(imp) == ultima_data:
                return imp

    # alternativa con cui l'IDE non si lamenta del tipo di ritorno
    def ultimo(self) -> Impiegato:
        ultimo_imp: Impiegato | None = None
        ultima_data: date | None = None
        if not self.coinvolti(): raise RuntimeError()

        for imp, link in self._coinvolti.items():
            if not ultima_data or link.data() > ultima_data:
                ultimo_imp = imp
                ultima_data = link.data()

        return ultimo_imp

        # Non arriverò mai qui, perché esiste sempre un impiegato con l'ultima data


class imp_prog:

    @classmethod
    def add_link(cls, progetto: Progetto, impiegato: Impiegato, data: date) -> _link:
        l = cls._link(progetto, impiegato, data)
        progetto._add_link_imp_prog(l)
        impiegato._add_link_imp_prog(l)
        return l
    
    @classmethod
    def add_link_oggi(cls, progetto: Progetto, impiegato: Impiegato, data: date) -> _link:
        cls.add_link(progetto, impiegato, date.today())

    @classmethod
    def remove_link(cls, l: _link) -> None:
        l.progetto()._remove_link_imp_prog(l)
        l.impiegato()._remove_link_imp_prog(l)
        del l

    @classmethod
    def remove(cls, progetto: Progetto, impiegato: Impiegato) -> None:
        l: imp_prog._link = progetto.get_link_imp_prog(impiegato)
        cls.remove_link(l)

    class _link:
        _progetto: Progetto     # ovviamente immutabile e noto alla nascita
        _impiegato: Impiegato   # ovviamente immutabile e noto alla nascita
        _data: date             # immutabile e noto alla nascita

        def __init__(self, progetto: Progetto, impiegato:Impiegato, data:date) -> None:
            self._progetto = progetto
            self._impiegato = impiegato
            self._data = data

        def progetto(self) -> Progetto:
            return self._progetto

        def impiegato(self) -> Impiegato:
            return self._impiegato

        def data(self) -> date:
            return self._data

        def __hash__(self) -> int:
            return hash((self.progetto(), self.impiegato()))

        def __eq__(self, other: Any) -> bool:
            if type(self) != type(other) \
                    or hash(self) != hash(other):
                return False
            return (self.progetto(), self.impiegato()) == (other.progetto(), other.impiegato())
            # ignoro la data, perché due link sono lo stesso link se e solo se coinvolgono
            # la stessa coppia di oggetti, indipendentemente dai valori degli attributi dell'associazione
