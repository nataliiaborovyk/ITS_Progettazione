from typing import Self
from datetime import datetime
from typing import *

def buinding_DataOra(anno_inizio: int, anno_fine: int) -> Type:

    class DataOra(datetime):

        def __new__(cls, anno:int, 
                        mese:int,
                        giorno:int,
                        ora:int,
                        minuti:int) -> Self:
            
            if anno < anno_inizio or anno > anno_fine:
                raise ValueError(f"Errore, anno deve essere tra {anno_inizio} e {anno_fine}")
            try:
                return super().__new__(cls, anno, mese, giorno, ora, minuti)
            except ValueError as e:
                raise ValueError(f"Errore, dati inseriti {e} non sono corretti")

        def __str__(self) -> str:
            return f"Data e ora: {self.strftime('%d/%m/%Y %H:%M')}"
        
        def __repr__(self) -> str:
            return f"DataOra({self.strftime('%d/%m/%Y %H:%M')})"
        
    return DataOra
        
if __name__ == "__main__":

    DataOra_1900_2010 = buinding_DataOra(1900, 2100)
    print(DataOra_1900_2010)
    
    d1: datetime = DataOra_1900_2010(2024,2,28,15,45)
    print(d1)

    # d2: datetime = DataOra_1900_2010(2024,2,31,15,45)
    # print(d2)

    d3: datetime = DataOra_1900_2010(2024,2,28,15,45)
    print(d3)

    d4: datetime = DataOra_1900_2010(2004,2,29,20,00)
    print(d4)

    print(d1 == d3)

    elenco:set = {d1, d3, d4}
    print(elenco)