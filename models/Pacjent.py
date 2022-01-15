class Pacjent:
    def __init__(self, imię: str, nazwisko: str, wiek: int, adres: str):
        self._imię = imię
        self._nazwisko = nazwisko
        self._wiek = wiek
        self._adres = adres

    @property
    def imię(self) -> str:
        return self._imię

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def wiek(self) -> int:
        return self._wiek

    @property
    def adres(self) -> str:
        return self._adres

    def __str__(self):
        return f"Pacjent nazywa się {self.imię}  {self.nazwisko}. Ma {self.wiek} lat i mieszka na {self.adres}."
