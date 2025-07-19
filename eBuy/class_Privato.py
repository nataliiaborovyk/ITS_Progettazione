from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ass_bid_ut import bid_ut

from class_Utente import Utente
from datetime import datetime

class Privato(Utente):

    _username:str
    _registrazione: datetime
    _elenco_link_bid_ut: set[bid_ut._link] # non noto alla nascita

    def __init__(self, username:str) -> None:
        super().__init__(username)
        self._elenco_link_bid_ut = set()

    #abstractmethod da Utente
    def get_tipo_utente(self):     
        return "Utente privato"
    
#collegamento con class Bid, associazione - bid_ut

    def get_elenco_link_bid_ut(self) -> frozenset[bid_ut._link]:
        return frozenset(self._elenco_link_bid_ut)
    
    def _aggiorna_elenco_link_bid_ut(self, link: bid_ut._link) -> None:
        if link.get_utente() != self:
            raise ValueError(f"il link non riguarda utente {self.get_username()} ")
        if link in self._elenco_link_bid_ut:
            raise ValueError("Il link è gia nel elenco")
        self._elenco_link_bid_ut.add(link)


# eredita metodi get e str da Utente