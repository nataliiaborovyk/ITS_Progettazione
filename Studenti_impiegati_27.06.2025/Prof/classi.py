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

        if maternita is not None:
            self.set_attributi_donna(maternita)
        else:
            self.remove_attributi_donna()
        if posizione_militare is not None:
            self.set_attributi_uomo(posizione_militare)
        else:
            self.remove_attributi_uomo()

        if not (self.is_uomo() or self.is_donna()):
            # [V.Persona.fusione]
            # Per ogni p: Persona: p.is_donna ==True or p.is_uomo==True
            raise ValueError("Ogni persona deve essere uomo, donna o entrambi!")

    def set_attributi_donna(self, maternita: IntGEZ) -> None:
        # [V.Persona.fusione]
        # Per ogni p: Persona:
        # - p.is_donna == True <==> p.maternità è valorizzato

        self._is_donna = True
        self._maternita = maternita

    def remove_attributi_donna(self) -> None:
        try:
            if not self.is_donna():
                raise RuntimeError("La persona non era una donna!")
        except AttributeError:
            pass

        try:
            if not self.is_uomo():
                raise RuntimeError("La persona non era anche un uomo, quindi non può rimanere senza un genere!")
        except AttributeError:
            pass
        self._is_donna = False
        del self._maternita

    def set_attributi_uomo(self, posizione_militare: PosizioneMilitare) -> None:
        # [V.Persona.fusione]
        # Per ogni p: Persona:
        #   p.is_uomo == True <==> p è coinvolto in un link 'pos_uomo'
        self._is_uomo = True
        self._posizione_militare = posizione_militare

    def remove_attributi_uomo(self) -> None:
        try:
            if not self.is_uomo():
                raise RuntimeError("La persona non era una uomo!")
        except AttributeError:
            pass

        try:
            if not self.is_donna():
                raise RuntimeError("La persona non era anche un donna, quindi non può rimanere senza un genere!")
        except AttributeError:
            pass

        self._is_uomo = False
        del self._posizione_militare


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




class PosizioneMilitare:
    _nome: str # id immutabile

    def __init__(self, nome: str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome
    

