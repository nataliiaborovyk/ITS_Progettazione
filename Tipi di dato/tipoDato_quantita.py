from typing import Self

class Quantita(int):
    def __new__(cls, q:int|Self) -> Self:
        if not isinstance(q, int):
            raise ValueError("Errore, inserisci valore intero maggiore uguale a 0")
        if q < 0:
            raise ValueError(f"Errore, valore di quantita ({q}) deve essere >= 0")
        return int.__new__(cls, q)
    
    def __str__(self) -> str:
        return f"Crediti: {int(self)}"
    
if __name__ == "__main__":

    q1:Quantita = Quantita(4)
    print(q1)

    # q2:Quantita = Quantita(-4)
    # print(q2)

    # q3:Quantita = Quantita("4")
    # print(q3)

    q4:Quantita = Quantita(4)
    print(q4)
 
    print(q1 == q4)

    q5:Quantita = Quantita(4)
    print(q5)

    q6:Quantita = Quantita(17)
    print(q6)

    elenco:set = {q1,q4,q5,q6}
    print(elenco)