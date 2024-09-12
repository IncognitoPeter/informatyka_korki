# zadanie_1
def sprawdz_czy_jest_potega(liczba):
    podstawa_parzysta = 2
    podstawa_nieparzysta = 3
    if liczba == 1:
        return True
    if liczba % 2 == 0:
        mnoznik = 1
        wynik = podstawa_parzysta
        while wynik <= liczba:
            if wynik == liczba:
                print(f'{podstawa_parzysta}^{mnoznik}')
            mnoznik += 1
            wynik *= podstawa_parzysta
    if liczba % 2 != 0:
        mnoznik = 1
        wynik = podstawa_nieparzysta
        while wynik <= liczba:
            if wynik == liczba:
                print(f'{podstawa_nieparzysta}^{mnoznik}')
            mnoznik += 1
            wynik *= podstawa_nieparzysta
    for i in range(3, liczba + 1, 2):
        mnoznik = 1
        wynik = i
        while wynik <= liczba:
            if wynik == liczba:
                print(f'{i}^{mnoznik}')
            mnoznik += 1
            wynik *= i
    return False


# print((sprawdz_czy_jest_potega(125)))

# zadanie_2


def licz_punkty_kratowe(a, b):
    x = a
    y= 1000/x
    pass


# print(licz_punkty_kratowe(1,20))
