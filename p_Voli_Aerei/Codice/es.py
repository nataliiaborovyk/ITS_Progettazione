class Nazione:
    _nomi_usati = set()

    def __init__(self, nome):
        nome = nome.capitalize()
        if nome in self._nomi_usati:
            raise ValueError(f"{nome} già esiste")
        self._nome = nome
        self._nomi_usati.add(nome)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        nuovo_nome = nuovo_nome.capitalize()
        if nuovo_nome in self._nomi_usati:
            raise ValueError(f"{nuovo_nome} già esiste")
        # rimuovi il vecchio nome
        self._nomi_usati.remove(self._nome)
        # aggiorna il nome
        self._nome = nuovo_nome
        self._nomi_usati.add(nuovo_nome)

class Nazione:
    _nomi_usati = set()

    def __init__(self, nome):
        self.nome = nome  # usa direttamente il setter

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        nuovo_nome = nuovo_nome.capitalize()

        # Se è già stato impostato e il nome non cambia, non fare nulla
        if hasattr(self, "_nome") and nuovo_nome == self._nome:
            return

        if nuovo_nome in self._nomi_usati:
            raise ValueError(f"{nuovo_nome} già esiste")

        # Se stiamo cambiando nome, rimuovi il vecchio
        if hasattr(self, "_nome"):
            self._nomi_usati.remove(self._nome)

        self._nome = nuovo_nome
        self._nomi_usati.add(nuovo_nome)


class Nazione:
    _istanze: dict = {}

    def __new__(cls, nome: str):
        nome = nome.capitalize()
        if nome in cls._istanze:
            return cls._istanze[nome]
        self = super().__new__(cls)
        return self

    def __init__(self, nome: str):
        # solo se non è già stato inizializzato
        if not hasattr(self, "_nome"):
            self._nome = None
            self.nome = nome  # usa il setter

    @property       #  decoratore .nome == .getNome()
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome: str):
        nuovo_nome = nuovo_nome.capitalize()

        # Se il nome è già in uso da un'altra istanza
        if nuovo_nome in self._istanze and self._istanze[nuovo_nome] is not self:
            raise ValueError(f"La nazione '{nuovo_nome}' esiste già.")

        # Rimuovi il vecchio nome dal dizionario (se esiste)
        if self._nome is not None:
            del self._istanze[self._nome]

        # Imposta il nuovo nome e aggiorna il dizionario
        self._nome = nuovo_nome
        self._istanze[nuovo_nome] = self

    def __str__(self):
        return self._nome

    def __repr__(self):
        return f"Nazione('{self._nome}')"
