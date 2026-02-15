
from custom_types import CodiceFiscale, IntGEZ
from datetime import date

class Persona:
    _nome:str
    _cognome:str
    _cf: CodiceFiscale
    _nascita: date