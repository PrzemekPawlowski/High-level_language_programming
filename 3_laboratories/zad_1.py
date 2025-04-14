"""Library using dictionaries instead of class Ksiazka"""


class Biblioteka:
    """Constructor"""

    def __init__(self):
        self.lista_ksiazek = []

    def dodaj_ksiazke(self, tytul, autor, dostepna=True):
        """Function adding book"""
        ksiazka = {"tytul": tytul, "autor": autor, "dostepna": dostepna}
        self.lista_ksiazek.append(ksiazka)

    def wypozycz_ksiazke(self, tytul):
        """Function check books"""
        for ksiazka in self.lista_ksiazek:
            if ksiazka["tytul"] == tytul:
                if ksiazka["dostepna"]:
                    ksiazka["dostepna"] = False
                    return f"Wypozyczono: {tytul}"
                return f"Ksiazka {tytul} niedostepna"
        return f"Brak ksiazki: {tytul}"

    def zwroc_ksiazke(self, tytul):
        """Function return book"""
        for ksiazka in self.lista_ksiazek:
            if ksiazka["tytul"] == tytul:
                ksiazka["dostepna"] = True
                return f"Zwrocono: {tytul}"
        return f"Nie nalezy do biblioteki: {tytul}"

    def dostepne_ksiazki(self):
        """Book availability checker function"""
        dostepne = []
        for ksiazka in self.lista_ksiazek:
            if ksiazka["dostepna"]:
                dostepne.append(ksiazka["tytul"])
        return dostepne


def main():
    """Main function"""
    biblioteka = Biblioteka()
    biblioteka.dodaj_ksiazke("Wiedzmin", "Sapkowski")
    biblioteka.dodaj_ksiazke("Solaris", "Lem")
    biblioteka.dodaj_ksiazke("Lalka", "Prus", False)

    print(biblioteka.wypozycz_ksiazke("Solaris"))
    print(biblioteka.wypozycz_ksiazke("Lalka"))
    print(biblioteka.zwroc_ksiazke("Lalka"))
    print("Dostepne ksiazki: ", biblioteka.dostepne_ksiazki())


main()
