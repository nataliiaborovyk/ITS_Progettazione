from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from class_luoghi import Citta, Nazione

#from class_luoghi import *

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
            return f"cit_naz (Citta: {self._citta.get_nome()} - Nazione: {self._nazione.get_nome()})"
        
        def __repr__(self) -> str:
            return F"cit_naz._link({self._citta.get_nome()}, {self._nazione.get_nome()})"