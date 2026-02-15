from typing import Self

class IntGZ(int):
    
    def __new__(cls, v: int | float | str | Self) -> Self:
        
        value: int = super().__new__(cls,v)
        
        if value <= 0:
            raise ValueError(f"Error, valore deve essere maggiore di 0")
        return value
    
    def __str__(self) -> str:
        return str(int(self))
    
    def __repr__(self) -> str:
        return f"IntGZ({int(self)})"
    
if __name__ == "__main__":

    v1: IntGZ = IntGZ(145)
    print(v1)

    # v2: IntGZ = IntGZ(-145)
    # print(v2)

    v3: IntGZ = IntGZ("145")
    print(v3)

    v4: IntGZ = IntGZ(145.0)
    print(v4)

    v5: IntGZ = IntGZ(v1)
    print(v5)

    print(v1 == v3)

    elenco:set = {v1, v3, v4, v5}
    print(elenco)


    

