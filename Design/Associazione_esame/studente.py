from __future__ import annotations

from esame import *
from modulo import Modulo

class Studente:
    _nome: str
    _esami: dict[Modulo, esame._link]  # mutabile, non noto alla nascita

    def __init__(self, nome:str) -> None:
        self._nome = nome
        self._esami = dict()

    def nome(self) -> str:
        return self._nome
    
    def esami(self) -> frozenset[esame._link]:
        return frozenset(self._esami.values())
    
    def add_esame(self, modulo: Modulo, voto: int) -> None:
        if modulo in self._esami:
            raise ValueError(f"Lo studente aveva gia superato l'esame del modulo {modulo}")
        l: esame._link = esame._link(self, modulo, voto)
        self._esami[modulo] = l


if __name__ == "__main__":

    from studente import Studente

    a: 'Studente' = Studente("Alice")
    p1: Modulo = Modulo("Prog.1")
    p2: Modulo = Modulo("Prog.2")
    #ap1: esame._link = esame._link(a, p1, 29)

    # print(ap1.studente().nome())
    # print(ap1.modulo().codice())
    # print(a.esami())
    a.add_esame(p1,19)
    a.add_esame(p2,18)
    print(a.esami())
    print(a._esami)
    print(a._esami[p2])

    esame_ap2 = a._esami[p2]
    print(esame_ap2.studente().nome())
    print(esame_ap2.modulo().codice())
    print(a.esami())
    