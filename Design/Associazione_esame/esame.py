from __future__ import annotations

#from studente import Studente
from modulo import Modulo

class esame:

    class _link:

        _studente: 'Studente'
        _modulo: Modulo
        _voto: int

        def __init__(self, studente:'Studente', modulo:Modulo, voto: int) -> None:
            self._studente = studente
            self._modulo = modulo
            self._voto = voto

        def studente(self) -> 'Studente':
            return self._studente
        
        def modulo(self) -> Modulo:
            return self._modulo
    

if __name__ == "__main__":

    from studente import Studente

    a: 'Studente' = Studente("Alice")
    p1: Modulo = Modulo("Progettazione")
    p2: Modulo = Modulo("Prog.1")
    ap1: esame._link = esame._link(a, p1, 29)

    print(ap1.studente().nome())
    print(ap1.modulo().codice())
    print(a.esami())

    a.add_esame(p2,18)
    print(a.esami())
    print(a._esami)
    print(a._esami[p2])

    esame_ap2 = a._esami[p2]
    print(esame_ap2.studente().nome())
    print(esame_ap2.modulo().codice())
    print(a.esami())


    