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
    for x in range(a, b + 1):
        y = 1000 / x
        if 1000 % x == 0:
            print(x, y)


# print(licz_punkty_kratowe(1,20))

# zadanie_3
def rozklad_na_czynniki():
    pass


# print(rozklad_na_czynniki())

# zadanie_4
def wypisz_trojki_pitagorejskie(n):
    for a in range(1, n):
        for b in range(a + 1, n):
            c = 1
            while c * c < a*a + b*b:
                c += 1
            if c * c == a*a + b*b:
                if c < n:
                    print(a, b, c)


# print(wypisz_trojki_pitagorejskie(14))

# zadanie_5
def wypisz_n_cyfrowe():
    pass


# print(wypisz_n_cyfrowe())

# zadanie_6
def pierwiastek_calkowitolicznowy():
    pass

# print(pierwiastek_calkowitolicznowy())

# zadanie_7


def koledzy_miliona():
    pass

# print(koledzy_miliona))

# zadanie_8


def nwd_3_liczb():
    pass


# print(nwd_3_liczb())

# zadanie_9
def nww_3_liczb():
    pass


# print(nww_3_liczb())

# zadanie_10
def liczba_smitha():
    pass

# print(liczba_smitha())
