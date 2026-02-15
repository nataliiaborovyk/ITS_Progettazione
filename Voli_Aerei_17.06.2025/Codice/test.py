from __future__ import annotations

from tipoDato_intGEZ import IntGEZ  
from assoc_class_nazione import Nazione
from assoc_class_citta import Citta


n1: Nazione = Nazione("italia")
print(n1)
print(n1.cit_naz())   

c1:Citta = Citta("Roma", IntGEZ(2746789), n1)
n1.creaLinkCitta(c1)  #come argomento va oggetto e non stringa
print(n1)