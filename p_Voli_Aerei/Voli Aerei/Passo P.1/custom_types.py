from typing import Self
import re

class IntGZ(int):
	# Tipo di dato specializzato Intero > 0

	def __new__(cls, v: Self | int | float | str | bool) -> Self:

		value: int = super().__new__(cls, v)

		if value <= 0:
			raise ValueError(f"The value {v} must be greater than zero")
		return value

class IntGEZ(int):
	# Tipo di dato specializzato Intero >= 0

	def __new__(cls, v: Self | int | float | str | bool) -> Self:

		value: int = super().__new__(cls, v)

		if value < 0:
			raise ValueError(f"The value {v} must be greater than or equal to zero")
		return value


class IntG1900(int):
	# Tipo di dato specializzato Intero > 1900

	def __new__(cls, v: Self | int | float | str | bool) -> Self:

		value: int = super().__new__(cls, v)

		if value <= 1900:
			raise ValueError(f"The value {v} must be greater than 1900")
		return value





