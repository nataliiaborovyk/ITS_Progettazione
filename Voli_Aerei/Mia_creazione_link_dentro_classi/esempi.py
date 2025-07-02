# from __future__ import annotations
from ass_aerop_citta import aerop_citta
from class_aeroporto import Aeroporto
from class_luoghi import Citta, Nazione
from custom_types import *
from ass_cit_naz import cit_naz

italia = Nazione("Italia")
roma: Citta = Citta("Roma", IntGEZ(2800000), italia)
orte: Citta = Citta("Orte", IntGEZ(9000), italia)

print(roma)
print("....elenco aeroporti")
print(roma.get_elenco_aeroporti())

print(orte)

#ass_aerop_citta_test