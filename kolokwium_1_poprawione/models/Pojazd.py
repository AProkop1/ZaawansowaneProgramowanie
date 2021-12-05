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
        return f"Pojazd firmy {self.__marka} ma rejestrację {self.__rejestracja}. Jego przebieg to {self.__przebieg}." \
               "Ma pojemność: {self.__pojemnosc}. Jego rocznik to {self.__rok}"
