from classi import _imp_prog
from custom_types import *
from classi import *
from datetime import date, timedelta

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
pegaso.add_impiegato(alice, oggi)

print("Provo nuovamente ad aggiungere Alice al progetto Pegaso")
try:
    pegaso.add_impiegato(alice, domani)
    print("Sono riuscito ad aggiungere due volte Alice al progetto Pegaso :(")
except KeyError as e:
    print(e)

print("Provo a rimuovere Biagio dal progetto Pegaso")
try:
    pegaso.remove_impiegato(biagio)
except KeyError as e:
    print(e)

pegaso.add_impiegato(biagio, domani)
pegaso.add_impiegato(carlo, date.today()-timedelta(days=150))

print(pegaso.is_coinvolto(biagio))
print(biagio in pegaso)

print(f"Ultimo impiegato coinvolto in Pegaso: "
      f"{pegaso.ultimo_impiegato_coinvolto().nome()}")

phoenix: Progetto = Progetto(nome="Phoenix", budget=Importo(75000))
phoenix.add_impiegato_oggi(carlo)

imp_prog: set[_imp_prog] = set()
imp_prog.update(pegaso.coinvolti())
imp_prog.update(phoenix.coinvolti())
