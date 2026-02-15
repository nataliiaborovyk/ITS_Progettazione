from custom_types import *
from v2_classi_respons_Dipart import *
from datetime import date, timedelta
from v2_classi_respons_Dipart import _imp_prog

print("\t...creo dipartimento \"Logistica\"")
logistica: Dipartimento = Dipartimento(nome="Logistica", telefono=Telefono("060606"))
print(logistica)
print("\t...stampo impiegati che lavorano in \"Logistica\"")
print(logistica.get_impiegati())

print("\t...creo dipartimento \"trasporto\"")
trasporto: Dipartimento = Dipartimento(nome="trasporto", telefono=Telefono("070707"))
print(trasporto)
print("\t...stampo impiegati che lavorano in \"trasporto\"")
print(trasporto.get_impiegati())


print("\n\t\t!!! primo caso - creo impegato con link afferenza")

print("\t...creo Alice in \"Lofistica\"e")
alice: Impiegato = Impiegato("Alice", "Alberelli",
                             nascita=date.today() - timedelta(weeks=52*25),
                             stipendio=Importo(45000),
                             dipartimento_aff=logistica, data_afferenza=date.today() - timedelta(weeks=52 * 4))
print(alice)
print(logistica)

print("\t...stampo impiegati che lavorano in \"Logistica\"")
print(logistica.get_impiegati())
#print(f"logistica: {[l.get_impiegato().get_nome() for l in logistica.get_impiegati()]}\n")



print("\n\t\t!!! secondo caso - creo impegato senza link afferenza")

print("\t...creo Biagio senza dipartimento")
biagio: Impiegato = Impiegato("Biagio", "Bianchi",
                              nascita=date.today() - timedelta(weeks=52 * 65),
                              stipendio=Importo(45000) )
print(biagio)

print("\t...aggiungo Biagio a \"Aquisti\"")
biagio.set_link_afferenza(trasporto, date.today() - timedelta(weeks=52 * 2))

print("\t...stampo impiegati che lavorano in \"trasporto\"")
print(trasporto.get_impiegati())

print("Creo Carlo senza dipartimento")
carlo: Impiegato = Impiegato("Carlo", "Colletti",
                              nascita=date.today() - timedelta(weeks=52 * 65),
                              stipendio=Importo(45000) )

#print(f"\tlogistica: {[l.get_impiegato().get_nome() for l in logistica.get_impiegati()]}\n")


print("\n\t\t!!! terzo caso - cambio link afferenza")

print("\t...sposto Biagio in \"Logistica\"")
biagio.set_link_afferenza(logistica, date.today())

print("\t...stampo impiegati che lavorano in \"trasporto\"")
print(trasporto.get_impiegati())

print("\t...stampo impiegati che lavorano in \"Logistica\"")
print(logistica.get_impiegati())

# print("Impiegati di ogni dipartimento:")
# print(f"\tlogistica: {[l.impiegato().nome() for l in logistica.impiegati()]}")
# print(f"\ttrasporto: {[l.impiegato().nome() for l in trasporto.impiegati()]}")


print("\n\t\t!!! quarto caso - elimino link afferenza (set_link_afferenza(None, None))")

print("\t...rimuovo Alice dal suo dipartimento")
alice.set_link_afferenza(None, None)

print("\t...stampo impiegati che lavorano in \"Logistica\"")
print(logistica.get_impiegati())

print("\t...stampo impiegati che lavorano in \"trasporto\"")
print(trasporto.get_impiegati())

print("\n\t\t!!! quinto caso - elimino link afferenza (remove_link_afferenza())")

print("\t...rimuovo Biagio dal suo dipartimento")
biagio.remove_link_afferenza()

print("\t...stampo impiegati che lavorano in \"Logistica\"")
print(logistica.get_impiegati())

print("\t...stampo impiegati che lavorano in \"trasporto\"")
print(trasporto.get_impiegati())


print("\n\t\t!!! sesto caso - creo link da classe Dipartimento")

print("\t...aggiungo Biaggio alle \"Logistica\"")
logistica.creaLinkAfferenza(biagio, date.today() - timedelta(weeks=52 * 1) )
print(logistica)

print("\t...aggiungo Alice alle \"trasporto\"")
trasporto.creaLinkAfferenza(alice, date.today() - timedelta(weeks=52 * 1))
print(trasporto)

print("\t...stampo impiegati che lavorano in \"Logistica\"")
print(logistica.get_impiegati())

print("\t...stampo impiegati che lavorano in \"trasporto\"")
print(trasporto.get_impiegati())


print("\n\t\t!!! settimo caso - cambio link da classe Dipartimento")

print("\t...sposto Alice in \"Logistica\"")
logistica.creaLinkAfferenza(alice, date.today() - timedelta(days=30 * 2))
print(logistica)

print("\t...sposto Biagio in \"trasporto\"")
trasporto.creaLinkAfferenza(biagio, date.today() - timedelta(days=30 * 2))
print(trasporto)


print("\n\t\t!!! ottavo caso - elimino link da classe Dipartimento")

print("\t...rimuovo Alice dal \"Logistica\" da Dipartimento")
logistica.remove_impiegato(alice)
print(logistica)

print("\t...rimuovo Biagio dal \"Trasporto\" da Dipartimento")
trasporto.remove_impiegato(biagio)
print(trasporto)

# ._remove_impiegato(biagio.get_link_afferenza())
# print(acquisti)

# print("Impiegati di ogni dipartimento:")
# print(f"\tlogistica: {[l.impiegato().nome() for l in logistica.impiegati()]}")
# print(f"\ttrasporto: {[l.impiegato().nome() for l in trasporto.impiegati()]}")




print("\n\n--------------------Progetti aggiunge link--------------------\n")

print("....Aggiungo Alice al progetto Pegaso")
pegaso: Progetto = Progetto(nome="Pegaso", budget=Importo(25000))

oggi = date.today()
domani = date.today() + timedelta(days=1)
pegaso.add_impiegato(alice, oggi)

print("....Provo nuovamente ad aggiungere Alice al progetto Pegaso")
try:
    pegaso.add_impiegato(alice, domani)
    print("Sono riuscito ad aggiungere due volte Alice al progetto Pegaso :(")
except KeyError as e:
    print(e)

print("....Provo a rimuovere Biagio dal progetto Pegaso")
try:
    pegaso.remove_impiegato(biagio)
except KeyError as e:
    print(e)

print("....Aggiungo Biagio al progetto Pegaso")
pegaso.add_impiegato(biagio, domani)
print("....Aggiungo Carlo al progetto Pegaso")
pegaso.add_impiegato(carlo, date.today()-timedelta(days=150))

print("....Controllo se  Biagio al progetto Pegaso")
print(pegaso.is_coinvolto(biagio))
print(biagio in pegaso)

print(f"....Ultimo impiegato coinvolto in Pegaso: "
      f"{pegaso.ultimo_impiegato_coinvolto().get_nome()}")

phoenix: Progetto = Progetto(nome="Phoenix", budget=Importo(75000))
phoenix.add_impiegato_oggi(carlo)

imp_prog: set[_imp_prog] = set()
imp_prog.update(pegaso.get_coinvolti())
imp_prog.update(phoenix.get_coinvolti())
print(imp_prog)

print("\n\n-------------------Impiegato aggiunge link--------------------\n")

print("\t...creo Anna senza dipartimento")
anna: Impiegato = Impiegato("Anna", "Rossi",
                              nascita=date.today() - timedelta(weeks=52 * 65),
                              stipendio=Importo(45000) )
print(anna)
anna.add_progetto(pegaso, oggi)
print("....Controllo se  Anna al progetto Pegaso")
print(anna.is_coinvolto(pegaso))
print(anna in pegaso)
imp_prog.update(pegaso.get_coinvolti())
print(imp_prog)