from __future__ import annotations

from custom_types import IntGZ
from datetime import timedelta
from class_compagnia import CompagniaAerea
from ass_volo_comp import volo_comp
from class_aeroporto import Aeroporto
from ass_arrivo import arrivo
from ass_partenza import partenza

class Volo:
	_codice: str # <<immutabile>>, noto alla nascita
	_durata_minuti: IntGZ # noto alla nascita
	_link_volo_comp: volo_comp._link # noto alla nascita [1..1] / immutabile
	_link_arrivo: arrivo._link # noto alla nascita [1..1] / immutabile
	_link_partenza: partenza._link # noto alla nascita [1..1] / immutabile

	def __init__(self, codice: str, durata_minuti: IntGZ, compania:CompagniaAerea, 
			  	aerop_arrivo:Aeroporto, aerop_partenza:Aeroporto) -> None:
		self._codice = codice
		self.set_durata_minuti(durata_minuti)
		if compania is None:
			raise ValueError("Error, bisogna indicare la compania aerea del volo")
		if aerop_arrivo is None:
			raise ValueError("Error, bisogna indicare la aeroporto di arrivo!")
		if aerop_partenza is None:
			raise ValueError("Error, bisogna indicare la aeroporto di partenza!")
		self._link_volo_comp = None     #serve per evitare un errore al momento di creazione del link
		self._crea_link_volo_comp(compania)
		self._link_arrivo = None
		self._crea_link_arrivo(aerop_arrivo)
		self._link_partenza = None
		self._crea_link_partenza(aerop_partenza)

	def get_codice(self) -> str:
		return self._codice

	def get_durata_minuti(self) -> IntGZ:
		return self._durata_minuti

	def get_durata(self) -> timedelta:
		return timedelta(minutes=self.get_durata_minuti())

	def set_durata_minuti(self, durata: IntGZ) -> None:
		self._durata_minuti = durata

# collegamento con class CompaniaAerea, associazione - volo_comp

	def get_link_volo_comp(self) -> volo_comp._link:
		return self._link_volo_comp
	
	def get_compania_volo_comp(self) -> CompagniaAerea:
		return self.get_link_volo_comp().get_compania()
	
	def _crea_link_volo_comp(self, compania:CompagniaAerea) -> volo_comp._link: # o None ??????
		''' Crea link volo_comp da class volo_comp'''
		volo_comp.crea_link_volo_comp(self, compania)

	def _aggiorna_link_volo_comp(self, link:volo_comp._link) -> None:
		self._link_volo_comp = link

	# # ?????????????????????????????????????????????????????????????????????????????
	# # serve solo nel caso se viene eliminato il ogetto volo, per salvare il link nel _elenco_vecchi_voli
	# def _remove_link_volo_comp(self, link:volo_comp._link) -> None:
	# 	# if not _for_delete:
	# 	# 	raise PermissionError("Non è permesso rimuovere il collegamento tranne durante l'eliminazione del volo.")
	# 	if link.get_volo() != self:
	# 		raise ValueError(f"Il link non riguarda il volo {self.get_codice()}")
	# 	if self.get_link_link_volo_comp() == link:
	# 		self._link_volo_comp = None
	# 		link.get_compania()._remove_link_volo_comp(link)
	# 		link.get_compania()._aggiorna_elenco_vecchi_voli(link)

# collegamento con class Aeroporto, associazione - arrivo

	def get_link_arrivo(self) -> arrivo._link:
		return self._link_arrivo
	
	def get_aeroporto_arrivo(self) -> Aeroporto:
		return self.get_link_arrivo().get_aeroporto()
	
	def _crea_link_arrivo(self, aerop_arrivo:Aeroporto) -> None:
		''' Crea link arrivo da class arrivo'''
		arrivo.crea_link_arrivo(self, aerop_arrivo)

	def _aggiorna_link_arrivo(self, link: arrivo._link) -> None:
		self._link_arrivo = link


# collegamento con class Aeroporto, associazione - partenza

	def get_link_partenza(self) -> partenza._link:
		return self._link_partenza
	
	def get_aeroporto_partenza(self) -> Aeroporto:
		return self.get_link_partenza().get_aeroporto()
	
	def _crea_link_partenza(self, aerop_partenza:Aeroporto) -> None:
		''' Crea link partenza da class partenza'''
		partenza.crea_link_partenza(self, aerop_partenza)

	def _aggiorna_link_partenza(self, link: partenza._link) -> None:
		self._link_partenza = link



	def __str__(self) -> str:
		return f"Codice volo: {self.get_codice()}, durata: {self.get_durata_minuti()} minuti, compania: {self.get_link_volo_comp().get_compania().get_nome()}"
    
	def __repr__(self) -> str:
		return f"Volo(Codice:{self.get_codice()},durata:{self.get_durata_minuti()},compania:{self.get_link_volo_comp().get_compania().get_nome()})"