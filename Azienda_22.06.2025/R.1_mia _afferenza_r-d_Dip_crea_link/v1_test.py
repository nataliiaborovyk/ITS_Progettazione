from custom_types import *
from v1_classi_respons_Dipart import *
from datetime import date, timedelta

print("\t...creo dipartimento \"Vendite\"")
vendite: Dipartimento = Dipartimento(nome="Vendite", telefono=Telefono("060606"))
print(vendite)
print("\t...stampo impiegati che lavorano in \"Vendite\"")
print(vendite.get_impiegati())

print("\t...creo dipartimento \"Aquisti\"")
acquisti: Dipartimento = Dipartimento(nome="Acquisti", telefono=Telefono("070707"))
print(acquisti)
print("\t...stampo impiegati che lavorano in \"Acquisti\"")
print(acquisti.get_impiegati())

print("\n\t\t!!! primo caso - creo impegato con link afferenza da classe Impiegato")

print("\t...creo Alice in vendite")
alice: Impiegato = Impiegato("Alice", "Alberelli",
                             nascita=date.today() - timedelta(weeks=52*25),
                             stipendio=Importo(45000),
                             dipartimento_aff=vendite, data_afferenza=date.today() - timedelta(weeks=52 * 4))
print(alice)
print(vendite)
print("\t...stampo impiegati che lavorano in \"Vendite\"")
print(vendite.get_impiegati())

#print(f"Vendite: {[l.get_impiegato().get_nome() for l in vendite.get_impiegati()]}\n")

print("\n\t\t!!! secondo caso - creo impegato senza link afferenza")

print("\t...creo Biagio senza dipartimento")
biagio: Impiegato = Impiegato("Biagio", "Bianchi",
                              nascita=date.today() - timedelta(weeks=52 * 65),
                              stipendio=Importo(45000) )
print(biagio)

print("\t...aggiungo Biagio a \"Aquisti\"")
biagio.set_link_afferenza(acquisti, date.today() - timedelta(weeks=52 * 2))

print("\t...stampo impiegati che lavorano in \"Acquisti\"")
print(acquisti.get_impiegati())

#print(f"\tVendite: {[l.get_impiegato().get_nome() for l in vendite.get_impiegati()]}\n")

print("\n\t\t!!! terzo caso - cambio link afferenza")

print("\t...sposto Biagio in \"Vendite\"")
biagio.set_link_afferenza(vendite, date.today())
print("\t...stampo impiegati che lavorano in \"Acquisti\"")
print(acquisti.get_impiegati())
print("\t...stampo impiegati che lavorano in \"Vendite\"")
print(vendite.get_impiegati())


# print("Impiegati di ogni dipartimento:")
# print(f"\tVendite: {[l.impiegato().nome() for l in vendite.impiegati()]}")
# print(f"\tAcquisti: {[l.impiegato().nome() for l in acquisti.impiegati()]}")

print("\n\t\t!!! quarto caso - elimino link afferenza (set_link_afferenza(None, None))")

print("\t...rimuovo Alice dal \"Aquisti\"da Impiegato")
alice.set_link_afferenza(None, None)
print("\t...stampo impiegati che lavorano in \"Vendite\"")
print(vendite.get_impiegati())
print("\t...stampo impiegati che lavorano in \"Acquisti\"")
print(acquisti.get_impiegati())

print("\n\t\t!!! quinto caso - elimino link afferenza (remove_link_afferenza())")

print("\t...rimuovo Biagio dal \"Vendite\" da Impiegato")
biagio.remove_link_afferenza()
print("\t...stampo impiegati che lavorano in \"Vendite\"")
print(vendite.get_impiegati())
print("\t...stampo impiegati che lavorano in \"Acquisti\"")
print(acquisti.get_impiegati())

print("\n\t\t!!! sesto caso - creo link da classe Dipartimento")
print("\t...aggiungo Biaggio alle \"Vendite\"")
vendite.creaLinkAfferenza(biagio, date.today() - timedelta(weeks=52 * 1) )
print(vendite)
print("\t...aggiungo Alice alle \"Aquisti\"")
acquisti.creaLinkAfferenza(alice, date.today() - timedelta(weeks=52 * 1))
print(acquisti)
print("\t...stampo impiegati che lavorano in \"Vendite\"")
print(vendite.get_impiegati())
print("\t...stampo impiegati che lavorano in \"Acquisti\"")
print(acquisti.get_impiegati())

print("\n\t\t!!! settimo caso - cambio link da classe Dipartimento")
print("\t...sposto Alice in \"Vendite\"")
vendite.creaLinkAfferenza(alice, date.today() - timedelta(days=30 * 2))
print(vendite)
print("\t...sposto Biagio in \"Aquisti\"")
acquisti.creaLinkAfferenza(biagio, date.today() - timedelta(days=30 * 2))
print(acquisti)

print("\n\t\t!!! ottavo caso - elimino link da classe Dipartimento")

print("\t...rimuovo Biagio dal \"Aquisti\" da Dipartimento")
acquisti.remove_impiegato(biagio)
print(acquisti)

print("\t...rimuovo Alice dal \"Vendite\" da Dipartimento")
vendite.remove_impiegato(alice)
print(acquisti)
# print("Impiegati di ogni dipartimento:")
# print(f"\tVendite: {[l.impiegato().nome() for l in vendite.impiegati()]}")
# print(f"\tAcquisti: {[l.impiegato().nome() for l in acquisti.impiegati()]}")
