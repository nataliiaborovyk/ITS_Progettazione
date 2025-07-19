from typing import Any
import re

class CodiceFiscale:
   
    def __init__(self, cf:str) -> None:
       
        if cf is None:
            raise ValueError("Errore, codice fiscale non puo essere None")
        if not isinstance(cf, str):
            raise ValueError("Errore, inserisci codice fiscale in formato stringa ")
        
        cf = cf.upper()
        modello_cf: str = r"^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$"
        if not re.match(modello_cf, cf):
            raise ValueError(f"Errore, il codice fiscale inserito {cf} non è valido, riprova")
        self._cf = cf

    def get_cf(self) -> str:
        return self._cf
    
    def __hash__(self) -> int:
        return hash(self._cf)
    
    def __eq__(self, other:Any) -> bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return self._cf == other._cf
    
    def __str__(self) -> str:
        return self._cf
    
    def __repr__(self) -> str:
        return f"Codice Fiscale = {self.get_cf()}"
    

if __name__ == "__main__":
    cf1:CodiceFiscale = CodiceFiscale("BgkNtl84s69z153K")
    print(cf1)

    # cf2:CodiceFiscale = CodiceFiscale(12121)
    # print(cf2)

    # cf3:CodiceFiscale = CodiceFiscale("BgkNtl84s69z15")
    # print(cf3)

    cf4:CodiceFiscale = CodiceFiscale("bgkntl84s69z153k")
    print(cf4)

    print(cf1 == cf4)

    cf5:CodiceFiscale = CodiceFiscale("BGKNTL84S69Z153K")
    print(cf5)

    cf6:CodiceFiscale = CodiceFiscale("BBBBtl11s11z111K")
    print(cf6)

    cf7:CodiceFiscale = CodiceFiscale("aaaatl22S22Z222M")
    print(cf7)

    elenco_cf:set = {cf1, cf4, cf5, cf6, cf7}
    print(elenco_cf)