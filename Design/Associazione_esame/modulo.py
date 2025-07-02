
class Modulo:
    _codice: str

    def __init__(self, codice:str) -> None:
        self._codice = codice

    def codice(self) -> str:
        return self._codice
    
    def __hash__(self):
        return hash(self.codice)