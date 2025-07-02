from tipoDato_intGEZ import IntGEZ

class Citta:

    _nome:str    # noto alla nascita / mutabile
    _abitanti:IntGEZ   # noto alla nascita / mutabile

    def __init__(self, nome:str, abitanti:IntGEZ) -> None:
        self.setNome = nome
        self.setAbitanti = abitanti
    
    @property
    def getNome(self) -> str:
        return self._nome
    
    @getNome.setter
    def setNome(self, nome:str) -> None:
        self._nome = nome.capitalize()
    
    @property
    def getAbitanti(self) -> IntGEZ:
        return self._abitanti
    
    @getNome.setter
    def setAbitanti(self, abitanti:IntGEZ) -> None:
        self._abitanti = abitanti
    
    def __str__(self) -> str:
        return f"Citta: {self.getNome}, abitanti: {self.getAbitanti}"

    def __repr__(self) -> str:
        return f"Citta('{self.getNome}', {self.getAbitanti})"
    
if __name__ == "__main__":

    c1:Citta = Citta("Roma", IntGEZ(2746789))
    print(c1)

    c2:Citta = Citta("roma", IntGEZ(2746789))
    print(c2)

    c3:Citta = Citta("1111", IntGEZ(2746789))  # ??? chi controlla creazione dei oggetti ???
    print(c3)

    print(c1 == c2)

    elenco_citta:set = {c1, c2}   # ??? due oggetti uguali possono esistere o devo inserire eq e hash ???
    print(elenco_citta)