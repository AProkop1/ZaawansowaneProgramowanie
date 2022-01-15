class Dietetyk:
    def __init__(self, imię: str, nazwisko: str, firma: str, nr_licencji: int):
        self._imię = imię
        self._nazwisko = nazwisko
        self._firma = firma
        self._nr_licencji = nr_licencji

    @property
    def imię(self) -> str:
        return self._imię

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def firma(self) -> str:
        return self._firma

    @property
    def nr_licencji(self) -> int:
        return self._nr_licencji

    def __str__(self):
        return f"Dietetyk {self.imię} {self.nazwisko} pracuje w firmie {self.firma}. Nr licencji: {self.nr_licencji}"
