from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from class_Bid import Bid

from datetime import datetime
from tipoDato_FloatGez import FloatGez
from tipoDato_IntGEZ import IntGEZ
from tipoDato_Condizioni import Condizioni
from typing import Optional

from ass_asta_bid import asta_bid

from class_PostOggetto import PostOggetto
from class_Utente import Utente


class Asta(PostOggetto):

    _prezzo_bid: FloatGez 
    _scadenza: datetime | str
    _elenco_link_asta_bid: set[asta_bid._link]


    def __init__(self, *, 
                descrizione:str, 
                prezzo:FloatGez, 
                anni_garanzia:IntGEZ,
                prezzo_bid: FloatGez,
                scadenza: datetime | str, 
                condizioni: Condizioni | None = None ) -> None:

        self._elenco_link_asta_bid = set() # bisogna definire prima per evitare AttributeError nel _puo_cambiare()
        self.set_prezzo_bid(prezzo_bid)
        self.set_scadenza(scadenza)
        super().__init__(
                        descrizione=descrizione,
                        prezzo=prezzo,
                        anni_garanzia=anni_garanzia,
                        condizioni=condizioni) 

    #abstractmethod da PostOgetto
    def _puo_cambiare(self) -> bool: # serve per controllare se esiste almeno un bid
        if self._elenco_link_asta_bid:
            return False
        else:
            return True
        
    def _controllo_se_si_puo_cambiare(self, che_cosa: str) -> None:  #per non ripetere codice
        if self._puo_cambiare() == False:
            raise ValueError(f"Non si puo modificare {che_cosa} dopo il primo bid")

    def set_descrizione(self, descrizione: str) -> None:
        self._controllo_se_si_puo_cambiare("la descrizione")
        super().set_descrizione(descrizione)

    def set_prezzo(self, prezzo: FloatGez) -> None:
        self._controllo_se_si_puo_cambiare("il prezzo iniziale")
        super().set_prezzo(prezzo)

    def _set_condizioni(self, condizioni: Condizioni) -> None:
        self._controllo_se_si_puo_cambiare("le condizioni")
        super()._set_condizioni(condizioni)

    #abstractmethod da PostOgetto
    def get_tipoPostOggetto(self) -> str: 
        return f"Asta"

    def set_prezzo_bid(self, prezzo_bid: FloatGez) -> None:
        self._controllo_se_si_puo_cambiare("il prezzo di rialzo")
        self._prezzo_bid = prezzo_bid

    def set_scadenza(self, scadenza: datetime | str) -> None:
        self._controllo_se_si_puo_cambiare("la scadenza")
        if isinstance(scadenza, str):
            scadenza = datetime.strptime(scadenza, "%d-%m-%Y %H:%M")  #trasformo stringa in datetime formattato
        self._scadenza = scadenza

    def get_prezzo_bid(self) -> FloatGez:
        return self._prezzo_bid
    
    def get_scadenza(self) -> datetime:
        return self._scadenza
    
    # eredita altri metodi get da PostOggetto
    
 # Operazioni di classe

    def prezzo(self, i: datetime) -> FloatGez:
        cont:int = 0
        for l in self._elenco_link_asta_bid:
            if l.get_bid().get_istante() <= i:
                cont += 1
        return cont * self.get_prezzo_bid() + self.get_prezzo()
    
    def ultimo_bid(self, i: datetime) -> Bid | None:
        
        ultimo_link: asta_bid._link | None = None   
        for l in self._elenco_link_asta_bid:
            if l.get_bid().get_istante() <= i:
                if ultimo_link is None or ultimo_link.get_bid().get_istante() < l.get_bid().get_istante():
                    ultimo_link = l
        return None if ultimo_link is None else ultimo_link.get_bid()
        
    def _conclusa(self) -> bool:
        if self.get_scadenza() <= datetime.now():
            return True
        return False

    def vincitore(self) -> Utente | None:
        if self._conclusa() == True:
            bid: Bid = self.ultimo_bid(datetime.now())
            if bid is not None:  # per evitare attribut error
                return bid.get_link_bid_ut().get_utente()
        return None

# collegamento con classe Bid, assiociazione - asta_bid

    def get_elenco_link_asta_bid(self) -> frozenset[asta_bid._link]:
        return frozenset(self._elenco_link_asta_bid)
    
    def get_tutti_bid(self) -> frozenset[Bid]:
        return frozenset({l.get_bid() for l in self._elenco_link_asta_bid})  
    
    def _aggiorna_elenco_link_asta_bid(self, link: asta_bid._link) -> None:
        if link.get_asta() != self:
            raise ValueError(f"Il link fornito non riguarda asta {self.get_id()}")
        if link in self._elenco_link_asta_bid:
            raise ValueError("Errore, il link gia esiste")
        self._elenco_link_asta_bid.add(link)



    def __str__(self) -> str:
        base = super().__str__() # str della superclasse PostOggetto
        da_asta: str = f"prezzo bid: {self.get_prezzo_bid()}\nscadenza: {self.get_scadenza().strftime('%Y-%m-%d %H:%M')}\n"
        return base + da_asta
        

