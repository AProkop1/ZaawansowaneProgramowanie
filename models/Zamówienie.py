from models.Dietetyk import Dietetyk
from models.Pacjent import Pacjent
from models.Dieta import Dieta


class Zamowienie:
    def __init__(self, dietetyk: Dietetyk, pacjent: Pacjent, lista_diet: list[Dieta], adres_dostawy: str):
        self._dietetyk = dietetyk
        self._pacjent = pacjent
        self._lista_diet = lista_diet
        self._adres_dostawy = adres_dostawy

    @property
    def dietetyk(self) -> Dietetyk:
        return self._dietetyk

    @dietetyk.setter
    def dietetyk(self, value: Dietetyk) -> None:
        self._dietetyk = value

    @property
    def pacjent(self) -> Pacjent:
        return self._pacjent

    @pacjent.setter
    def pacjent(self, value: Pacjent) -> None:
        self._pacjent = value

    @property
    def lista_diet(self) -> list[Dieta]:
        return self._lista_diet

    @lista_diet.setter
    def lista_diet(self, value: list[Dieta]) -> None:
        self._lista_diet = value

    @property
    def adres_dostawy(self) -> str:
        return self._adres_dostawy

    @adres_dostawy.setter
    def adres_dostawy(self, value: str) -> None:
        self.adres_dostawy = value

    def __str__(self):
        return f"Zamówienie dla pacjenta {self.pacjent.imię} {self.pacjent.nazwisko} zostanie dostarczone na adres" \
               f" {self.adres_dostawy}. Zamówienie składa się z {[x.nazwa for x in self.lista_diet]}, które zostały " \
               f"ułożone przez {self.dietetyk.imię} {self.dietetyk.nazwisko}."

    def cena_zamowienia(self) -> float:
        cena = 0.0
        for x in self.lista_diet:
            cena = cena + x.cena
        return round(cena, 2)

    def kcal_zamowienia(self) -> int:
        kcal = 0
        for x in self.lista_diet:
            kcal = kcal + x.kcal
        return kcal
