def sprawdz_czy_jest_kwadratem(liczba):
    for i in range(liczba // 2):
        if i * i == liczba:
            return i
    return -1


# print(sprawdz_czy_jest_kwadratem(25))

def sprawdz_czy_jest_szescianem(liczba):
    for i in range(liczba // 2):
        if i * i * i == liczba:
            return i
    return -1


# print(sprawdz_czy_jest_szescianem(8))

def znajdz_rozne_cyfry(liczba):
    zero, jeden, dwa, trzy, cztery, piec = 0, 0, 0, 0, 0, 0
    szesc, siedem, osiem, dziewiec, rozne_cyfry = 0, 0, 0, 0, 0
    while liczba != 0:
        cyfra = liczba % 10
        if cyfra == 0 and zero == 0:
            zero += 1
            rozne_cyfry += 1
        if cyfra == 1 and jeden == 0:
            jeden += 1
            rozne_cyfry += 1
        if cyfra == 2 and dwa == 0:
            dwa += 1
            rozne_cyfry += 1
        if cyfra == 3 and trzy == 0:
            trzy += 1
            rozne_cyfry += 1
        if cyfra == 4 and cztery == 0:
            cztery += 1
            rozne_cyfry += 1
        if cyfra == 5 and piec == 0:
            piec += 1
            rozne_cyfry += 1
        if cyfra == 6 and szesc == 0:
            szesc += 1
            rozne_cyfry += 1
        if cyfra == 7 and siedem == 0:
            siedem += 1
            rozne_cyfry += 1
        if cyfra == 8 and osiem == 0:
            osiem += 1
            rozne_cyfry += 1
        if cyfra == 9 and dziewiec == 0:
            dziewiec += 1
            rozne_cyfry += 1
        liczba = liczba // 10
    return rozne_cyfry


# print(znajdz_rozne_cyfry(1255))

def czy_pierwsza(liczba):
    if liczba <= 1:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


def szukaj_unikatowych_pierwszych(liczba):
    ilosc = 0
    for i in range(2, liczba):
        if czy_pierwsza(i):
            if liczba % i == 0:
                liczba = liczba / i
                if liczba % i != 0:
                    ilosc += 1
    return ilosc


# print(szukaj_unikatowych_pierwszych(26))


def suma_dzielnikow_pierwszych(liczba):
    suma = 0
    for i in range(2, liczba):
        if czy_pierwsza(i):
            if liczba % i == 0:
                liczba = liczba / i
                if liczba % i != 0:
                    suma += i
    return suma


# print(suma_dzielnikow_pierwszych(26))

def sprawdz_czy_liczba_to_dwa_kwadraty(liczba):
    for i in range(liczba):
        if i * i + (i + 1) * (i + 1) == liczba:
            return i
    return -1


# print(sprawdz_czy_liczba_to_dwa_kwadraty(41))

def sprawdz_czy_liczba_to_trzy_kwadraty(liczba):
    for i in range(liczba):
        if i * i + (i + 1) * (i + 1) + (i + 2) * (i + 2) == liczba:
            return i
    return -1


# print(sprawdz_czy_liczba_to_trzy_kwadraty(50))

def sprawdz_czy_da_sie_zsumowac_kwadraty(liczba):
    suma = 0
    for i in range(1, liczba, 2):
        suma += i * i
        if suma == liczba:
            return True
    return False


#print(sprawdz_czy_da_sie_zsumowac_kwadraty(10))

def odwracanie_liczby(liczba):
    nowa = 0
    while liczba != 0:
        cyfra = liczba % 10
        nowa = nowa *10 +cyfra
        liczba = liczba // 10
    return nowa

# print(odwracanie_liczby(2567))

def sprawdz_czy_palindrom(liczba):
    nowa = 0
    liczba_1 = liczba
    while liczba != 0:
        cyfra = liczba % 10
        nowa = nowa * 10 + cyfra
        liczba = liczba // 10
    if nowa == liczba_1:
        return True
    return False


# print(sprawdz_czy_palindrom(161))

def zamiana_na_dwojkowy(liczba):
    a = 0
    mnoznik = 1
    while liczba != 0:
        cyfra = liczba % 2
        a += cyfra * mnoznik
        liczba = liczba // 2
        mnoznik *= 10
    return a


# print(zamiana_na_dwojkowy(54))

