from typing import Any
import re

class Indirizzo:
    _via:str
    _civico:int
    _cap:int

    def __init__(self, via:str, civico:str|int, cap:str) -> None:
       
        if via is None:
            raise ValueError("Errore, via non puo essere None")
        if not isinstance(via, str):
            raise ValueError("Errore, inserisci via in formato stringa")
        via = via.title()
        self._via:str = via
       
        if civico is None:
            raise ValueError("Errore, civico non puo essere None")
        civico = str(civico)
        if not re.search("^[0-9]+[a-zA-Z]*$", civico):
            raise ValueError("Errore, scrivi il civico in formato numero con lettera accanto se c'è")
        self._civico:str = civico
       
        if cap is None:
            raise ValueError("Errore, cap non puo essere None")
        if not isinstance(cap, (str)):
            raise ValueError("Errore, inserisci \"cap\" in formato stringa")
        cap = str(cap)
        if not re.search("^[0-9]{5}$", cap):
            raise ValueError("Errore, scrivi cap in formato 5 caretteri numerici")
        self._cap:int = cap

    def get_via(self) -> str:
        return self._via
    
    def get_civico(self) -> int|str:
        return self._civico
    
    def get_cap(self) -> str:
        return self._cap
    
    def __str__(self) -> str:
        return f"Via: {self.get_via()}, Civico: {self.get_civico()}, CAP: {self.get_cap()}"
    
    def __repr__(self) -> str:
        return f"Indirizzo(via={self.get_via()}, civico={self.get_civico()}, cap={self.get_cap()})"
    
    def __hash__(self) -> int:
        return hash((self._via, self._civico, self._cap))

    def __eq__(self, other:Any) -> bool:
        if other is None or not isinstance(other, Indirizzo):
            return False
        if hash(self) != hash(other):
            return False
        return self.get_via() == other.get_via() and self.get_civico() == other.get_civico() and self.get_cap() == other.get_cap()
    
if __name__ == "__main__":
    
    i1:Indirizzo = Indirizzo("via roma", 64, "02343")
    print(i1)

    # i2:Indirizzo = Indirizzo(1232,"43ghf", "3768768")
    # print(i2)

    # i3:Indirizzo = Indirizzo("Corso Navi","43ghf", "3768768")
    # print(i3)

    i4:Indirizzo = Indirizzo("Via ROMA", 64, "02343")
    print(i4)

    print(i1 == i4)

    i5:Indirizzo = Indirizzo("vIa romA", 64, "02343")
    print(i5)

    i6:Indirizzo = Indirizzo("via garibaldi", "14b", "09543")
    print(i6)

    elenco_inirizzi:set = {i1, i4, i5, i6}
    print(elenco_inirizzi)