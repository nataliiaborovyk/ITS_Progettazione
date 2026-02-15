from __future__ import annotations
from typing import TYPE_CHECKING
from typing import Any


if TYPE_CHECKING:
	from class_aeroporto import Aeroporto
# 	from class_luoghi import Citta

# from class_aeroporto import Aeroporto
from class_luoghi import Citta

class aerop_citta:

    @classmethod
    def crea_link_aerop_citta(cls, aeroporto: Aeroporto, citta: Citta) -> aerop_citta._link:
        '''responsabile di creazione link aerop_citta '''
        vecchio_link: aerop_citta._link = aeroporto.get_link_aerop_citta()
        if vecchio_link:
            if vecchio_link.get_citta() == citta:
                raise ValueError("Il link esiste già tra questo aeroporto e la città.")
            cls._remove_link_aerop_citta(vecchio_link)
        link: aerop_citta._link = cls._link(aeroporto, citta)
        citta._aggiorna_elenco_aeroporti(link)
        aeroporto._aggiorna_link_aerop_citta(link)
        return link
    
    @classmethod
    def _remove_link_aerop_citta(cls, link: aerop_citta._link) -> None:
        link.get_aeroporto()._remove_link_aerop_citta(link)
        link.get_citta()._remove_link_aerop_citta(link)
        del link

    class _link:

        _aeroporto: 'Aeroporto'
        _citta: 'Citta'

        def __init__(self, aeroporto:'Aeroporto', citta:'Citta') -> None:
            self._aeroporto = aeroporto
            self._citta = citta

        def get_aeroporto(self) -> 'Aeroporto':
            return self._aeroporto
        
        def get_citta(self) -> 'Citta':
            return self._citta
        
        def __hash__(self) -> int:
             return hash((self.get_aeroporto(), self.get_citta()))
        
        def __eq__(self, other:Any) -> bool:
             if type(self) != type(other) or hash(self) != hash(other):
                  return False
             return self.get_aeroporto() == other.get_aeroporto() and self.get_citta() == other.get_citta()
        
        def __str__(self) -> str:
            return f"aerop_citta (Aeroporto: {self.get_aeroporto()} - Citta: {self.get_citta()})"
        
        def __repr__(self) -> str:
            return f"aerop_citta({self.get_aeroporto()} - {self.get_citta()})"
    