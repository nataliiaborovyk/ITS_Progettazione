from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from class_volo import Volo

from class_aeroporto import Aeroporto
# from class_volo import Volo

class partenza:

    @classmethod
    def crea_link_partenza(cls, volo:Volo, aeroporto:Aeroporto) -> None:
        '''responsabile di creazione link partenza '''
        vecchio_link = volo.get_link_partenza()
        if vecchio_link:
            if vecchio_link.get_aeroporto() == aeroporto:
                raise ValueError("Il link esiste già tra questo volo e la compagnia.")
        link: partenza._link = cls._link(volo, aeroporto)
        volo._aggiorna_link_partenza(link)
        aeroporto._aggiorna_elenco_voli_partenza(link)

# link è immutabile

    class _link:

        _aeroporto: Aeroporto
        _volo: Volo

        def __init__(self, volo:Volo, aeroporto:Aeroporto) -> None:
            self._aeroporto = aeroporto
            self._volo = volo

        def get_aeroporto(self) -> Aeroporto:
            return self._aeroporto

        def get_volo(self) -> Volo:
            return self._volo
        
        def __str__(self) -> str:
            return f"partenza (Aeroporto: {self.get_aeroporto()} - Volo: {self.get_volo()})"
        
        def __repr__(self) -> str:
            return f"partenza({self.get_aeroporto()} - {self.get_volo()})"