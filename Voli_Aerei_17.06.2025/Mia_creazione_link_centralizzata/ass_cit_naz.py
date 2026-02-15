from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from class_luoghi import Citta, Nazione

#from class_luoghi import *

class cit_naz:

    @classmethod
    def crea_link_cit_naz(cls, citta: Citta, nazione: Nazione) -> cit_naz._link:
        '''responsabile di creazione link cit_naz '''
        vecchio_link: cit_naz._link = citta.get_link_cit_naz()
        if vecchio_link:
            if vecchio_link.get_nazione() == nazione:
                raise ValueError("Il link esiste già tra questa citta e nazione")
            cls._remove_link_cit_naz(vecchio_link)
        link: cit_naz._link = cls._link(citta, nazione)
        citta._aggiorna_link_cit_naz(link)
        nazione._aggiorna_link_elenco_citta(link)
        return link
    
    @classmethod
    def _remove_link_cit_naz(cls, link: cit_naz._link) -> None:
        link.get_nazione()._remove_link_elenco_citta(link)
        link.get_citta()._remove_link_cit_naz(link)
        del link

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