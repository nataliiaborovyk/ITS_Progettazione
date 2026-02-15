from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from class_volo import Volo

from class_aeroporto import Aeroporto
# from class_volo import Volo

class arrivo:

    class _link:

        _aeroporto: Aeroporto
        _volo: Volo

        def __init__(self, aeroporto:Aeroporto, volo:Volo) -> None:
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