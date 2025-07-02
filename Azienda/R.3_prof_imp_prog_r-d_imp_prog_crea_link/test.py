import sys

from custom_types import *
from datetime import date, timedelta
from classi import *
from classi import imp_prog

vendite: Dipartimento = Dipartimento(nome="vendite", telefono=Telefono("060606"))

print(vendite.impiegati())
print("Creo Alice in vendite")
alice: Impiegato = Impiegato("Alice", "Alberelli",
                             nascita=date.today() - timedelta(weeks=52*25),
                             stipendio=Importo(45000),
                             dipartimento_aff=vendite, data_afferenza=date.today())

print(f"\tVendite: {[l.impiegato().nome() for l in vendite.impiegati()]}\n")
acquisti: Dipartimento = Dipartimento(nome="acquisti", telefono=Telefono("070707"))

print("Creo Biagio senza dipartimento")
biagio: Impiegato = Impiegato("Biagio", "Bianchi",
                              nascita=date.today() - timedelta(weeks=52 * 65),
                              stipendio=Importo(45000) )

print("Creo Carlo senza dipartimento")
carlo: Impiegato = Impiegato("Carlo", "Colletti",
                              nascita=date.today() - timedelta(weeks=52 * 65),
                              stipendio=Importo(45000) )

print(biagio)

print("Aggiungo Biagio a Vendite")
biagio.set_link_afferenza(vendite, date.today())

print(f"\tVendite: {[l.impiegato().nome() for l in vendite.impiegati()]}\n")
biagio.set_link_afferenza(acquisti, date.today())
print("Sposto Biagio in Acquisti")

print("Impiegati di ogni dipartimento:")
print(f"\tVendite: {[l.impiegato().nome() for l in vendite.impiegati()]}")
print(f"\tAcquisti: {[l.impiegato().nome() for l in acquisti.impiegati()]}")

print("Rimuovo alice dal suo dipartimento")
alice.set_link_afferenza(None, None)
print("Impiegati di ogni dipartimento:")
print(f"\tVendite: {[l.impiegato().nome() for l in vendite.impiegati()]}")
print(f"\tAcquisti: {[l.impiegato().nome() for l in acquisti.impiegati()]}")


print("\n\n--------------------Progetti--------------------\n")

pegaso: Progetto = Progetto(nome="Pegaso", budget=Importo(25000))

oggi = date.today()
domani = date.today() + timedelta(days=1)

alice_in_pegaso: imp_prog._link = imp_prog.add(pegaso, alice, oggi)

print(f"Ho creato il link ("
      f"{alice_in_pegaso.progetto().nome()}, "
      f"{alice_in_pegaso.impiegato().nome()}, "
      f"a partire dal {alice_in_pegaso.data()}"
      f")")
print("Provo nuovamente ad aggiungere Alice al progetto Pegaso")
try:
    alice_in_pegaso: imp_prog._link = imp_prog.add(pegaso, alice, domani)
    print("Sono riuscito ad aggiungere due volte Alice al progetto Pegaso :(")
except KeyError as e:
    print("Mi sono accorto dell'errore!")
    print(f"\t==> {e}")





print("Provo a rimuovere Biagio dal progetto Pegaso")
try:
    imp_prog.remove(progetto=pegaso, impiegato=biagio)
except KeyError as e:
    print("Mi sono accorto dell'errore!")
    print(f"\t==> {e}")


imp_prog.add(pegaso, biagio, domani)
imp_prog.add(pegaso, carlo, date.today()-timedelta(days=150))

print(pegaso.is_coinvolto(biagio))
print(biagio in pegaso) # invoca il __contains__, equivalente alla linea precedente

print(f"Ultimo impiegato coinvolto in Pegaso: "
      f"{pegaso.ultimo_impiegato_coinvolto().nome()}")

phoenix: Progetto = Progetto(nome="Phoenix", budget=Importo(75000))
imp_prog.add(phoenix, carlo, domani)

ip: set[imp_prog._link] = set()
ip.update(pegaso.coinvolti())
ip.update(phoenix.coinvolti())
