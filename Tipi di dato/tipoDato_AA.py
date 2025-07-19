from typing import Any


class AnnoAccademico:
    def __init__(self, inizio: int, fine:int) -> None:
       
        if inizio is None:
            raise ValueError("Errore, anno di inizio non puo essere None")
        if type(inizio) != int:
            raise ValueError("Errore, inserire anno di inizio in formato numerico tra 1950 e 2100")

        if fine is None:
            raise ValueError("Errore, anno di fine non puo essere None")
        if type(fine) != int:
            raise ValueError("Errore, inserire anno di fine in formato numerico tra 1950 e 2100")

        if not (1950 <= inizio <= 2050):
            raise ValueError("Errore, l'anno di inizio deve essere tra 1950 e 2100")
       
        if fine - inizio != 1:
            raise ValueError("Errore, l'anno accademico puo durare solo 1 anno")
       
        # if inizio > fine:
        #     raise ValueError("Errore, l'anno di inizio deve essere precedente dell'anno di fine")
       
        self._inizio = inizio
        self._fine = fine

    def get_AA(self) -> str:
        return f"{self._inizio}/{self._fine}"

    def __str__(self) -> str:
        return f"{self._inizio}/{self._fine}"
    
    def __repr__(self) -> str:
        return f"Anno Accademico = {self.get_AA()}"
    
    
    def __hash__(self) -> int:
        return hash((self._inizio, self._fine))
    
    def __eq__(self, other:Any) -> bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return self._inizio == other._inizio and self._fine == other._fine
    
if __name__ == "__main__":

    a1:AnnoAccademico = AnnoAccademico(2024,2025)
    print(a1)

    # a2:AnnoAccademico = AnnoAccademico(2022,2025)
    # print(a2)

    # a3:AnnoAccademico = AnnoAccademico(2025,2024)
    # print(a3)

    # a4:AnnoAccademico = AnnoAccademico(20240,20241)
    # # print(a4)

    # a5:AnnoAccademico = AnnoAccademico("3323",2025)
    # print(a5)

    a6:AnnoAccademico = AnnoAccademico(2024,2025)
    print(a6)

    print(a1 == a6)
    print(f"{a1.get_AA() == a6.get_AA()}") #restituisce comunque True perche le stringe sono uguali

    a7:AnnoAccademico = AnnoAccademico(2024,2025)
    print(a7)

    a8:AnnoAccademico = AnnoAccademico(2020,2021)
    print(a8)

    a9:AnnoAccademico = AnnoAccademico(2025,2026)
    print(a9)

    elenco_aa:set = {a1, a6, a7, a8, a9}
    print(elenco_aa)