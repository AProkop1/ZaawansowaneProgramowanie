class FirmaTransportowa:
    def __init__(self, nazwa: str, wlasciciel: str, rokZalozenia: int, iloscPracownikow: int, krajZalozenia: str):
        self.__nazwa = nazwa
        self.__wlasciciel = wlasciciel
        self.__rokZalozenia = rokZalozenia
        self.__iloscPracownikow = iloscPracownikow
        self.__krajZalozenia = krajZalozenia

    @property
    def get_nazwa(self):
        return self.__nazwa

    def get_wlasciciel(self):
        return self.__wlasciciel

    def get_rokZalozenia(self):
        return self.__rokZalozenia

    def get_iloscPracownikow(self):
        return self.__iloscPracownikow

    def get_krajZalozenia(self):
        return self.__krajZalozenia

    def __str__(self):
        return f"Firma transportowa {self.__nazwa} została założona w {self.__rokZalozenia}r. przez {self.__wlasciciel}" \
               "w {self.__krajZalozenia}. Obecnie zatrudnia {self.__iloscPracownikow} pracowników."

class FirmaSpozywcza:
    def __init__(self, nazwa: str, adres: str, miasto: str, nrTel: int, wlasciciel: str):
        self.__nazwa = nazwa
        self.__adres = adres
        self.__miasto = miasto
        self.__nrTel =nrTel
        self.__wlasciciel = wlasciciel

    def get_nazwa(self):
        return self.__nazwa

    def get_adres(self):
        return self.__adres

    def get_miasto(self):
        return self.__miasto

    def get_nrTel(self):
        return self.__nrTel

    def get_wlasciciel(self):
        return self.__wlasciciel

    def __str__(self):
        return f"Firma spożywcza {self.__nazwa} znajduje się w {self.__miasto} pod adresem {self.__adres}."\
                "Jej obecny właścciiel nazywa się : {self.__wlasciciel}. Kontakt po nr telefonu: {self.__nrTel}"

class Pojazd:
    def __init__(self, marka: str, rok: int, przebieg: int, pojemnosc: int, rejestracja: str):
        self.__marka = marka
        self.__rok = rok
        self.__przebieg = przebieg
        self.__pojemnosc = pojemnosc
        self.__rejestracja = rejestracja

    def get_marka(self):
        return self.__marka

    def get_rok(self):
        return self.__rok

    def get_przebieg(self):
        return self.__przebieg

    def get_pojemnosc(self):
        return self.__pojemnosc

    def get_rejestracja(self):
        return self.__rejestracja

    def __str__(self):
        return f"Pojazd firmy {self.__marka} ma rejestrację {self.__rejestracja}. Jego przebieg to {self.__przebieg}."\
                "Ma pojemność: {self.__pojemnosc}. Jego rocznik to {self.__rok}"

class Odcinek:
    def __init__(self, punktStart: str, punktDocelowy: str, odleglosc: float, cena: int, id: int):
        self.__punktStart = punktStart
        self.__punktDocelowy = punktDocelowy
        self.__odleglosc = odleglosc
        self.__cena = cena
        self.__id = id

    def get_punktStart(self):
        return self.__punktStart

    def get_punktDocelowy(self):
        return self.__punktDocelowy

    def get_odleglosc(self):
        return self.__odleglosc

    def get_cena(self):
        return self.__cena

    def get_id(self):
        return self.__id

    def __str__(self):
        f"Odcinek zaczyna się  {self.__punktStart} i kończy się {self.get_punktStart}. Odległość wynosi {self.__odleglosc} "\
                "a koszt to {self.__cena}. ID tego odcinku to {self.__id}"


class Kurs:
    def __init__(self, pracownikLogistyczny: str, listaOdcinkow: list[Odcinek], firmaTransportowa: FirmaTransportowa,
                 firmaSpozywcza: FirmaSpozywcza, pojazd: Pojazd):
        self.__pracownikLogistyczny = pracownikLogistyczny
        self.__listaOdcinkow = listaOdcinkow
        self.__firmaTransportowa = firmaTransportowa
        self.__firmaSpozywcza = firmaSpozywcza
        self.__pojazd = pojazd

    def get_pracownikLogistyczny(self):
        return self.__pracownikLogistyczny

    def get_listaOdcinkow(self):
        return self.__listaOdcinkow

    def get_firmaTransportowa(self):
        return self.__firmaTransportowa

    def get_firmaSpozywcza(self):
        return self.__firmaSpozywcza

    def get_pojazd(self):
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
                "a kończących  w {[x.get_punktDocelowy() for x in self.__listaOdcinkow]} . Logistyką kursu zajmuje się pracownik "\
                "{self.__pracownikLogistyczny}. Za transport odpowiedzialna jest {self.__firmaTransportowa.__str__()}. Transport "\
                "odbędzie się pojazdem: {self.__pojazd.__str__()}. "

    def suma_km(self):
        suma = 0.0
        for x in self.__listaOdcinkow:
            suma += x.get_odleglosc()
        return round(suma,2)

    def get_markaPojazdu(self):
        return self.__marka


firma_transportowa = FirmaTransportowa("Transportex", "Adam Kowalski", 2000, 32, "Polska")
firma_spozycza = FirmaSpozywcza("Lidlex", "Obronców 43", "Warszawa", 653826597, "Jan Nowakowski")
pojazd = Pojazd("Audi", 2021, 400000, 3000, "SK Transportex1")
odcinek_1 = Odcinek("Berlin", "Katowice", 517.83, 450, 1063)
odcinek_2 = Odcinek("Katowice", "Warszawa", 293.31, 300, 1064)
list_odcinkow = (odcinek_1, odcinek_2)
kurs = Kurs("Joanna Nowak", list_odcinkow, firma_transportowa, firma_spozycza, pojazd)

print(kurs)










