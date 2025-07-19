from __future__ import annotations
from typing import TYPE_CHECKING
from typing import Any


if TYPE_CHECKING:
	from class_Asta import Asta
	from class_Bid import Bid

class asta_bid:
	
    class _link:
          
        _asta: Asta
        _bid: Bid

        def __init__(self, asta: Asta, bid: Bid) -> None:
            self._asta = asta
            self._bid = bid
        
        def get_asta(self) -> Asta:
             return self._asta
        
        def get_bid(self) -> Bid:
             return self._bid
        
        def __hash__(self) -> int:
             return hash((self.get_asta(), self.get_bid()))
        
        def __eq__(self, other: Any) -> bool:
             if type(self) != type(other) or hash(self) != hash(other):
                  return False
             return self.get_asta() == other.get_asta() and self.get_bid() == other.get_bid()
        
        
        def __str__(self) -> str:
             return f"Bid {self.get_bid()} riguarda Asta {self.get_asta()}"
        
        def __repr__(self) -> str:
             return f"asta_bid({self.get_bid()} - {self.get_asta()})"

            
