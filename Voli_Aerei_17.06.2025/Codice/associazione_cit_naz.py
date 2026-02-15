from __future__ import annotations
from tipoDato_intGEZ import IntGEZ   #quando manca il modulo è 'giallo'

#from assoc_class_citta import Citta
#from assoc_class_nazione import Nazione


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
            return f"Link(Citta: {self._citta.get_nome()} - Nazione: {self._nazione.get_nome()})"
        
        def __repr__(self) -> str:
            return F"cit_naz._link({self._citta.get_nome()}, {self._nazione.get_nome()})"
        
if __name__ == "__main__":
     
     from assoc_class_citta import Citta
     from assoc_class_nazione import Nazione
     

     n1: Nazione = Nazione("italia")
     c1: Citta = Citta("Roma", IntGEZ(2746789), n1)
     c2: Citta = Citta("Orte", IntGEZ(9000), n1)
     print(c1.cit_naz())
     print(c2.cit_naz())
     print(n1.cit_naz())

