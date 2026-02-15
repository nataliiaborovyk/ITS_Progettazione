from tipoDato_intG1909 import IntG1909

class CompaniaAerea:

    _nome:str    # noto alla nascita / mutabile / {id}
    _aa:IntG1909     # noto alla nascita / immutabile

    elenco_nomi:list = []   # ??? forse meglio usare set???

    def __init__(self, nome: str, aa: IntG1909) -> None:

        self._aa = aa
        self.setNome(nome)
    
    def getAa(self) -> IntG1909:
        return self._aa
    
    def getNome(self) -> str:
        return self._nome
    
    def setNome(self, nome:str) -> None:
        nome = nome.capitalize()
        if nome in self.elenco_nomi:
            raise ValueError(f"Errore, nome {nome} è gia stato inserito")
        self._nome = nome
        self.elenco_nomi.append(nome)   # se meglio usare set allora - self.elenco_nomi.add(nome)

    def __str__(self) -> str:
        return f"Compania aerea: {self.getNome()}, anno di fondazione: {self.getAa()}"

if __name__ == "__main__":

    c1: CompaniaAerea = CompaniaAerea("lufthansa", IntG1909(1953))
    print(c1)

    # c2: CompaniaAerea = CompaniaAerea("LUFthansa", IntG1909(1953))
    # print(c2)