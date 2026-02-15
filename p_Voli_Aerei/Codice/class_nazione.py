class Nazione:

    _nome: str # noto alla nascita / mutabile
    _elenco_nazioni: list = []

    def __init__(self, nome:str):
        self.setNome(nome)


    def getNome(self) -> str:
        return self._nome
    
    def setNome(self, nome) -> None:
        nome = nome.capitalize()
        if nome in self._elenco_nazioni:
            raise ValueError(f"Errore, {nome} è gia stato inserito")
        self._nome = nome
        self._elenco_nazioni.append(nome)

    def __str__(self) -> str:
        return f"Nazione: {self.getNome()}"
    
    def __repr__(self) -> str:
        return f"Nazione({self.getNome()})"
    
if __name__ == "__main__":

    n1: Nazione = Nazione("italia")
    print(n1)

    # n2: Nazione = Nazione("ITALIA")
    # print(n2)

    n2: Nazione = Nazione("1111")   # un problema
    print(n2)    

 # solo alcuni utenti (admin) possono creare o cambiare il nome ???? 



