class FirmaTransportowa:
    def __init__(self, nazwa: str, wlasciciel: str, rokZalozenia: int, iloscPracownikow: int, krajZalozenia: str):
        self.__nazwa = nazwa
        self.__wlasciciel = wlasciciel
        self.__rokZalozenia = rokZalozenia
        self.__iloscPracownikow = iloscPracownikow
        self.__krajZalozenia = krajZalozenia

    @property
    def get_nazwa(self) -> str:
        return self.__nazwa

    def get_wlasciciel(self) -> str:
        return self.__wlasciciel

    def get_rokZalozenia(self) -> int:
        return self.__rokZalozenia

    def get_iloscPracownikow(self) -> int:
        return self.__iloscPracownikow

    def get_krajZalozenia(self) -> int:
        return self.__krajZalozenia

    def __str__(self):
        return f"Firma transportowa {self.__nazwa} została założona w {self.__rokZalozenia}r. przez {self.__wlasciciel}" \
               f"w {self.__krajZalozenia}. Obecnie zatrudnia {self.__iloscPracownikow} pracowników."