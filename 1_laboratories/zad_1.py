import json

class ModelAI:
    liczba_modeli = 0

    def __init__(self, nazwa_modelu, wersja):
        self.nazwa_modelu = nazwa_modelu
        self.wersja = wersja
        ModelAI.nowy_model()

    @classmethod
    def nowy_model(cls):
        cls.liczba_modeli += 1

    @classmethod
    def ile_modeli(cls):
        return cls.liczba_modeli

    @classmethod
    def z_pliku(cls, nazwa_pliku):
        with open(nazwa_pliku, 'r') as plik:
            dane = json.load(plik)
            modele = []
            for item in dane:
                modele.append(cls(item['name'], item['version']))
            return modele

model1 = ModelAI("ModelA", "1.0")

print(ModelAI.ile_modeli())

modele_z_pliku = ModelAI.z_pliku("models.json")

print(ModelAI.ile_modeli())  # Powinna zwrócić 4 (3 modele z pliku + 1 stworzony ręcznie)

for model in modele_z_pliku:
    print(f"Model: {model.nazwa_modelu}, Wersja: {model.wersja}")
