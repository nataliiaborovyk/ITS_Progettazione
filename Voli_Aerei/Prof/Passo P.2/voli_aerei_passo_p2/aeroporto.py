class Aeroporto:
	_codice: str # <<immutabile>> noto alla nascita
	_nome: str # noto alla nascita

	def __init__(self, codice: str, nome: str) -> None:
		self._codice = codice
		self.set_nome(nome)

	def nome(self) -> str:
		return self._nome

	def codice(self) -> str:
		return self._codice

	def set_nome(self, nome: str) -> None:
		self._nome = nome
