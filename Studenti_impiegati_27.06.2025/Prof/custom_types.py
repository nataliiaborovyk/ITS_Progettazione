from __future__ import annotations

from typing import Any
from typing import Self
import re

'''
CodiceAeroporto(str)
CodiceVolo(str)
IntG1909(int)
IntGEZ(int)
IntGZ(int)
Telefono(str)
Email(str)
CodiceFiscale
'''

class CodiceAeroporto(str):

    def __new__(cls, cod: str | Self) -> Self:
        codice:str = cod.upper().strip()
        if not re.fullmatch(r'^[A-Z]{3,4}$', codice):
            raise ValueError(f"Errore, {codice} non è un codice di aeroporto")
        return super().__new__(cls, codice)
    
    def __str__(self) -> str:
        return  super().__str__()   # oppure str(self)
    
    def __repr__(self) -> str:
        return f"CodiceAeroporto({ super().__str__()})"
    
class CodiceVolo(str):

    def __new__(cls, cod: str | Self) -> Self:
        codice:str = cod.upper().strip()
        if not re.fullmatch(r'^[A-Z]{2}\d{1,4}$', codice):
            raise ValueError(f"Errore, {codice} non è un codice di volo")
        return super().__new__(cls, codice)
    
    def __str__(self) -> str:
        return  super().__str__()  # oppure str(self)
    
    def __repr__(self) -> str:
        return f"CodiceVolo({ super().__str__()})"
    
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
    
class Telefono(str):
     
	def __new__(cls, tel: str | Self) -> Self:
		if re.fullmatch(r'^\d{10}$', tel):
			return super().__new__(cls, tel)
		raise ValueError(f"{tel} non è un numero di telefono italiano valido")


class Email(str):
     
	def __new__(cls, v: str | Self) -> Self:
		if re.fullmatch(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", v):
			return super().__new__(cls, v)
		raise ValueError(f"{v} non è un indirizzo email valido")
     


class CodiceFiscale:
   
    def __init__(self, cf:str) -> None:
       
        if cf is None:
            raise ValueError("Errore, codice fiscale non puo essere None")
        if not isinstance(cf, str):
            raise ValueError("Errore, inserisci codice fiscale in formato stringa ")
        
        cf = cf.upper()
        modello_cf: str = r"^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$"
        if not re.match(modello_cf, cf):
            raise ValueError(f"Errore, il codice fiscale inserito {cf} non è valido, riprova")
        self._cf = cf

    def get_cf(self) -> str:
        return self._cf
    
    def __hash__(self) -> int:
        return hash(self._cf)
    
    def __eq__(self, other:Any) -> bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return self._cf == other._cf
    
    def __str__(self) -> str:
        return self._cf
    
    def __repr__(self) -> str:
        return f"Codice Fiscale = {self.get_cf()}"
    