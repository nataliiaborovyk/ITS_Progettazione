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
print(alice)

print(f"\tVendite: {[l.impiegato().nome() for l in vendite.impiegati()]}\n")
acquisti: Dipartimento = Dipartimento(nome="acquisti", telefono=Telefono("070707"))

print("Creo Biagio senza dipartimento")
biagio: Impiegato = Impiegato("Biagio", "Bianchi",
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
