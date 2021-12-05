from models.FirmaSpozywcza import FirmaSpozywcza
from models.FirmaTransportowa import FirmaTransportowa
from models.Odcinek import Odcinek
from models.Kurs import Kurs
from models.Pojazd import Pojazd


firma_transportowa = FirmaTransportowa("Transportex", "Adam Kowalski", 2000, 32, "Polska")
firma_spozycza = FirmaSpozywcza("Lidlex", "Obronców 43", "Warszawa", 653826597, "Jan Nowakowski")
pojazd = Pojazd("Audi", 2021, 400000, 3000, "SK Transportex1")
odcinek_1 = Odcinek("Berlin", "Katowice", 517.83, 450, 1063)
odcinek_2 = Odcinek("Katowice", "Warszawa", 293.31, 300, 1064)
list_odcinkow = [odcinek_1, odcinek_2]
kurs = Kurs("Joanna Nowak", list_odcinkow, firma_transportowa, firma_spozycza, pojazd)

print(kurs)
