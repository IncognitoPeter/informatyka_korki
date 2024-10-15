# zadanie_1
def sprawdz_czy_jest_potega(liczba):
    if liczba == 1:
        return True
    for i in range(2, liczba + 1):
        mnoznik = 1
        wynik = i
        while wynik <= liczba:
            if wynik == liczba:
                print(f'{i}^{mnoznik}')
                return True
            mnoznik += 1
            wynik *= i
    return False


# print((sprawdz_czy_jest_potega(125)))

# zadanie_2


def licz_punkty_kratowe(a, b):
    for i in range(a, b + 1):
        lepsze_y = 1000 // i
        y = 1
        while y <= lepsze_y:
            print(f'({i},{y})')
            y += 1


# print(licz_punkty_kratowe(1,2))

# zadanie_3
def rozklad_na_czynniki(liczba):
    dzielnik = 2
    czynniki = 0
    mnoznik = 1
    while liczba > 1:
        if liczba % dzielnik == 0:
            czynniki += dzielnik * mnoznik
            mnoznik *= 10
            liczba //= dzielnik
        else:
            dzielnik += 1
    return czynniki


def rozklad_na_czynniki_z_jedna_wspolna(liczba_1, liczba_2):
    czynniki_1 = rozklad_na_czynniki(liczba_1)
    czynniki_2 = rozklad_na_czynniki(liczba_2)
    wspolny_czynnik = 0
    while czynniki_1 > 0 and czynniki_2 > 0:
        cyfra_1 = czynniki_1 % 10
        cyfra_2 = czynniki_2 % 10
        if cyfra_1 == cyfra_2 and cyfra_1 != 0:
            wspolny_czynnik += 1
        czynniki_1 //= 10
        czynniki_2 //= 10
    if wspolny_czynnik == 1:
        return True
    else:
        return False


# print(rozklad_na_czynniki_z_jedna_wspolna(24, 14))


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
def wypisz_n_cyfrowe(liczba):
    liczba_v1 = liczba
    cyfry = 0
    while liczba_v1 != 0:
        liczba_v1 = liczba_v1 // 10
        cyfry += 1
    wynik = 0
    liczba_v1 = liczba
    while liczba_v1 != 0:
        cyfra = liczba_v1 % 10
        wynik += cyfra ** cyfry
        liczba_v1 = liczba_v1 // 10
    return wynik == liczba


def wypisz_liczby():
    for i in range(1, 10000):
        if wypisz_n_cyfrowe(i):
            print(i)

# wypisz_liczby()


# zadanie_6


def pierwiastek_calkowitolicznowy(n):
    i = 1
    sumy = 0
    licznik = 0
    while sumy <= n:
        sumy += i
        i += 2
        licznik += 1
    return licznik-1


# print(pierwiastek_calkowitolicznowy(4))

# zadanie_7
def suma_dzielnikow(liczba):
    sumy = 0
    for i in range(1, liczba // 2 + 1):
        if liczba % i == 0:
            sumy += i
    return sumy


def koledzy_miliona():
    for i in range(1, 10000):
        a = suma_dzielnikow(i)
        if i < a:
            if a < 10000:
                if suma_dzielnikow(a) == i:
                    print(i, a)

# koledzy_miliona()

# zadanie_8


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def nwd_3_liczb(a, b, c):
    jeden = nwd(a, b)
    wynik = nwd(c, jeden)
    return wynik


# print(nwd_3_liczb(16, 8, 4))

# zadanie_9


def nww(a, b):
    return a * b // nwd(a, b)


def nww_3_liczb(a, b, c):
    jeden = nww(a, b)
    wynik = nww(c, jeden)
    return wynik


# print(nww_3_liczb(2, 4, 8))

# zadanie_10
def suma(liczba):
    sumy = 0
    while liczba > 0:
        sumy += liczba % 10
        liczba //= 10
    return sumy


def suma_cyfr_czynnikow(liczba):
    dzielnik = 2
    suma_czynnikow = 0
    while liczba > 1:
        if liczba % dzielnik == 0:
            suma_czynnikow += suma(dzielnik)
            liczba //= dzielnik
        else:
            dzielnik += 1
    return suma_czynnikow


def czy_liczba_smith(liczba):
    suma_liczby = suma(liczba)
    suma_czynnikow = suma_cyfr_czynnikow(liczba)
    return suma_liczby == suma_czynnikow


def liczba_smitha():
    for i in range(2, 100):
        if not czy_liczba_smith(i):
            continue
        print(i)

# print(liczba_smitha())

# zadanie 11


def kwadraty_nie_szesciany(n):
    i = 1
    while i * i < n:
        kwadrat = i * i
        szescian = i * i * i
        if kwadrat >= n:
            break
        if szescian >= n or kwadrat != szescian:
            print(kwadrat)
        i += 1

# kwadraty_nie_szesciany(10)

# zadanie 12


def palindrom(n, p):
    liczba = n
    odwrocona = 0
    temp = liczba
    while temp > 0:
        odwrocona = odwrocona * p + temp % p
        temp //= p
    return odwrocona == liczba


def podstawa(n):
    for p in range(2, 11):
        if palindrom(n, p):
            return p
    return None


def czy_jest(n):
    if podstawa(n):
        return podstawa(n)

# print(czy_jest(5))

# zadanie 13


def czy_ciag(liczba):
    n = 1
    while True:
        an = n * n + n + 1
        if an > liczba:
            break
        elif an == liczba:
            return n, liczba
        n += 1
    return None


# print(czy_ciag(31))

# zadanie 14
def licz_zera(n):
    zera = 0
    dzielnik = 5
    while n>= dzielnik:
        zera += n // dzielnik
        dzielnik *=5
    return zera

# print(licz_zera(100))

# zadanie 15
def ostatnia_niezerowa(n):
    zera = licz_zera(n)
    iloczyn = 1
    licznik_dwojek = 0
    for i in range(1, n + 1):
        a = i
        while a % 5 == 0:
            a //= 5
        while a % 2 == 0 and licznik_dwojek < zera:
            a = a // 2
            licznik_dwojek += 1
        iloczyn = (iloczyn * (a % 10)) % 10
    return iloczyn

# print(ostatnia_niezerowa(26))