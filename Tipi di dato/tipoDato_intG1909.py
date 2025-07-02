from typing import Self

class IntG1909(int):

    def __new__(cls, year: Self | int | float | str | bool) -> Self:
        
        value: int = super().__new__(cls, year)
        
        if value < 1909 or value > 2100:
            raise ValueError("Errore, anno deve essere tra 1909 e 2010")
        return value

    def __str__(self) -> str:
        return str(int(self))
    
    def __repr__(self) -> str:
        return f"IntG1909({int(self)})"
    
if __name__ == "__main__":
    d1:IntG1909 =IntG1909(1980)
    print(d1)

    # d2:IntG1909 =IntG1909(1900)
    # print(d2)

    d3:IntG1909 =IntG1909(1980)
    print(d3)

    print(d1 == d3)
    
    d4:IntG1909 =IntG1909(2010)
    print(d4)

    print(d1 == d3)

    elenco:set = {d1, d3, d4}
    print(elenco)