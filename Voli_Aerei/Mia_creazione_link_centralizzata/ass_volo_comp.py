from __future__ import annotations
from typing import TYPE_CHECKING
from typing import Any

if TYPE_CHECKING:
    from class_volo import Volo
    from class_compagnia import CompagniaAerea

# from class_volo import Volo
# from class_compagnia import CompagniaAerea

class volo_comp:

    @classmethod
    def crea_link_volo_comp(cls, volo: Volo, compania: CompagniaAerea) -> None:
        '''responsabile di creazione link volo_comp'''
        vecchio_link: volo_comp._link = volo.get_link_volo_comp()
        if vecchio_link:
            if vecchio_link.get_compania() == compania:
                raise ValueError("Il link esiste già tra questo volo e compania aerea.")
        #     cls._remove_link_volo_comp(vecchio_link)
        link: volo_comp._link = cls._link(volo, compania)
        volo._aggiorna_link_volo_comp(link)
        compania._aggiorna_elenco_voli(link)

# link è immutabile
    # @classmethod
    # def _remove_link_volo_comp(cls, link:volo_comp._link) -> None:
    #     link.get_volo()._remove_link_volo_comp(link)
    #     link.get_compania()._remove_link_volo_comp(link)

    class _link:

        _volo: Volo
        _compania: CompagniaAerea

        def __init__(self, volo:Volo, compania:CompagniaAerea) -> None:
            self._volo = volo
            self._compania = compania

        def get_volo(self) -> Volo:
            return self._volo
        
        def get_compania(self) -> CompagniaAerea:
            return self._compania
        
        def __hash__(self) -> int:
            return hash((self.get_compania(), self.get_volo()))

        def __eq__(self, other:Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            return self.get_compania() == other.get_compania() and self.get_volo() == other.get_volo()

        def __str__(self) -> str:
            return f"volo_comp (Volo: {self.get_volo()} - Compania Aerea: {self.get_compania()})"
        
        def __repr__(self) -> str:
            return f"volo_comp({self.get_volo()} - {self.get_compania()})"
        
