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
