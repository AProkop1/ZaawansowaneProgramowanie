class FirmaSpozywcza:
    def __init__(self, nazwa: str, adres: str, miasto: str, nrTel: int, wlasciciel: str):
        self.__nazwa = nazwa
        self.__adres = adres
        self.__miasto = miasto
        self.__nrTel = nrTel
        self.__wlasciciel = wlasciciel

    @property
    def get_nazwa(self) -> str:
        return self.__nazwa

    @property
    def get_adres(self) -> str:
        return self.__adres

    @property
    def get_miasto(self) -> str:
        return self.__miasto

    @property
    def get_nrTel(self) -> int:
        return self.__nrTel

    @property
    def get_wlasciciel(self) -> int:
        return self.__wlasciciel

    def __str__(self):
        return f"Firma spożywcza {self.__nazwa} znajduje się w {self.__miasto} pod adresem {self.__adres}." \
               "Jej obecny właścciiel nazywa się : {self.__wlasciciel}. Kontakt po nr telefonu: {self.__nrTel}"
