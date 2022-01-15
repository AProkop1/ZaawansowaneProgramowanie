class Dieta:
    def __init__(self, nazwa: str, kategoria: str, cena: float, kcal: int):
        self._nazwa = nazwa
        self._kategoria = kategoria
        self._cena = cena
        self._kcal = kcal

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def kategoria(self) -> str:
        return self._kategoria

    @property
    def cena(self) -> float:
        return self._cena

    @property
    def kcal(self) -> int:
        return self._kcal

    def __str__(self):
        return f"Dieta {self.nazwa} należy do kategori {self.kategoria}, posiada {self.kcal} kcal i kosztuje " \
               f"{self.cena} zł "
