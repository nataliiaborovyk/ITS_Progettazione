from dataclasses import dataclass

@dataclass(frozen=True)
class Volo:
    def __init__(self,codice:str,durata:int):
        self.codice=codice
        self.durata=durata

@dataclass(frozen=True)
class Aereoporto:
    def __init__(self, codice:str,nome:str):
        self.codice=codice
        self.nome=nome
   

@dataclass(frozen=True)
class CompagniaAerea:
    def __init__(self,nome:str,anno_fondazione:int):
        self.nome=nome
        self.anno_fondazione=anno_fondazione
        
        if self.anno_fondazione<1900:
            raise ValueError("le compagnie aeree prima del 1900 non esistevano")
        
@dataclass
class Citta:
    def __init__(self,nome:str,abitanti:int):
        self.nome=nome
        self.abitanti=abitanti
       
        if self.abitanti<0:
            raise ValueError("gli abitanti non possono un valore negativo")

@dataclass
class Nazione:
    def __init__(self,nome:str):
        self.nome=nome
        
        