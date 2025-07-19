
from datetime import datetime

from class_Asta import Asta
from class_Privato import Privato
from ass_asta_bid import asta_bid
from ass_bid_ut import bid_ut

class Bid:

    _istante: datetime # <<imm>> / noto alla nascita
    _link_asta_bid: asta_bid._link # <<imm>> / noto alla nascita
    _link_bid_ut: bid_ut._link # <<imm>> / noto alla nascita

    _elenco_istanti: set[tuple[int, datetime]] = set()

    @classmethod
    def _controllo_se_esist_bid_con_istante_verso_asta(cls, asta: Asta, istante:datetime ) -> bool:
        if (asta.get_id(), istante) in cls._elenco_istanti:
            return True
        else: 
            return False

    def __init__(self, asta: Asta, utente: Privato) -> None:
        self._istante = datetime.now()
        self._link_asta_bid = None # per evitare attributeError 
        self._crea_link_asta_bid(asta)
        self._link_bid_ut = None   # per evitare attributeError 
        self._crea_link_bid_ut(utente)

    def get_istante(self) -> datetime:
        return self._istante

#collegamento con classe Asta, associzione - asta_bid

    def get_link_asta_bid(self) -> asta_bid._link:
        return self._link_asta_bid

    def _crea_link_asta_bid(self, asta: Asta) -> None:
        if self.get_link_asta_bid() is not None:
            raise ValueError("Non si puo modificare link verso asta")
        if self._controllo_se_esist_bid_con_istante_verso_asta(asta, self.get_istante()):
            raise ValueError(f"Esiste gia un bid con istante identico verso asta {asta.get_id()}")
        link: asta_bid._link = asta_bid._link(asta, self)
        self._link_asta_bid = link
        asta._aggiorna_elenco_link_asta_bid(link)
        Bid._elenco_istanti.add((asta.get_id(), self.get_istante()))
    

#collegamento con classe Privato, associzione - bid_ut

    def get_link_bid_ut(self) -> bid_ut._link:
        return self._link_bid_ut
    
    def _crea_link_bid_ut(self, utente: Privato):
        if self.get_link_bid_ut() is not None:
            raise ValueError("Non si puo modificare utente")
        link: bid_ut._link = bid_ut._link(self, utente)
        self._link_bid_ut = link
        utente._aggiorna_elenco_link_bid_ut(link)
        
        
    
    def __str__(self) -> str:
        istante: datetime = self.get_istante().strftime("%Y-%m-%d %H:%M")
        return f"\tIstante di bid: {istante}\n\
            fatto da utente: {self.get_link_bid_ut().get_utente().get_username()}\n\
            verso asta: {self.get_link_asta_bid().get_asta().get_id()}"
    
    def __repr__(self) -> str:
        username_utente: str = self.get_link_bid_ut().get_utente().get_username()
        id_asta: int = self.get_link_asta_bid().get_asta().get_id()
        return f"Bid({username_utente}, {id_asta})"
