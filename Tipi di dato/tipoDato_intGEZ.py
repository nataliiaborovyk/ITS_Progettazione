from typing import Self

class IntGEZ(int):
    def __new__(cls, v: Self | int | float | str | bool) -> Self:
        
        value: int = super().__new__(cls, v)

        if value < 0:
            raise ValueError(f"Errore, il valore deve essere >= 0")
        return value
    
    def __str__(self) -> str:
        return str(int(self))
    
    def __repr__(self) -> str:
        return f"IntGEZ({int(self)})"
    
if __name__ == "__main__":

    v1:IntGEZ = IntGEZ(4)
    print(v1)

    # v2:IntGEZ = IntGEZ(-4)
    # print(v2)

    # v3:IntGEZ = IntGEZ("4")
    # print(v3)

    v4:IntGEZ = IntGEZ(4)
    print(v4)

    v5:IntGEZ = IntGEZ(4)
    print(v5)

    v6:IntGEZ = IntGEZ(17)
    print(v6)

    print(v1 == v4)

    elenco:set = {v1,v4,v5,v6}
    print(elenco)