from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from class_volo import Volo

from class_aeroporto import Aeroporto
# from class_volo import Volo

class arrivo:

    @classmethod
    def crea_link_arrivo(cls, volo:Volo, aeroporto: Aeroporto) -> None:
        '''responsabile di creazione link arrivo '''
        vecchio_link = volo.get_link_arrivo()
        if vecchio_link:
            if vecchio_link.get_aeroporto() == aeroporto:
                raise ValueError("Il link esiste già tra questo volo e la compagnia.")
        link: arrivo._link = cls._link(volo, aeroporto)
        volo._aggiorna_link_arrivo(link)
        aeroporto._aggiorna_elenco_voli_arrivo(link)
        
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
            return f"arivo (Aeroporto: {self.get_aeroporto()} - Volo: {self.get_volo()})"
        
        def __repr__(self) -> str:
            return f"arivo({self.get_aeroporto()} - {self.get_volo()})"