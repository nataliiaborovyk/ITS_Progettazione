from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ass_aerop_citta import aerop_citta
	# from ass_cit_naz import cit_naz
	from class_aeroporto import Aeroporto

from ass_cit_naz import cit_naz
from custom_types import IntGEZ
#import inspect                                   #????????????????????
# from class_aeroporto import Aeroporto
# from ass_aerop_citta import *


class Citta:

	_nome:str      # noto alla nascita / mutabile
	_abitanti:IntGEZ     # noto alla nascita / mutabile
	_elenco_aeroporti: set['aerop_citta._link']    # non noto alla nascita [0..*] / mutabile / bisogna salvare vecchi_link??????????
	_elenco_vecchi_aeroporti: set['aerop_citta._link']
	_nazione_citta: cit_naz._link

	def __init__(self, nome: str, abitanti: IntGEZ, nazione:Nazione) -> None:
		self.set_nome(nome)
		self.set_abitanti(abitanti)
		self._elenco_aeroporti = set()
		self._elenco_vecchi_aeroporti = set()
		self._nazione_citta = None
		self.set_nazione(nazione)

	def get_nome(self) -> str:
		return self._nome

	def set_nome(self, nome: str) -> None:
		self._nome = nome.capitalize()

	def get_abitanti(self) -> IntGEZ:
		return self._abitanti

	def set_abitanti(self, abitanti: IntGEZ) -> None:
		self._abitanti = abitanti

# colegamento con class Aeroporto, associazione - aerop_citta

	def get_elenco_aeroporti(self) -> frozenset['aerop_citta._link']:
		return frozenset(self._elenco_aeroporti)
	
	def get_tutti_aeroporti(self) -> frozenset[Aeroporto]:
		return frozenset({link.get_aeroporto().get_nome() for link in self._elenco_aeroporti})
	
	def _aggiorna_elenco_aeroporti(self, link:'aerop_citta._link'):
		# caso di errore
		if link.get_citta() != self:
			raise ValueError(f"Link fornito non riguarda citta {self.get_nome()} ")
		if link in self._elenco_aeroporti:
			raise ValueError(f"Errore, il link è gia presnte nel elenco")
		self._elenco_aeroporti.add(link)

	def _aggiorna_elenco_vecchi_aeroporti(self, link:'aerop_citta._link'):
		# caso di errore
		if link.get_citta() != self:
			raise ValueError(f"Link fornito non riguarda citta {self.get_nome()} ")	
		if link in self._elenco_vecchi_aeroporti:
			raise ValueError(f"Errore, il link è gia presnte nel elenco")	
		self._elenco_vecchi_aeroporti.add(link)

	def _solo_remove_link_aerop_citta(self, link:'aerop_citta._link') -> None:
		# caso di errore
		if link.get_citta() != self:
			raise ValueError(f"Link fornito non riguarda citta {self.get_nome()} ")		
		if link in self._elenco_aeroporti:
			self._elenco_aeroporti.remove(link)	

# collegamento con class Nazione, associazione - cit_naz

	def get_link_cit_naz(self) -> cit_naz._link:
		return self._nazione_citta

	def set_nazione(self, nazione:Nazione) -> None:
		if self._nazione_citta:
			vechia_nazione: Nazione = self.get_link_cit_naz().get_nazione()
			vechia_nazione._remove_link_elenco_citta(self.get_link_cit_naz())
		link: cit_naz._link = cit_naz._link(self, nazione)
		self._nazione_citta = link
		nazione._aggiorna_link_elenco_citta(link)

	def get_nazione(self) -> Nazione:
		return self.get_link_cit_naz().get_nazione()

	def _remove_link_cit_naz(self, link:cit_naz._link) -> None:
		if link.get_citta() != self:
			raise ValueError(f" Il link non riguarda citta {self.get_nome()}")
		self._nazione_citta = None
		link.get_nazione()._remove_link_elenco_citta(link)


	def __str__(self) -> str:
		return f"Citta: {self.get_nome()}, abitanti: {self.get_abitanti()}, nazione: {self.get_nazione().get_nome()}"

	def __repr__(self) -> str:
		return f"Citta('{self.get_nome()}', {self.get_abitanti()}"


class Nazione:
	_nome: str    # noto alla nascita / mutabile
	_elenco_citta: set[cit_naz._link]  #certamente???? non noto alla nascita / mutabile

	def __init__(self, nome: str) -> None:
		self.set_nome(nome)
		self._elenco_citta = set()

	def get_nome(self) -> str:
		return self._nome

	def set_nome(self, nome: str) -> None:
		self._nome = nome

# collegamento con class Citta, associazione - cit_naz

	def get_link_cit_naz(self) -> frozenset[cit_naz._link]:
		return frozenset(self._elenco_citta)
	
	def get_tutte_citta(self) -> frozenset[Citta]:
		# tutte_citta: set[Citta] = set()
		# for link in self._elenco_citta:
		# 	tutte_citta.add(link.get_citta())
		# return frozenset(tutte_citta)
		return frozenset({link.get_citta().get_nome() for link in self._elenco_citta})

	def _aggiorna_link_elenco_citta(self, link:cit_naz._link) -> None:
		if link.get_nazione() != self:
			raise ValueError(f"Il link non riguarda la nazione {self.get_nome()}")
		if link in self._elenco_citta:
			raise ValueError(f"La citta gia presente nella nazione {self.get_nome()}")
		self._elenco_citta.add(link)

	def _remove_link_elenco_citta(self, link:cit_naz._link) -> None:
		if link.get_nazione() != self:
			raise ValueError(f"Il link non riguarda la nazione {self.get_nome()}")
		if link not in self._elenco_citta:
			raise ValueError(f"La citta non è presente nella nazione {self.get_nome()}")
		self._elenco_citta.remove(link)

	def crea_link_cit_naz(self, citta:Citta) -> None:
		citta.set_nazione(self)

	def __str__(self) -> str:
		return f"Nazione: {self.get_nome()}, elenco citta: {self.get_tutte_citta()}"
	  
	def __repr__(self) -> str:
		return f"Nazione({self.get_nome()}"