from typing import Self
import re
class Importo(float):
	def __new__(cls, v:int|float|str)->Self:
		if v < 0:
			raise ValueError(f"Value v == {v} must be >= 0")
		return float.__new__(cls, v)

class Telefono(str):
	def __new__(cls, v:str)->Self:
		if not re.fullmatch(r'\+?[0-9]+', v):
			raise ValueError(f"Value v == {v} does not satisfy the standard")
		return str.__new__(cls, v)