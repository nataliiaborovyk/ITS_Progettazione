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
    _elenco_progetti: dict[Progetto, imp_prog._link]

    def __init__(self, nome:str, cognome:str, nascita:date, stipendio:Importo,
                 dipartimento_aff: Dipartimento | None = None, data_afferenza: date | None=None) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        self._elenco_progetti: dict[Progetto, imp_prog._link] = {}

        #self._afferenza = None
        self.set_link_afferenza(dipartimento_aff, data_afferenza)

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

# colegamento con Progetti

    def is_coinvolto(self, progetto:Progetto) -> bool:
        return progetto in self._elenco_progetti
    
    def __contains__(self, item:Any) -> bool:
        if not isinstance(item, Progetto):
            return False
        return self.is_coinvolto(item)

    def get_elenco_progetti(self) -> frozenset[imp_prog._link]:
        return frozenset(self._elenco_progetti.values())
    
    def get_link_progetto(self, progetto: Progetto) -> imp_prog._link:
        if progetto not in self._elenco_progetti:
            raise KeyError("Impiegato non lavora al progetto")
        return self._elenco_progetti[progetto]
            
    # serve solo per Progetto nella fase di creazione di link        
    def _aggiorna_link_imp_prog_nel_elenco_imp(self, link: imp_prog._link) -> None:
        if link.get_progetto() in self._elenco_progetti:
            raise ValueError(f"{link.get_impiegato().get_nome()} gia lavora al {self.get_nome()}")
        self._elenco_progetti[link.get_progetto()] = link

    #serve solo a Progetto per dire a Impiegato di eliminare il link nel suo dizionario  
    def _remove_link(self, link: imp_prog._link) -> None:
        if not isinstance(link, imp_prog._link):
            raise ValueError("Errore, argomento di tipo sbagliato")
        if link != self.get_link_progetto(link.get_progetto()):
            raise ValueError("il link non corisponde")
        if link not in self._elenco_progetti.values(): 
            raise ValueError(f"{link.get_impiegato()} non lavora al progetto {self.get_nome()}")     
        # if link.get_impiegato() is not self:              #  "is" non è la stessa cosa che "=="
        #     raise ValueError("il link non appartiene a questo impegato")  
        del self._elenco_progetti[link.get_progetto()]

#collegamento con la classe Dipartimento

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

    def __str__(self) -> str:
        if self._afferenza:
            dip:str = self._afferenza.get_dipartimento().get_nome()
            data:date = self._afferenza.get_data_afferenza()
            afferenza: str = f"che afferisce al dip. {dip} dal {data}" 
        else:
            afferenza = ""
        progetti = ", ".join(prog.get_nome() for prog in self._elenco_progetti) or "nessun progetto"
        return f"Impiegato {self.get_nome()} {self.get_cognome()} {afferenza}\nProgetti:{progetti}"


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
    
    def __repr__(self):
        return str(self)


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
    #_coinvolti_impiegati: set[_imp_prog]      non piu
    _coinvolti_impiegati: dict[Impiegato, imp_prog._link]

    def __init__(self, nome:str, budget:Importo) -> None:
        self.set_nome(nome)
        self.set_budget(budget)
        self._coinvolti_impiegati: dict[Impiegato, imp_prog._link] = {}

    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def get_nome(self) -> str:
        return self._nome

    def set_budget(self, budget:Importo) -> None:
        self._budget = budget

    def get_budget(self) -> Importo:
        return self._budget
    
    def is_coinvolto(self, impiegato:Impiegato) -> bool: #bello ma cattivo
        return impiegato in self._coinvolti_impiegati  #cerchiamo la chiave
    
                            #      (quando self._coinvolti_impiegati era set di link)
                            # for i in self._coinvolti_impiegati:
                            #     if i.get_impiegato() == impiegato:
                            #         return True
                            # return False
        
    def __contains__(self, item: Any) -> bool:
        if not isinstance(item, Impiegato):
            return False
        return self.is_coinvolto(item)          # ???????????

                            #      (quando self._coinvolti_impiegati era set di link)
                            # def is_coinvolto_brutto(self, impiegato:Impiegato) -> bool: #brutto ma buono
                            #     link: _imp_prog = _imp_prog(self, impiegato, None)        # (alternativa)
                            #     if link in self._coinvolti_impiegati:                               # return link in self._coinvolti_impiegati 
                            #         return True              
                            #     return False
    
    def data_coinvolgimento(self, impiegato:Impiegato) -> date:
        try:
            return self._coinvolti_impiegati[impiegato].get_data()
        except KeyError:
            raise KeyError("il progetto non contiene impiegato")
        
    def ultimo_impiegato_coinvolto(self) -> Impiegato:
        if not self._coinvolti_impiegati:
            raise RuntimeError(f" il progetto {self.get_nome()} non ha impiegati coinvolti")
        date_coinvolgimento:set[date] = set()
        for i in self._coinvolti_impiegati.values():
            date_coinvolgimento.add(i.get_data())
        #date_coinvolgimento = set([i.get_data() for i in self._coinvolti_impiegati.values()])
        ultima_data: date = max(date_coinvolgimento)
        for impiegato in self._coinvolti_impiegati:
            if self.data_coinvolgimento(impiegato) == ultima_data:   # ????????????????
                return impiegato
            
        #alternativa
    def ultimo(self) -> Impiegato:
        ultimo_imp: Impiegato | None
        ultima_data: date | None
        if not self.get_coinvolti_impiegati(): 
            raise RuntimeError()

        for impiegato, link in self._coinvolti_impiegati.items():
            if not ultima_data or link.get_data() > ultima_data:
                ultimo_imp = impiegato
                ultima_data = link.get_data()
            
        return ultimo_imp

    def get_coinvolti_impiegati(self) -> frozenset[imp_prog._link]:
        return frozenset(self._coinvolti_impiegati.values())
            
    def get_link_impiegato(self, impiegato:Impiegato) -> imp_prog._link:
        if impiegato not in self._coinvolti_impiegati:
            raise KeyError(f"Impiegato {impiegato.get_nome()} non è coinvolto nel {self.get_nome()}")
        return self._coinvolti_impiegati[impiegato]

    # serve solo per Impiegato nella fase di creazione di link      
    def _aggiorna_link_imp_prog_nel_coinvolti_impiegati(self, link: imp_prog._link) -> None:
        # TODO controllo che l'impiegato non ci sia già
        if link._impiegato in self._coinvolti_impiegati:
            raise ValueError(f"{link.get_impiegato().get_nome()} gia lavora al {self.get_nome()}")
        self._coinvolti_impiegati[link._impiegato] = link

    #serve solo a Impiegato per dire a Progetto di eliminare il link nel suo dizionario       
    def _remove_link_imp_prog(self, link: imp_prog._link) -> None:
        if not isinstance(link, imp_prog._link):
            raise ValueError("Errore, argomento di tipo sbagliato")
        if link.get_progetto() is not self:
            raise ValueError("il link non appartiene a questo progetto")
        if link != self.get_link_impiegato(link.get_impiegato()):
            raise ValueError("il link non corisponde")
        # if link not in self._coinvolti_impiegati.values():
        #     raise ValueError(f"{link.get_impiegato()} non lavora al progetto {self.get_nome()}")
        del self._coinvolti_impiegati[link.get_impiegato()]

    def __str__(self) -> str:
        coinvolti = ", ".join(imp.get_nome() for imp in self._coinvolti_impiegati) or "nessun impiegato"
        return f"Progetto: {self._nome}\nBudget: {self._budget}\nCoinvolti: {coinvolti}"   

    def __repr__(self):
        return str(self)
    

class imp_prog:

    @classmethod
    def add_link(cls, progetto:Progetto, impiegato:Impiegato, data:date) -> imp_prog._link:
        link: imp_prog._link = cls._link(progetto, impiegato, data)
        impiegato._aggiorna_link_imp_prog_nel_elenco_imp(link)
        progetto._aggiorna_link_imp_prog_nel_coinvolti_impiegati(link)
        return link

    @classmethod
    def remove_link(cls, link: imp_prog._link) -> None:
        link.get_impiegato()._remove_link(link)
        link.get_progetto()._remove_link_imp_prog(link)
        del link

    @classmethod
    def remove(cls, progetto:Progetto, impiegato:Impiegato) -> None:
        link:imp_prog._link = impiegato.get_link_progetto(progetto)
        #link:imp_prog._link = progetto.get_link_impiegato(impiegato)  #  alternativa
        cls.remove_link(link)


    class _link:
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
        
        def __str__(self) -> str:
            return f"\n{self._impiegato.get_nome()} lavora in {self._progetto.get_nome()} dal {self._data}"
        
        def __repr__(self) -> str:
            return str(self)