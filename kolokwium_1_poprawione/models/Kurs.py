from models.FirmaSpozywcza import FirmaSpozywcza
from models.FirmaTransportowa import FirmaTransportowa
from models.Odcinek import Odcinek
from models.Pojazd import Pojazd


class Kurs:
    def __init__(self, pracownikLogistyczny: str, listaOdcinkow: list[Odcinek], firmaTransportowa: FirmaTransportowa,
                 firmaSpozywcza: FirmaSpozywcza, pojazd: Pojazd):
        self.__pracownikLogistyczny = pracownikLogistyczny
        self.__listaOdcinkow = listaOdcinkow
        self.__firmaTransportowa = firmaTransportowa
        self.__firmaSpozywcza = firmaSpozywcza
        self.__pojazd = pojazd

    def get_pracownikLogistyczny(self) -> str:
        return self.__pracownikLogistyczny

    def get_listaOdcinkow(self) -> list:
        return self.__listaOdcinkow

    def get_firmaTransportowa(self) -> FirmaTransportowa:
        return self.__firmaTransportowa

    def get_firmaSpozywcza(self) -> FirmaSpozywcza:
        return self.__firmaSpozywcza

    def get_pojazd(self) -> Pojazd:
        return self.__pojazd

    def set_pracownikLogistyczny(self, value: str):
        self.__pracownikLogistyczny = value

    def set_listaOdcinkow(self, value: list):
        self.__listaOdcinkow = value

    def set_firmaTransportowa(self, value: FirmaTransportowa):
        self.__firmaTransportowa = value

    def set_firmaSpozywcza(self, value: FirmaSpozywcza):
        self.__firmaSpozywcza = value

    def set_pojazd(self, value: Pojazd):
        self.__pojazd = value

    def __str__(self):
        return f"Kurs składa się z odcinków zaczynających się w: {[x.get_punktStart() for x in self.__listaOdcinkow]} "\
               f"a kończących  w {[x.get_punktDocelowy() for x in self.__listaOdcinkow]} . Logistyką kursu zajmuje " \
               f"się pracownik {self.__pracownikLogistyczny}. Za transport odpowiedzialna jest "\
               f"{self.__firmaTransportowa.__str__()}. Transport odbędzie się pojazdem: {self.__pojazd.__str__()}. "

    def suma_km(self):
        suma = 0.0
        for x in self.__listaOdcinkow:
            suma += x.get_odleglosc()
        return round(suma,2)

    def get_markaPojazdu(self):
        return self.__marka