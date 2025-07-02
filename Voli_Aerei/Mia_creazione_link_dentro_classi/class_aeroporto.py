from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from class_volo import Volo, arrivo, partenza

from class_luoghi import Citta
from ass_aerop_citta import aerop_citta
from custom_types import CodiceAeroporto

class Aeroporto:
	_codice: CodiceAeroporto # <<immutabile>> noto alla nascita
	_nome: str # noto alla nascita / mutabile
	_aeroporto_citta: 'aerop_citta._link'  #noto alla nastita / mutabile
	_elenco_voli_arrivo: set[arrivo._link]  # certamente non noto alla nascita / muttabile
	_elenco_voli_partenza: set[partenza._link]  # certamente non noto alla nascita / muttabile

	def __init__(self, codice: CodiceAeroporto, nome: str, citta:'Citta') -> None:
		if citta is None:
			raise ValueError("Bisogna indicare la citta!")
		self._codice = codice
		self.set_nome(nome)
		self._aeroporto_citta = None   # in caso di versione 2 set_aeroporto_citta()
		self.set_aeroporto_citta(citta)
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
		return self._aeroporto_citta
	
	def get_citta(self) -> Citta:
		return self.get_link_aerop_citta().get_citta()

	# responsabile di creazione o modifica  
	def set_aeroporto_citta(self, citta:'Citta') -> None:
		# try:                                             # versione 1. quale versione è migliore???
		# 	if self.get_link_aerop_citta():
		# 		self._remove_link_aerop_citta(self.get_link_aerop_citta())
		# except AttributeError:
		# 	pass

		#controllo dublicato            funziona solo dentro una citta ma non fa controllo generico  :-((
		# for link in citta.get_elenco_aeroporti():
		# 	if link.get_aeroporto().get_codice() == self.get_codice():  #self._codice deve essere definito prima di chiamare set_aeroporto_citta()
		# 		raise ValueError(f"Il codice di aeroporto deve essere univoco")
		if self.get_link_aerop_citta() is not None:        # versione 2. ho impostato self._aeroporto_citta = None 
			if self.get_link_aerop_citta().get_citta() == citta:   # se esite gia link verso citta, non fa lavoro inutile
				raise ValueError("Errore, il link è gia presente")
			self._remove_link_aerop_citta(self._aeroporto_citta)
		link:'aerop_citta._link' = aerop_citta._link(self, citta)
		self._aeroporto_citta = link
		citta._aggiorna_elenco_aeroporti(link)

	def _remove_link_aerop_citta(self, link:'aerop_citta._link') -> None:
		# caso di errore
		if link.get_aeroporto() != self:
			raise ValueError(f"Link fornito non riguarda aeroporto {self.get_nome()} ")	
		if self.get_link_aerop_citta() == link:   #serve solo per evitare di usare questo metodo con vechio link che riguarda self
			self._aeroporto_citta = None
			#TODO aggiornare set citta
			link.get_citta()._aggiorna_elenco_vecchi_aeroporti(link)
			link.get_citta()._solo_remove_link_aerop_citta(link)
		

# collegamento con class Volo, associzaone - arrivo

	def get_elenco_voli_arrivo(self) -> frozenset[arrivo._link]:
		return frozenset(self._elenco_voli_arrivo)

	def _aggiorna_elenco_voli_arrivo(self, link:arrivo._link) -> None:
		if link.get_aeroporto() != self:
			raise ValueError(f"Errore, il link non riguarga aeroporto {self.get_nome()}")
		if link in self._elenco_voli_arrivo:
			raise ValueError(f"Aeroporto ha gia il link di volo {link.get_volo().get_codice()} ")
		self._elenco_voli_arrivo.add(link)

# collegamento con class Volo, associzaone - partenza

	def get_elenco_voli_partenza(self) -> frozenset[partenza._link]:
		return frozenset(self._elenco_voli_partenza)

	def _aggiorna_elenco_voli_partenza(self, link:partenza._link) -> None:
		if link.get_aeroporto() != self:
			raise ValueError(f"Errore, il link non riguarga aeroporto {self.get_nome()}")
		if link in self._elenco_voli_arrivo:
			raise ValueError(f"Aeroporto ha gia il link di volo {link.get_volo().get_codice()} ")
		self._elenco_voli_partenza.add(link)


	def __str__(self) -> str:
		return f"Aeroporto: '{self.get_nome()}', codice: {self.get_codice()}, citta: {self.get_citta().get_nome()}"
    
	def __repr__(self) -> str:
		return f"Aeroporto('{self.get_nome()}', CodiceAeroporto({self.get_codice()}))"