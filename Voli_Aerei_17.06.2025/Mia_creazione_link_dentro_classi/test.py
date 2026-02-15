from class_aeroporto import Aeroporto
from class_compagnia import CompagniaAerea
from class_luoghi import Citta, Nazione
from class_volo import Volo

from ass_aerop_citta import aerop_citta
from ass_arrivo import arrivo
from ass_cit_naz import cit_naz
from ass_partenza import partenza
from ass_volo_comp import volo_comp

from custom_types import *

print("\n\t....creo nazioni")
italia: Nazione = Nazione("Italia")
francia: Nazione = Nazione("Francia")
print(italia)
print(francia)

print("\n\t....creo citta con link cit_naz")
roma: Citta = Citta("Roma", IntGEZ(2800000), italia)
milano: Citta = Citta("Milano", IntGEZ(1500000), italia)
print(roma)
print(milano)

print("\n\t...stampo Italia")
print(italia)

print("\n\t....creo citta zenza link cit_naz")
try:
    orte: Citta = Citta("Orte", IntGEZ(9000))
except TypeError as e:
    print("Errore previsto: manca attributo nazione\n", e)

print("\n\t....creo Aeroporto con link aerop_citta")
a1: Aeroporto = Aeroporto(CodiceAeroporto("FCO"), "Fiumicino", roma)
a2: Aeroporto = Aeroporto(CodiceAeroporto("CIA"), "Ciampino", roma)
print(a1)
print(a2)
print("\n\t...stampo nomi aeroporti presenti a Roma")
print(roma.get_tutti_aeroporti())

print("\n\t....cambio link aerop_citta")
a1.set_aeroporto_citta(milano)
print(a1)

print("\n\t....creo aeroporto dublicato con link aerop_citta")
try:
    a3: Aeroporto = Aeroporto(CodiceAeroporto("CIA"), "Ciampino", roma)
except ValueError as e:
    print("Errore previsto: aeroporto con quel codice gia esiste\n", e)


print("\n\t....creo companie aerei con link comp_cit")
compagnia1: CompagniaAerea = CompagniaAerea("Alitalia", IntG1909(1946), roma)
compagnia2: CompagniaAerea = CompagniaAerea("Ryanair", IntG1909(1984), roma)
print(compagnia1)
print(compagnia2)

print("\n\t....provo a creare compania aerea senza link comp_cit")
try: 
    compagnia2: CompagniaAerea = CompagniaAerea("WizzAir", IntG1909(1984))
except TypeError as e:
    print("Errore previsto, manca aributo citta\n", e)

print("\n\t....creo voli con link comp_cit, arrivo e partenza")
volo1: Volo = Volo("AZ321", IntGZ(60), compagnia1, a1, a2)
volo2: Volo = Volo("FR456", IntGZ(120), compagnia2, a2, a1)
print(volo1)
print(volo2)
print(f"\n\t....Volo: {volo1.get_codice()}  stampo aeroporti di arrivo e partenza")
print(f"Volo: {volo1.get_codice()} \naeroporto partenza: {volo1.get_aeroporto_partenza().get_nome()}\naeroporto arrivo: {volo1.get_aeroporto_arrivo().get_nome()}")
print(f"\n\t....Volo: {volo2.get_codice()}  stampo aeroporti di arrivo e partenza")
print(f"Volo: {volo2.get_codice()} \naeroporto partenza: {volo2.get_aeroporto_partenza().get_nome()}\naeroporto arrivo: {volo2.get_aeroporto_arrivo().get_nome()}")

print("\n\t....provo a creare volo con codice dublicato")
try:
    volo3: Volo = Volo("AZ321", IntGZ(90), compagnia1, a1, a2)
except ValueError as e:
    print("Errore previsto, volo con quel codice gia esiste\n", e)

print("\n\t....provo a creare volo senza link arrivo")
try:
    volo4: Volo = Volo("Aa444", IntGZ(90), compagnia1, aerop_partenza=a1)
except TypeError as e:
    print("Errore previsto, manca aributo aerop_arrivo\n", e)

print("\n\t....provo a creare volo senza link partenza")
try:
    volo5: Volo = Volo("Aa444", IntGZ(90), compagnia1, aerop_arrivo=a1)
except TypeError as e:
    print("Errore previsto, manca aributo aerop_partenza\n", e)

print("\n\t....provo a creare volo senza compania aerea")
try:
    volo6: Volo = Volo("Aa444", IntGZ(90), aerop_arrivo=a1, aerop_partenza=a1)
except TypeError as e:
    print("Errore previsto, manca aributo compania\n", e)

print("\n\t....rinomino correttamente la nazione da Francia a Germania")
francia.set_nome("Germania")
print(francia)

print("\n\t....provo a collegare manualmente una città a una nazione sbagliata")
try:
    link_sbagliato = cit_naz._link(roma, francia)  # francia non esiste più, ora si chiama Germania
    italia._aggiorna_link_elenco_citta(link_sbagliato)  # questo solleva errore
except ValueError as e:
    print("Errore previsto: il link non riguarda questa nazione\n", e)

print("\n\t....cambio nazione di Milano → Germania")
milano.set_nazione(francia)  # francia ora si chiama Germania
print(milano)
print(italia)
print(francia)



print("\n\t....provo a creare aeroporto con stesso codice in un'altra città")
try:
    Aeroporto(CodiceAeroporto("CIA"), "AeroportoFake", milano)
except ValueError as e:
    print("Errore previsto: codice aeroporto già in uso\n", e)
#puo creare aeropotro con codice uguale ma nella citta diversa  :-(