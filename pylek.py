import json
from typing import Dict

class Pylek():

    def __init__(self, stan_wewnetrzny: str) -> None:
        self._stan_wewnetrzny = stan_wewnetrzny

    def operation(self, stan_zewnetrzny: str) -> None:
        s = json.dumps(self._stan_wewnetrzny)
        u = json.dumps(stan_zewnetrzny)
        print(f"Pylek: Stan wewnętrzny ({s}) i stan zewnętrzny ({u}).", end="")


class FabrykaPylkow():


    _Pylki: Dict[str, Pylek] = {}

    def __init__(self, pylki_poczatkowe: Dict) -> None:
        for stan in pylki_poczatkowe:
            self._Pylki[self.uzyskaj_klucz(stan)] = Pylek(stan)

    def uzyskaj_klucz(self, stan: Dict) -> str:

        return "_".join(sorted(stan))

    def uzyskaj_pylek(self, stan_wewnetrzny: Dict) -> Pylek:
        klucz = self.uzyskaj_klucz(stan_wewnetrzny)

        if not self._Pylki.get(klucz):
            print("FabrykaPylkow: Nie mogę znaleźć pyłka. Tworzę nowy.")
            self._Pylki[klucz] = Pylek(stan_wewnetrzny)
        else:
            print("FabrykaPylkow: Korzystam z istniejącego pyłka")

        return self._Pylki[klucz]

    def wypisz_pylki(self) -> None:
        ilosc = len(self._Pylki)
        print(f"FabrykaPylkow: Mam {ilosc} pylkow:")
        print("\n".join(map(str, self._Pylki.keys())), end="")


def dodaj_samochod_do_bazy(
    fabryka: FabrykaPylkow, blachy: str, wlasciciel: str,
    marka: str, model: str, kolor: str
) -> None:
    print("\n\nKlient: Dodaje samochod do bazy.")
    pylek = fabryka.uzyskaj_pylek([marka, model, kolor])
    pylek.operation([blachy, wlasciciel])


if __name__ == "__main__":

    fabryka = FabrykaPylkow([
        ["Chevrolet", "spark", "zielony"],
        ["Ford", "mustang", "czerwony"],
        ["Toyota", "yaris", "czarny"],
        ["Citroen", "xsara_picasso", "niebieski"],
        ["BMW", "x6", "szary"],
        ["Citroen", "c6", "bialy"],
        ["KIA", "proceed", "czarny"],
        ["Seat", "leon", "czerwony"],
        ["Renault", "megane", "zloty"],
        ["Peugeot", "308", "zielony"],
        ["Wolksvagen", "golf", "szary"],
        ["Toyota", "corolla", "bialy"],
    ])

    fabryka.wypisz_pylki()

    dodaj_samochod_do_bazy(
        fabryka, "XYZ12345", "Jan Kowalski", "BMW", "x6", "szary")
    dodaj_samochod_do_bazy(
        fabryka, "XYZ98765", "Anna Nowak", "Toyota", "corolla", "bialy")
    dodaj_samochod_do_bazy(
        fabryka, "ABC98765", "Zuzanna Sitek", "Renault", "megane", "zloty")
    dodaj_samochod_do_bazy(
        fabryka, "ABC13579", "Karol Krawczyk", "Ford", "mustang", "zloty")
    dodaj_samochod_do_bazy(
        fabryka, "TVN24680", "Tadeusz Norek", "KIA", "proceed", "czarny")
    dodaj_samochod_do_bazy(
        fabryka, "TVN78272", "Józef Budka", "Chevrolet", "spark", "zielony")
    dodaj_samochod_do_bazy(
        fabryka, "TVP95321", "Robert Narewny", "Fiat", "multipla", "bialy")

    print("\n")

    fabryka.wypisz_pylki()
 
