class Telefon:
    def __init__(self, model, producent):
        self.model = model
        self.producent = producent

    def info(self):
        return {self.producent}, {self.model}


class Komunikacja:
    def wyslij_wiadomosc(self, odbiorca, tresc):
        print(f"Wysłano wiadomość do: {odbiorca}: {tresc}")


class Rozrywka:
    def odtworz_rozrywke(self, utwor):
        print(f"Odtwarzanie utworu: {utwor}")


class Smartphone(Telefon):
    def __init__(self, model, producent):
        super().__init__(model, producent)
        self.komunikacja = Komunikacja()
        self.rozrywka = Rozrywka()


# Test
telefon = Smartphone("Nokia 3310", "Nokia")
print("Informacje o telefonie: ", telefon.info())

#Funkcjonalnosci
telefon.komunikacja.wyslij_wiadomosc("Tom", "Hello")
telefon.rozrywka.odtworz_rozrywke("Test")

'''
Kompozycja
Jest bardziej elastyczna – możesz łatwo wymieniać/składać różne funkcjonalności.
Unikasz problemów wielodziedziczenia, np. konfliktów metod o tych samych nazwach (tzw. diamond problem).
Klasy są lepiej rozdzielone logicznie – każda ma swoją odpowiedzialność.
'''