from abc import ABC, abstractmethod
from datetime import datetime
import random

class Utente(ABC):

    _username: str # <<imm>> / noto alla nascita
    _registrazione: datetime # <<imm>> / noto alla nascita


    def __init__(self, username:str) -> None:
        self._username = username
        self._registrazione = datetime.now()

    def get_username(self) -> str:
        return self._username

    def get_registrazione(self) -> datetime:
        return self._registrazione
    
    @abstractmethod
    def get_tipo_utente(self) -> str:
        pass

    def __str__(self) -> str:
        data: datetime = self.get_registrazione().strftime("%Y-%m-%d %H:%M")
        return f"Utente: {self.get_username()}, registrazione: {data}, tipo: {self.get_tipo_utente()}"
    
    def __repr__(self) -> str:
        data: datetime = self.get_registrazione().strftime("%Y-%m-%d")
        return f"Utente({self.get_username}, {data}, {self.get_tipo_utente()})"