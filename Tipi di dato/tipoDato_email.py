from typing import Self
import re

class Email(str):

    def __new__(cls, em: str | Self) -> Self:

        em = em.lower()

        if not re.fullmatch(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", em):
            raise ValueError(f"Errore, {em} non è un email valido")
        return super().__new__(cls, em)
    
    def __str__(self) -> str:
        return f"Email: {super().__str__()}"
    
    def __repr__(self) -> str:
        return f"Email({super().__str__()})"


if __name__ == "__main__":

    e1: Email = Email("abcd743@hom.com")
    print(e1)

    e2: Email = Email("ABCD743@hom.com")
    print(e2)

    # e3: Email = Email("3ergwgwgw88877776@fsfsefe)()())")
    # print(e3)

    # e4: Email = Email("3888777m66")
    # print(e4)

    elenco:set = {e1, e2}
    print(elenco)