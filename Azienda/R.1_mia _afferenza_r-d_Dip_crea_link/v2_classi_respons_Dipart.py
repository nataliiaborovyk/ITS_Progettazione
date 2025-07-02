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
    _elenco_progetti: dict[Progetto, date]

    def __init__(self, nome:str, cognome:str, nascita:date, stipendio:Importo,
                 dipartimento_aff: Dipartimento | None = None, data_afferenza: date | None=None) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        #self._elenco_progetti: dict[Progetto, _imp_prog] = {}

        #self._afferenza = None
        self.set_link_afferenza(dipartimento_aff, data_afferenza)

# colegamento con Progetti
    def get_elenco_progetti(self) -> frozenset[_imp_prog]:
        return frozenset(self._elenco_progetti.values())
    
    def is_coinvolto(self, progetto:Progetto) -> bool:
        return progetto in self._elenco_progetti
    
    def __contains__(self, item:Any) -> bool:
        if not isinstance(item, Progetto):
            return False
        return self.is_coinvolto(item)
    
    def add_progetto(self, progetto:Progetto, data:date) -> None:
        if progetto in self._elenco_progetti:
            raise KeyError("L'impiegato è gia coinvolto nel progetto")
        link: _imp_prog = _imp_prog(progetto, self, data)
        self._elenco_progetti[progetto] = link
        progetto._add_link_coinvolto(link)


    def add_progetto_oggi(self,  progetto:Progetto) -> None:
        self.add_progetto(progetto, date.today())

    def remove_progetto(self, progetto:Progetto) -> None:
        try:
            del self._elenco_progetti[progetto]
            del progetto._coinvolti[self]
        except KeyError:
            raise KeyError("L'impiegato non lavora al progetto")

#collegamento con la classe Dipsrtimento
    def set_link_afferenza(self, dipartimento_aff: Dipartimento | None = None, data_afferenza:date | None = None) -> None:
        
        # caso di errore
        if (dipartimento_aff is None) != (data_afferenza is None):
            raise ValueError("dipartimento e data di afferenza devono essere entrambi None o entrambi non None")
        
        # rimuovo link vechio, se non esiste: pass
        try:
            if self.get_link_afferenza():
                self.remove_link_afferenza()
        except AttributeError: # nel caso che attributo _afferenza on era mai stato settato
            pass
        
        # creo link afferenza
        if dipartimento_aff: # sono entrambi not None
            self._afferenza = dipartimento_aff.creaLinkAfferenza(self, data_afferenza)
        
        # altrimenti link non esiste
        else:
            self._afferenza = None

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
        
        #se link non esiste get_link_afferenza non crea problemi, se esiste lo elimino per sostituire
        try:
            if impiegato.get_link_afferenza():
                impiegato.get_link_afferenza().get_dipartimento()._remove_link_impiegato(impiegato.get_link_afferenza())
        except AttributeError:
            pass

        #creo link
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
    #_coinvolti: set[_imp_prog]      non piu
    _coinvolti: dict[Impiegato, _imp_prog]

    def __init__(self, nome:str, budget:Importo) -> None:
        self.set_nome(nome)
        self.set_budget(budget)
        self._coinvolti: dict[Impiegato, _imp_prog] = {}

    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def get_nome(self) -> str:
        return self._nome

    def set_budget(self, budget:Importo) -> None:
        self._budget = budget

    def get_budget(self) -> Importo:
        return self._budget
    
    def get_coinvolti(self) -> frozenset[_imp_prog]:
        return frozenset(self._coinvolti.values())
    
    def is_coinvolto(self, impiegato:Impiegato) -> bool: #bello ma cattivo
        return impiegato in self._coinvolti  #cerchiamo la chiave
    
                            #      (quando self._coinvolti era set di link)
                            # for i in self._coinvolti:
                            #     if i.get_impiegato() == impiegato:
                            #         return True
                            # return False
        
    
    def __contains__(self, item: Any) -> bool:
        if not isinstance(item, Impiegato):
            return False
        return self.is_coinvolto(item)          # ???????????

                            #      (quando self._coinvolti era set di link)
                            # def is_coinvolto_brutto(self, impiegato:Impiegato) -> bool: #brutto ma buono
                            #     link: _imp_prog = _imp_prog(self, impiegato, None)        # (alternativa)
                            #     if link in self._coinvolti:                               # return link in self._coinvolti 
                            #         return True              
                            #     return False
    
    def data_coinvolgimento(self, impiegato:Impiegato) -> date:
        try:
            return self._coinvolti[impiegato].get_data()
        except KeyError:
            raise KeyError("il progetto non contiene impiegato")
        
    def ultimo_impiegato_coinvolto(self) -> Impiegato:
        if not self._coinvolti:
            raise RuntimeError(f" il progetto {self.get_nome()} non ha impiegati coinvolti")
        date_coinvolgimento:set[date] = set()
        for i in self._coinvolti.values():
            date_coinvolgimento.add(i.get_data())
        #date_coinvolgimento = set([i.get_data() for i in self._coinvolti.values()])
        ultima_data: date = max(date_coinvolgimento)
        for impiegato in self._coinvolti:
            if self.data_coinvolgimento(impiegato) == ultima_data:   # ????????????????
                return impiegato
            
    def _add_link_coinvolto(self, l: _imp_prog) -> None:
        # TODO controllo che l'impiegato non ci sia già
        self._coinvolti[l._impiegato] = l
            

        #alternativa
    def ultimo(self) -> Impiegato:
        ultimo_imp: Impiegato | None
        ultima_data: date | None
        if not self.get_coinvolti(): 
            raise RuntimeError()

        for impiegato, link in self._coinvolti.items():
            if not ultima_data or link.get_data() > ultima_data:
                ultimo_imp = impiegato
                ultima_data = link.get_data()
            
        return ultimo_imp


    def add_impiegato(self, impiegato:Impiegato, data:date) -> None:
        if impiegato in self._coinvolti:
            raise KeyError("Il progetto coinvoge gia impiegato")
        link: _imp_prog = _imp_prog(self, impiegato, data)
        self._coinvolti[impiegato] = link
        #impiegato._elenco_progetti[self] = link

    def add_impiegato_oggi(self, impiegato: Impiegato) -> None:
        self.add_impiegato(impiegato, date.today())

    def remove_impiegato(self, impiegato:Impiegato) -> None:
        try:
            del self._coinvolti[impiegato]
            #del impiegato._elenco_progetti[self]
        except KeyError:
            raise KeyError("Il progetto con contiene impiegato")
        #        alternativa
        # if not impiegato in self._coinvolti:
        #     raise KeyError("Il progetto con contiene impiegato")
        # del self._coinvolti[impiegato]


class _imp_prog:
    _progetto: Progetto   #ovviamente immutabile / noto alla nascita
    _impiegato: Impiegato    #ovviamente immutabile / noto alla nascita
    _data: date       # immutabile / noto alla nascita


    def __init__(self, progetto: Progetto, impiegato: Impiegato, data:date) -> None:
        self._progetto = progetto
        self._impiegato = impiegato
        self._data = data

    def get_progetto(self) -> Progetto:
        return self._progetto
    
    def get_impiegato(self) -> Impiegato:
        return self._impiegato
    
    def get_data(self) -> date:
        return self._data
    
    def __hash__(self) -> int:
        return hash((self.get_progetto(), self.get_impiegato()))
    
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False
        return self.get_progetto() == other.get_progetto() and self.get_impiegato() == other.get_impiegato() #ignoro la data
        #return (self.get_progetto(), self.get_impiegato) == (other.get_progetto(), other.get_impiegato())     
    