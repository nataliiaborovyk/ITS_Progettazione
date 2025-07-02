from typing import Self

class Nazione:

    _nome: str # noto alla nascita / mutabile / {id}
    _elenco_nazioni: dict[str, 'Nazione'] = {}

    def __new__(cls, nome:str) -> Self:
        nome = nome.capitalize()
        if nome in cls._elenco_nazioni:
            raise ValueError(f"Errore, nazione con nome {nome} gia esiste")
        return super().__new__(cls)


    def __init__(self, nome:str)  -> None:
        if not hasattr(self, "_nome"):  # controllo se un ogetto ha attributo  nome
            self._nome = None
            self.setNome = nome

    @property              #  decoratore  .nome == .getNome()
    def getNome(self)  -> str:
        return self._nome

    @getNome.setter          
    def setNome(self, nome) -> None:
        nome = nome.capitalize()
        
        if nome in self._elenco_nazioni:
            raise ValueError(f"Errore, la nazione con nome {nome} gia esiste")
        
        if self._nome is not None:
            del self._elenco_nazioni[self._nome]

        self._nome = nome
        self._elenco_nazioni[nome] = self

    def __str__(self) -> str:
        return f"Nazione: {self.getNome}"
    
    def __repr__(self) -> str:
        return f"Nazione({self.getNome})"
    
if __name__ == "__main__":

    n1: Nazione = Nazione("italia")
    print(n1)

    # n2: Nazione = Nazione("ITALIA")
    # print(n2)

    n3: Nazione = Nazione("1111")   # un problema
    print(n3)    

 # solo alcuni utenti (admin) possono creare o cambiare il nome ???? 

    n4: Nazione = Nazione("ital")
    print(n4)
    n4.nome = "Italia"
    print(n4)


