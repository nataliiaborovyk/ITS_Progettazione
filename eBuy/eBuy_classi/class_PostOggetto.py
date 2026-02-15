
from abc import ABC, abstractmethod
from datetime import datetime
from tipoDato_FloatGez import FloatGez
from tipoDato_IntGEZ import IntGEZ
from tipoDato_Condizioni import Condizioni
import random

class PostOggetto(ABC):
    
    _descrizione: str # noto alla nascita
    _prezzo: FloatGez  # noto alla nascita
    _anni_garanzia: IntGEZ #noto alla nascita
    _publicazione: datetime # <<imm>> / noto alla nascita
    _is_nuovo: bool  # <<imm>> / noto alla nascita
    _condizioni: Condizioni | None # non noto alla nascita
    # aggiungo id per identificare post
    _id: int
    _id_usati: set[int]

    _id_usati = set()  # attributo di classe

    @classmethod
    def _genera_id(cls) -> int:
        while True:
            id = random.randint(1, 1000)
            if id not in cls._id_usati:
                cls._id_usati.add(id)
                return id


    def __init__(self, *, 
                descrizione:str, 
                prezzo:FloatGez, 
                anni_garanzia:IntGEZ,
                condizioni: Condizioni | None = None ) -> None:
        
        if condizioni is None:
            self._is_nuovo = True
        else:
            self._is_nuovo = False

        self._publicazione = datetime.now()
        self.set_descrizione(descrizione)
        self.set_prezzo(prezzo)
        self._set_anni_garanzia_condizioni(anni_garanzia, condizioni)
        self._id = self._genera_id()


    def _set_anni_garanzia_condizioni(self, anni_garanzia: IntGEZ, condizioni: Condizioni | None = None) -> None:
        if self._is_nuovo == True:
            if condizioni is not None:
                raise ValueError("A ogetto nuovo non c'è bisogno di specificare le condizioni")
            if anni_garanzia < 2:
                raise ValueError("un ogetto nuovo deve avere almeno 2 anni di garanzia")
            self._anni_garanzia = anni_garanzia
            self._set_condizioni(condizioni)
        else:
            self._anni_garanzia = anni_garanzia
            if condizioni is None:
                raise ValueError("Bisogna inserire le condizioni del ogetto usato")
            self._set_condizioni(condizioni)

    @abstractmethod
    def _puo_cambiare(self) -> bool: # serve per controllare se esiste almeno un bid o per futuri controlli in comprasubito
        pass

    def set_descrizione(self, descrizione: str) -> None:
        self._descrizione = descrizione

    def set_prezzo(self, prezzo: FloatGez) -> None:
        self._prezzo = prezzo
    
    def _set_condizioni(self, condizioni: Condizioni) -> None:
        self._condizioni = condizioni

    @abstractmethod
    def get_tipoPostOggetto(self) -> str:
        pass

    def get_id(self) -> int:
        return self._id
    
    def get_publicazione(self) -> datetime:
        return self._publicazione

    def get_descrizione(self) -> str:
        return self._descrizione
    
    def get_prezzo(self) -> FloatGez:
        return round(self._prezzo, 2)
    
    def get_is_nuovo(self) -> bool:
        return self._is_nuovo
    
    def get_anni_garanzia(self) -> IntGEZ:
        return self._anni_garanzia
    
    def get_condizioni(self) -> Condizioni:
        if self._condizioni == None:
            raise ValueError("La condizione non è aggiunta")
        return self._condizioni

    
    def __str__(self) -> str:
        data: datetime = self.get_publicazione().strftime("%Y-%m-%d %H:%M") #formatto data
        result = f"Id: {self.get_id()}\n"
        result += f"publicazione: {data}\n"
        result += f"descrizione: {self.get_descrizione()}\n"
        result += f"prezzo: {self.get_prezzo()}\n"
        result += f"anni garanzia: {self.get_anni_garanzia()}\n"
        if self.get_is_nuovo():
            result += "stato: nuovo\n"
        else:
            result += f"stato: usato \ncondizioni: {self.get_condizioni()}\n"
        return result


