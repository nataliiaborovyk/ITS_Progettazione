from __future__ import annotations

from custom_types import *
from datetime import date

class Persona:
    _nome: str
    _cognome: str
    _cf: CodiceFiscale
    _nascita: date # <<immutable>>
    _is_uomo: bool  # da fusione
    _is_donna: bool # da fusione
    _maternita: IntGEZ | None # da fusione con Donna
    _posizione_militare: PosizioneMilitare | None # da fusione con Uomo e aggregazione di pos_uomo

    def __init__(self, *, nome: str, cognome: str, cf: CodiceFiscale, nascita: date,
                 maternita: IntGEZ|None = None,
                 posizione_militare: PosizioneMilitare | None=None) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_cf(cf)
        self._nascita = nascita

        self._is_donna = False
        self._is_uomo = False
        self._maternita = maternita
        self._posizione_militare = posizione_militare

        if maternita is not None:
            self._is_donna = True
        if posizione_militare is not None:
            self._is_uomo = True

        if not (self.is_uomo() or self.is_donna()):   # vincolo complete
            # [V.Persona.fusione]
            # Per ogni p: Persona: p.is_donna ==True or p.is_uomo==True
            raise ValueError("Ogni persona deve essere uomo, donna o entrambi!")

    def add_genere_donna(self, maternita: IntGEZ) -> None:
        if self.is_donna():
            raise RuntimeError("Era già una donna!")
        self._maternita = maternita
        self._is_donna = True


    def add_genere_uomo(self, pos_mil: PosizioneMilitare) -> None:
        if self.is_uomo():
            raise RuntimeError("Era già un uomo!")
        self._posizione_militare = pos_mil
        self._is_uomo = True

    def remove_genere_donna(self) -> None:
        if not self.is_donna():
            raise RuntimeError("Non era una donna!")
        if not self.is_uomo():
            raise RuntimeError("Non può rimanere senza genere!")
        self._maternita = None
        self._is_donna = False

    def remove_genere_uomo(self) -> None:
        if not self.is_uomo():
            raise RuntimeError("Non era un uomo!")
        if not self.is_donna():
            raise RuntimeError("Non può rimanere senza genere!")
        self._posizione_militare = None
        self._is_uomo = False

    def is_uomo(self) -> bool:
        return self._is_uomo

    def is_donna(self) -> bool:
        return self._is_donna

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome

    def set_cf(self, cf: CodiceFiscale) -> None:
        self._cf = cf

    def maternita(self) -> IntGEZ:
        if not self.is_donna():
            raise RuntimeError("Non era una donna!")
        return self._maternita

    def posizione_militare(self) -> PosizioneMilitare:
        if not self._is_uomo:
            raise RuntimeError("Non era una uomo!")
        return self._posizione_militare

class PosizioneMilitare:
    _nome: str # id immutabile

    def __init__(self, nome: str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome