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
	_compania_aerea: volo_comp._link # noto alla nascita [1..1] / immutabile
	_aeroporto_arrivo: arrivo._link # noto alla nascita [1..1] / immutabile
	_aeroporto_partenza: partenza._link # noto alla nascita [1..1] / immutabile

	def __init__(self, codice: str, durata_minuti: IntGZ, compania:CompagniaAerea, 
			  	aerop_arrivo:Aeroporto, aerop_partenza:Aeroporto) -> None:
		self._codice = codice
		self.set_durata_minuti(durata_minuti)
		self._compania_aerea = None     #serve per evitare un errore al momento di creazione del link
		if compania is None:
			raise ValueError("Error, bisogna indicare la compania aerea del volo")
		self._crea_link_volo_comp(compania)
		self._aeroporto_arrivo = None
		self._crea_link_arrivo(aerop_arrivo)
		self._aeroporto_partenza = None
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

	def get_link_compania_aerea(self) -> volo_comp._link:
		return self._compania_aerea
	
	def get_compania_aerea(self) -> CompagniaAerea:
		return self.get_link_compania_aerea().get_compania()
	
	def _crea_link_volo_comp(self, compania:CompagniaAerea) -> volo_comp._link: # o None ??????
		if self.get_link_compania_aerea() is not None:
			raise ValueError("Non si puo modificare compania aerea del volo")
		link: volo_comp._link = volo_comp._link(self, compania) 
		self._compania_aerea = link
		compania._aggiorna_elenco_voli(link)

	# ?????????????????????????????????????????????????????????????????????????????
	# serve solo nel caso se viene eliminato il ogetto volo, per salvare il link nel _elenco_vecchi_voli
	def _remove_link_volo_comp(self, link:volo_comp._link) -> None:
		# if not _for_delete:
		# 	raise PermissionError("Non è permesso rimuovere il collegamento tranne durante l'eliminazione del volo.")
		if link.get_volo() != self:
			raise ValueError(f"Il link non riguarda il volo {self.get_codice()}")
		if self.get_link_compania_aerea() == link:
			self._compania_aerea = None
			link.get_compania()._remove_link_volo_comp(link)
			link.get_compania()._aggiorna_elenco_vecchi_voli(link)

# collegamento con class Aeroporto, associazione - arrivo

	def get_link_arrivo(self) -> arrivo._link:
		return self._aeroporto_arrivo
	
	def get_aeroporto_arrivo(self) -> Aeroporto:
		return self.get_link_arrivo().get_aeroporto()
	
	def _crea_link_arrivo(self, aerop_arrivo:Aeroporto) -> None:
		if self.get_link_arrivo() is not None:
			raise ValueError("Non si puo modificare compania aerea del volo")
		for link in aerop_arrivo.get_elenco_voli_arrivo():
			if link.get_volo().get_codice() == self.get_codice():
				raise ValueError(f"Il codice di volo deve essere univoco")
		link: arrivo._link = arrivo._link(aerop_arrivo, self)
		self._aeroporto_arrivo = link
		aerop_arrivo._aggiorna_elenco_voli_arrivo(link)


# collegamento con class Aeroporto, associazione - partenza

	def get_link_partenza(self) -> partenza._link:
		return self._aeroporto_partenza
	
	def get_aeroporto_partenza(self) -> Aeroporto:
		return self.get_link_partenza().get_aeroporto()
	
	def _crea_link_partenza(self, aerop_partenza:Aeroporto) -> None:
		if self.get_link_partenza() is not None:
			raise ValueError("Non si puo modificare aeroporto do partenza del volo")
		for link in aerop_partenza.get_elenco_voli_partenza():
			if link.get_volo().get_codice() == self.get_codice():
				raise ValueError(f"Il codice di volo deve essere univoco")
		link: partenza._link = partenza._link(aerop_partenza, self)
		self._aeroporto_partenza = link
		aerop_partenza._aggiorna_elenco_voli_partenza(link)



	def __str__(self) -> str:
		return f"Codice volo: {self.get_codice()}, durata: {self.get_durata_minuti()} minuti, compania: {self.get_compania_aerea().get_nome()}"
    
