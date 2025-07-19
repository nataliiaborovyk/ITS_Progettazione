from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any

if TYPE_CHECKING:
    from class_Bid import Bid
    from class_Privato import Privato

class bid_ut:

    class _link:

        _bid: Bid
        _utente: Privato

        def __init__(self, bid: Bid, utente: Privato) -> None:
            self._bid = bid
            self._utente = utente

        def get_bid(self) -> Bid:
            return self._bid
        
        def get_utente(self) -> Privato:
            return self._utente
        
        def __hash__(self) -> int:
            return hash((self.get_bid(), self.get_utente()))
        
        def __eq__(self, other: Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            return self.get_bid() == other.get_bid and self.get_utente() == other.get_utente()
        
        
        def __str__(self) -> str:
            return f"Utente {self.get_utente()} ha fatto il bid"
        
        def __repr__(self) -> str:
            return f"bit_ut({self.get_bid()} - {self.get_utente()})"