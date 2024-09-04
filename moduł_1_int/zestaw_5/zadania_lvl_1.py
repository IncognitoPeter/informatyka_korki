# zadanie_1
def sprawdz_czy_jest_potega(liczba):
    podstawa_parzysta = 2
    podstawa_nieparzysta = 3
    mnoznik = 1
    if liczba == 1:
        return 1
    else:
        if liczba % 2 == 0:
            for i in range(2, liczba+1, 2):
                if podstawa_parzysta * mnoznik == liczba:
                    print(f'{podstawa_parzysta}^{mnoznik}')
                    return True
                mnoznik = mnoznik * mnoznik
        else:
            for i in range(3, liczba+1, 2):
                if podstawa_nieparzysta * mnoznik == liczba:
                    print(f'{podstawa_nieparzysta}^{mnoznik}')
                    return True
                mnoznik = mnoznik * mnoznik
    return False

# print((sprawdz_czy_jest_potega(64)))

# zadanie_2


def licz_punkty_kratowe():
    pass
