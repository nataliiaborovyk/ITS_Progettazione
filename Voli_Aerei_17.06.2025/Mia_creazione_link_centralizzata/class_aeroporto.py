from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from class_volo import Volo, arrivo, partenza
	from class_luoghi import Citta
	from ass_aerop_citta import aerop_citta

# from class_luoghi import Citta
from ass_aerop_citta import aerop_citta
from custom_types import CodiceAeroporto

class Aeroporto:
	_codice: CodiceAeroporto # <<immutabile>> noto alla nascita
	_nome: str # noto alla nascita / mutabile
	_link_aerop_citta: 'aerop_citta._link | None'  #noto alla nastita / mutabile
	_elenco_voli_arrivo: set[arrivo._link]  # certamente non noto alla nascita / muttabile
	_elenco_voli_partenza: set[partenza._link]  # certamente non noto alla nascita / muttabile

	def __init__(self, codice: CodiceAeroporto, nome: str, citta:'Citta') -> None:
		if citta is None:
			raise ValueError("Bisogna indicare la citta!")
		self._codice = codice
		self.set_nome(nome)
		self._link_aerop_citta = None   # in caso di versione 2 set_link_aerop_citta()
		self.crea_link_aerop_citta(citta)
		self._elenco_voli_arrivo = set()
		self._elenco_voli_partenza = set()

	def get_nome(self) -> str:
		return self._nome

	def get_codice(self) -> str:
		return self._codice

	def set_nome(self, nome: str) -> None:
		self._nome = nome.capitalize()
	
# colegamento con class Citta, associazione - aerop_citta

	def get_link_aerop_citta(self) -> 'aerop_citta._link':
		return self._link_aerop_citta
	
	def get_citta(self) -> Citta:
		return self.get_link_aerop_citta().get_citta()

	def crea_link_aerop_citta(self, citta:'Citta') -> None:
		''' Crea link aerop_citta da class aerop_citta'''
		aerop_citta.crea_link_aerop_citta(self, citta)

	def _remove_link_aerop_citta(self, link:'aerop_citta._link') -> None:
		''' Rimuove link aerop_citta e aggiorna set in citta'''
		if self.get_link_aerop_citta() == link:
			self._link_aerop_citta = None
	
	def _aggiorna_link_aerop_citta(self, link:aerop_citta._link) -> None:
		self._link_aerop_citta = link

# collegamento con class Volo, associzaone - arrivo

	def get_elenco_voli_arrivo(self) -> frozenset[arrivo._link]:
		return frozenset(self._elenco_voli_arrivo)

	def _aggiorna_elenco_voli_arrivo(self, link:arrivo._link) -> None:
		''' Aggiorna set(arrivo._link) in class Aeroporto'''
		if link.get_aeroporto() != self:
			raise ValueError(f"Errore, il link non riguarga aeroporto {self.get_nome()}")
		if link in self._elenco_voli_arrivo:
			raise ValueError(f"Aeroporto ha gia il link di volo {link.get_volo().get_codice()} ")
		self._elenco_voli_arrivo.add(link)

# collegamento con class Volo, associzaone - partenza

	def get_elenco_voli_partenza(self) -> frozenset[partenza._link]:
		return frozenset(self._elenco_voli_partenza)

	def _aggiorna_elenco_voli_partenza(self, link:partenza._link) -> None:
		''' Aggiorna set(partenza._link) in class Aeroporto'''
		if link.get_aeroporto() != self:
			raise ValueError(f"Errore, il link non riguarga aeroporto {self.get_nome()}")
		if link in self._elenco_voli_partenza:
			raise ValueError(f"Aeroporto ha gia il link di volo {link.get_volo().get_codice()} ")
		self._elenco_voli_partenza.add(link)



	def __str__(self) -> str:
		return f"Aeroporto: '{self.get_nome()}', codice: {self.get_codice()}, citta: {self.get_citta().get_nome()}"
    
	def __repr__(self) -> str:
		return f"Aeroporto('{self.get_nome()}', CodiceAeroporto({self.get_codice()}))"