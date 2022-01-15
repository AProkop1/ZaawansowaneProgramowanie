from models.Dietetyk import Dietetyk
from models.Pacjent import Pacjent
from models.Dieta import Dieta
from models.Zamówienie import Zamowienie

dieta1 = Dieta("Dieta Vegan", "Diety Roślinne", 49.99, 1800)
dieta2 = Dieta("Dieta Sport", "Diety z wysoką zawartością białka", 59.99, 3000)
diety = [dieta1, dieta2]
pacjent = Pacjent("Jan", "Kowalski", 29, "ul. Adamskiego 14/2 Katowice")
dietetyk = Dietetyk("Mariusz", "Nowak", "BodyChef", 651736)

zamowienie = Zamowienie(dietetyk, pacjent, diety, "ul. Adamskiego 14/2 Katowice")

print(zamowienie)

print(zamowienie.cena_zamowienia())
print(zamowienie.kcal_zamowienia())
