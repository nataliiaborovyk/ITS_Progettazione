from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from class_volo import Volo, volo_comp

from custom_types import IntG1909
from class_luoghi import Citta

class CompagniaAerea:
	_nome: str # noto alla nascita
	_anno_fondazione: IntG1909 # <<immutable>>, noto alla nascita
	_comp_direzione_citta: Citta 	# noto alla nascita
	_elenco_voli: set[volo_comp._link]   # certamente non noto alla nascita / mutabile
	_elenco_vecchi_voli: set[volo_comp._link]  # certamente non noto alla nascita / mutabile

	def __init__(self, nome: str, anno_fondazione: IntG1909, citta_sede: Citta) -> None:
		self.set_nome(nome)
		self._anno_fondazione = anno_fondazione
		self.set_citta_sede(citta_sede)
		self._elenco_voli = set()
		self._elenco_vecchi_voli = set()

	def get_nome(self) -> str:
		return self._nome

	def get_anno_fondazione(self) -> IntG1909:
		return self._anno_fondazione

	def set_nome(self, nome: str) -> None:
		self._nome = nome

# collegamento con class Citta, agregazione - comp_direzione_citta

	def get_citta_sede(self) -> Citta:
		return self._comp_direzione_citta

	def get_comp_direzione_citta(self) -> Citta:
		"""Semplice alias di citta_sede()"""
		return self.get_citta_sede()

	def set_citta_sede(self, c: Citta) -> None:
		self._comp_direzione_citta = c

# collegamento con class Volo, associazione - volo_comp

	def get_elenco_voli(self) -> frozenset[volo_comp._link]:
		return frozenset(self._elenco_voli)
	
	def _aggiorna_elenco_voli(self, link:volo_comp._link) -> None:
		if link.get_compania() != self:
			raise ValueError(f"Il link non riguarda compania {self.get_nome()}")
		if link in self._elenco_voli:
			raise ValueError(f"Il link è gia presente nel elenco")
		self._elenco_voli.add(link)

	def _aggiorna_elenco_vecchi_voli(self, link:volo_comp._link) -> None:
		if link.get_compania() != self:
			raise ValueError(f"Il link non riguarda compania {self.get_nome()}")
		if link in self._elenco_voli:
			raise ValueError("Il link è ancora presente nel elenco voli attuali") 
		if link in self._elenco_vecchi_voli:
			raise ValueError(f"Il link è gia presente nel elenco voli vecchi")
		self._elenco_vecchi_voli.add(link)

	# ?????????????????????????????????????????????????????????????????????????????
	# serve solo nel caso se viene eliminato il ogetto volo, per salvare il link nel _elenco_vecchi_voli
	def _remove_link_volo_comp(self, link:volo_comp._link) -> None:
		if link.get_compania() != self:
			raise ValueError(f"Il link non riguarda compania {self.get_nome()}")
		if link not in self._elenco_voli:
			raise ValueError(f"Il link non è presente nel elenco")
		self._elenco_voli.remove(link)

	def __str__(self) -> str:
		return f"Compania aerea: {self.get_nome()}, anno di fondazione: {self.get_anno_fondazione()}"
    