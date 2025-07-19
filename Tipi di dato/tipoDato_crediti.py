from typing import Self

class Crediti(int):
    def __new__(cls, c:int|Self) -> Self:
        if not isinstance(c, int):
            raise ValueError("Errore, inserisci valore intero tra 3 e 12 ")
        if c < 3 or c > 12:
            raise ValueError(f"Errore, valore crediti ({c}) deve essere tra 3 e 12")
        return int.__new__(cls, c)
    
    def __str__(self) -> str:
        return f"Crediti: {int(self)}"
    

if __name__ == "__main__":

    c1:Crediti = Crediti(10)
    print(c1)

    # c2:Crediti = Crediti(15)
    # print(c2)

    # c3:Crediti = Crediti("10")
    # print(c3)

    c4:Crediti = Crediti(10)
    print(c4)

    print(c1 == c4)
    
    c5:Crediti = Crediti(10)
    print(c5)

    c6:Crediti = Crediti(12)
    print(c6)

    c7:Crediti = Crediti(3)
    print(c7)

    elenco:set = {c1, c4, c5, c6, c7}
    print(elenco)