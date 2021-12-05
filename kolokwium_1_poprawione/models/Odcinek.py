class Odcinek:
    def __init__(self, punktStart: str, punktDocelowy: str, odleglosc: float, cena: int, id: int):
        self.__punktStart = punktStart
        self.__punktDocelowy = punktDocelowy
        self.__odleglosc = odleglosc
        self.__cena = cena
        self.__id = id

    def get_punktStart(self) -> str:
        return self.__punktStart

    def get_punktDocelowy(self) -> str:
        return self.__punktDocelowy

    def get_odleglosc(self) -> float:
        return self.__odleglosc

    def get_cena(self) -> int:
        return self.__cena

    def get_id(self) -> int:
        return self.__id

    def __str__(self):
        f"Odcinek zaczyna się  {self.__punktStart} i kończy się {self.get_punktStart}. Odległość wynosi {self.__odleglosc} " \
        f"a koszt to {self.__cena}. ID tego odcinku to {self.__id}"
