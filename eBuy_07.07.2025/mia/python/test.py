from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from class_Utente import Utente
from class_Privato import Privato
from class_PostOggetto import PostOggetto
from class_Asta import Asta
from class_Bid import Bid

from ass_bid_ut import bid_ut
from ass_asta_bid import asta_bid

from datetime import datetime
from tipoDato_FloatGez import FloatGez
from tipoDato_IntGEZ import IntGEZ
from tipoDato_Condizioni import Condizioni
import random

print("\ncreo utenti")

alice: Privato = Privato("alice_bella")
print(alice)

biagio: Privato = Privato("biaggio_carino")
print(biagio)

carlo = Privato("carlo_generoso")
print(carlo)


print("\ncreo aste")

asta_1: Asta = Asta(
                    descrizione="Libro di Python", 
                    prezzo=FloatGez(18), 
                    anni_garanzia=IntGEZ(2),  
                    prezzo_bid=FloatGez(0.5), 
                    scadenza="20-10-2025 20:00")
print(asta_1)

asta_2: Asta = Asta(
                    descrizione="WEB", 
                    prezzo=FloatGez(25), 
                    anni_garanzia=IntGEZ(2),  
                    prezzo_bid=FloatGez(0.5), 
                    scadenza="20-10-2025 20:00", 
                    condizioni=Condizioni("ottimo"))
print(asta_2)


print("\nCreo bid su asta_1")

bid_1:Bid = Bid(asta_1, alice)
print(bid_1)

print(f"Prezzo attuale asta_1 N. \'{asta_1.get_id()}\' è ", asta_1.prezzo(datetime.now()))

bid_2:Bid = Bid(asta_1, biagio)
print(bid_2)

print(f"Prezzo attuale asta_1 N. \'{asta_1.get_id()}\' è ", asta_1.prezzo(datetime.now()))

bid_3:Bid = Bid(asta_1, carlo)
print(bid_3)

print(f"Prezzo attuale asta_1 N. \'{asta_1.get_id()}\' è ", asta_1.prezzo(datetime.now()))


print("\nCreo bid su asta_2")

bid_4:Bid = Bid(asta_2, alice)
print(bid_4)

bid_5:Bid = Bid(asta_2, biagio)
print(bid_5)


print("\nStampo ultimo bid su asta_1")

ultimo:Bid = asta_1.ultimo_bid(datetime.now())
print("Ultimo bid su asta_1:")
print(ultimo)


print("\nStampo ultimo bid su asta_2")

ultimo:Bid = asta_2.ultimo_bid(datetime.now())
print("Ultimo bid su asta_2:")
print(ultimo)

print("\nStampo vincitore asta_1 (se scaduta)")

vincitore_asta_1:Utente = asta_1.vincitore()
print("Vincitore asta_1:")
print(vincitore_asta_1)

print(asta_1.get_elenco_link_asta_bid())