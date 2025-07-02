from custom_types import *
from classi_direzione import *
from datetime import date, timedelta
from classi_direzione import imp_prog

print("\n\n--------------------direzione--------------------\n")

print("\t...creo GianLuca senza dipartimento")
gianluca: Impiegato = Impiegato("GianLuca", "Verdi",
                              nascita=date.today() - timedelta(weeks=52 * 80),
                              stipendio=Importo(105000) )
print(gianluca)

print("\t...creo Gaetano senza dipartimento")
gaetano: Impiegato = Impiegato("Gaetano", "Di Filippo",
                              nascita=date.today() - timedelta(weeks=52 * 78),
                              stipendio=Importo(95000) )
print(gaetano)

print("\t...creo Elisabetta senza dipartimento")
elisabetta: Impiegato = Impiegato("Elisabetta", "Di Filippo",
                              nascita=date.today() - timedelta(weeks=52 * 78),
                              stipendio=Importo(95000) )
print(elisabetta)



print("\t...creo dipartimento \"Logistica\"")
logistica: Dipartimento = Dipartimento(nome="Logistica", telefono=Telefono("060606"), impiegato=gianluca)
print(logistica)
print("\t...stampo impiegati che lavorano in \"Logistica\"")
print(logistica.get_elenco_impiegati())

print("\t...creo dipartimento \"trasporto\"")
trasporto: Dipartimento = Dipartimento(nome="trasporto", telefono=Telefono("070707"), impiegato=gaetano)
print(trasporto)
print("\t...stampo impiegati che lavorano in \"trasporto\"")
print(trasporto.get_elenco_impiegati())

print("\t...cambio direttore della logistica a Elisabetta")
logistica.set_link_direzione(elisabetta)
print(logistica)

print("\t...controllo se Gianluca dirige dipartimento")
print(gianluca.dirige())

print("\n\n--------------------afferenza--------------------\n")

print("\n\t\t!!! primo caso - creo impegato con link afferenza")

print("\t...creo Alice in \"Lofistica\"e")
alice: Impiegato = afferenza.add_impiegato_con_link("Alice", "Alberelli",
                             nascita=date.today() - timedelta(weeks=52*25),
                             stipendio=Importo(45000), dipartimento=logistica, data_afferenza=date.today() - timedelta(weeks=52 * 2) )
print(alice)
print("\t...controllo se Alice dirige dipartimento")
print(alice.dirige())
print("\n\t...stampo dipartimento \"Logistica\"")
print(logistica)

print("\t...stampo impiegati che lavorano in \"Logistica\"")
print(logistica.get_elenco_impiegati())
#print(f"logistica: {[l.get_impiegato().get_nome() for l in logistica.get_elenco_impiegati()]}\n")



print("\n\t\t!!! secondo caso - creo impegato senza link afferenza")


print("\t...creo Biagio senza dipartimento")
biagio: Impiegato = Impiegato("Biagio", "Bianchi",
                              nascita=date.today() - timedelta(weeks=52 * 65),
                              stipendio=Importo(45000) )
print(biagio)

print("\t...aggiungo Biagio a \"Trasporto\"")
biagio_in_aquisti: afferenza._link = afferenza.add_link(biagio, trasporto, date.today() - timedelta(weeks=52 * 2))

print("\t...stampo impiegati che lavorano in \"trasporto\"")
print(trasporto.get_elenco_impiegati())

print("\t...Creo Carlo senza dipartimento")
carlo: Impiegato = Impiegato("Carlo", "Colletti",
                              nascita=date.today() - timedelta(weeks=52 * 65),
                              stipendio=Importo(45000) )
print(carlo)

#print(f"\tlogistica: {[l.get_impiegato().get_nome() for l in logistica.get_elenco_impiegati()]}\n")


print("\n\t\t!!! terzo caso - cambio link afferenza")

print("\t...sposto Biagio in \"Logistica\"")
biagio_in_logistica: afferenza._link = afferenza.add_link(biagio, logistica, date.today())

print("\t...stampo impiegati che lavorano in \"trasporto\"")
print(trasporto.get_elenco_impiegati())

print("\t...stampo impiegati che lavorano in \"Logistica\"")
print(logistica.get_elenco_impiegati())

# print("Impiegati di ogni dipartimento:")
# print(f"\tlogistica: {[l.impiegato().nome() for l in logistica.impiegati()]}")
# print(f"\ttrasporto: {[l.impiegato().nome() for l in trasporto.impiegati()]}")


print("\n\t\t!!! quarto caso - elimino link afferenza")

print("\t...rimuovo Biagio dal suo dipartimento")
afferenza.remove_link(biagio_in_logistica)

print("\t...stampo impiegati che lavorano in \"Logistica\"")
print(logistica.get_elenco_impiegati())

print("\t...stampo impiegati che lavorano in \"trasporto\"")
print(trasporto.get_elenco_impiegati())


print("\n\n--------------------direzione--------------------\n")

print("\t...creo Elvira senza dipartimento")
elvira: Impiegato = Impiegato("Elvira", "Pasini",
                              nascita=date.today() - timedelta(weeks=52 * 50),
                              stipendio=Importo(70000) )
print(elvira)


print("\n\n--------------------Imp_prog._link aggiunge link--------------------\n")

print("\t....Aggiungo Alice al progetto Pegaso")
pegaso: Progetto = Progetto(nome="Pegaso", budget=Importo(25000))

oggi = date.today()
domani = date.today() + timedelta(days=1)
alice_in_pegaso: imp_prog._link = imp_prog.add_link(pegaso, alice, oggi)

print("\t....Controllo se  Alice al progetto Pegaso")
print(alice in pegaso)


# print("....Provo nuovamente ad aggiungere Alice al progetto Pegaso")
# try:
#     alice_in_pegaso: imp_prog._link = imp_prog.add_link(pegaso, alice, oggi)
#     print("Sono riuscito ad aggiungere due volte Alice al progetto Pegaso :(")
# except KeyError as e:
#     print(e)

print("\t....Provo a rimuovere Alice dal progetto Pegaso")
try:
    imp_prog.remove(pegaso, alice)
except KeyError as e:
    print(e)

print("\t....Controllo se  Alice al progetto Pegaso")
print(alice in pegaso)

print("\t....Aggiungo Biagio al progetto Pegaso")
biagio_in_pegaso = imp_prog.add_link(pegaso, biagio, oggi)
print("....Controllo se  Biagio al progetto Pegaso")
print(biagio in pegaso)
print("\t....Aggiungo Carlo al progetto Pegaso")
imp_prog.add_link(pegaso, carlo, domani)
print("\t....Controllo se  Carlo al progetto Pegaso")
print(carlo in pegaso)

print(f"\t....Ultimo impiegato coinvolto in Pegaso: "
      f"{pegaso.ultimo_impiegato_coinvolto().get_nome()}")

phoenix: Progetto = Progetto(nome="Phoenix", budget=Importo(75000))
imp_prog.add_link(phoenix, carlo, oggi)
print("\t....Controllo se  Carlo al progetto Phoenix")
print(carlo in phoenix)


elenco: set[imp_prog._link] = set()
elenco.update(pegaso.get_coinvolti_impiegati())
elenco.update(phoenix.get_coinvolti_impiegati())
print(elenco)

print("\t....stampo progetto Pegaso")
print(pegaso)
print("\t....stampo progetto Phoenix")
print(phoenix)