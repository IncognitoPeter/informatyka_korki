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


# print(sprawdz_czy_da_sie_zsumowac_kwadraty(10))

def odwracanie_liczby(liczba):
    nowa = 0
    while liczba != 0:
        cyfra = liczba % 10
        nowa = nowa * 10 + cyfra
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

def zaszyfruj_cyfry_w_liczbie(liczba):
    zaszyfrowane = 0
    mnoznik = 1
    cyfry = 0
    liczba_pom = liczba
    while liczba_pom != 0:
        liczba_pom = liczba_pom // 10
        cyfry += 1
    while liczba != 0:
        cyfra = liczba % 10
        if cyfry == 1 and cyfra == 9:
            zaszyfrowane += (cyfra + 1) * mnoznik
        if cyfra == 9:
            zaszyfrowane += 0 * mnoznik
        else:
            zaszyfrowane += (cyfra + 1) * mnoznik
        liczba = liczba // 10
        mnoznik *= 10
        cyfry -= 1
    return zaszyfrowane


# print(zaszyfruj_cyfry_w_liczbie(9796))

def podziel_liczbe(liczba):
    super_dzielnik_2 = 2
    super_dzielnik_3 = 3
    super_dzielnik_5 = 5
    for i in range(1, liczba + 1):
        if i != super_dzielnik_2 and i != super_dzielnik_3 and i != super_dzielnik_5:
            if liczba % i == 0:
                return False
    return True


def szukaj_dziwnych_liczb(n):  # ta funkcja jesli ma być podzielne przez jakiekolwiek z 2,3,5 (łącznie z '1')
    suma = 0
    for i in range(1, n + 1):
        podziel_liczbe(i)
        suma += 1
    return suma

# print(szukaj_dziwnych_liczb(23))


def szukaj_dziwnych_liczb_v2(n):  # a ta funkcja jak ma być równocześnie podzielne przez 2,3,5 (łącznie z '1')
    suma = 1
    for i in range(1, n + 1):
        if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
            suma += 1
    return suma


# print(szukaj_dziwnych_liczb_v2(256))

def rozklad_na_iloczyn():
    liczba1 = 0
    liczba2 = 0
    liczba = int(input('podaj liczbe: \n'))
    for i in range(liczba//2):
        if i*i <= liczba:
            liczba1 = i
    for i in range(liczba//2):
        if liczba1*i == liczba:
            liczba2 = i
    return liczba1, liczba2


# print(rozklad_na_iloczyn())

def sprawdz_czy_cyfry_tworza_ciag_rosnacy(liczba):
    while liczba != 0:
        cyfra_1 = liczba % 10
        liczba = liczba // 10
        cyfra_2 = liczba % 10
        if cyfra_1 <= cyfra_2:
            return False
    return True


# print(sprawdz_czy_cyfry_tworza_ciag_rosnacy(123))

def sprawdz_czy_cyfry_tworza_ciag_arytmetyczny(liczba):
    while liczba != 0:
        cyfra_1 = liczba % 10
        liczba = liczba // 10
        cyfra_2 = liczba % 10
        liczba = liczba // 10
        cyfra_3 = liczba % 10
        if cyfra_1 - cyfra_2 == cyfra_2 - cyfra_3:
            return True
    return False


# print(sprawdz_czy_cyfry_tworza_ciag_arytmetyczny(123))

def sprawdz_czy_cyfry_tworza_ciag_geometryczny(liczba):
    while liczba != 0:
        cyfra_1 = liczba % 10
        liczba = liczba // 10
        cyfra_2 = liczba % 10
        liczba = liczba // 10
        cyfra_3 = liczba % 10
        try:
            if cyfra_1 / cyfra_2 == cyfra_2 / cyfra_3:
                return True
        except ZeroDivisionError:
            return False
    return False


# print(sprawdz_czy_cyfry_tworza_ciag_geometryczny(124))

def odwroc_liczbe(liczba):
    nowa = 0
    while liczba != 0:
        cyfra = liczba % 10
        nowa = nowa * 10 + cyfra
        liczba = liczba // 10
    return nowa


def znajdz_odwrocone_liczby():
    for i in range(1, 1000000):
        if i % 10 != 0 and odwroc_liczbe(i) * odwroc_liczbe(i) == odwroc_liczbe(i*i):
            print(i, odwroc_liczbe(i))


# print(znajdz_odwrocone_liczby())
