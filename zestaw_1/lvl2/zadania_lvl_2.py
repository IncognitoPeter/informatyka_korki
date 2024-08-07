def potega(x, n):
    wynik = 1
    for i in range(n):
        wynik *= x
    return wynik


# print(potega(4, 2))

def nwd(y, b):
    while b != 0:
        y, b = b, y % b
    return y


# print(nwd(24, 6))
'''
def nwd(c, b):
    while b != 0:
        c, b = b, c % b
    return c
'''


def nww(z, b):
    return z * b / nwd(z, b)


# print(nww(24, 6))

def suma_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba = liczba // 10
    return suma


# print(suma_cyfr(69))

def suma_kwadratow_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += (liczba % 10) * (liczba % 10)
        liczba = liczba // 10
    return suma


# print(suma_kwadratow_cyfr(69))

a = 125

'''
def suma_kwadratow_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += (liczba % 10) * (liczba % 10)
        liczba = liczba // 10
    return suma
'''


def czy_jest(liczba):
    if liczba == suma_kwadratow_cyfr(liczba):
        return True
    else:
        return False


# print(czy_jest(a))


def sprawdz_parzystosc_ilosc_nieparzystych_cyfr(liczba):
    ilosc = 0
    while liczba > 0:
        if liczba % 10 % 2 != 0:
            ilosc += 1
        liczba = liczba // 10
    if ilosc % 2 == 0:
        return True
    return False


# print(sprawdz_parzystosc_ilosc_nieparzystych_cyfr(126))


def czy_wzglednie_pierwsze(liczba1, liczba2):
    while liczba2 != 0:
        liczba1, liczba2 = liczba2, liczba1 % liczba2
    if liczba1 == 1:
        return True
    return False


# print(czy_wzglednie_pierwsze(25, 17))

def sprawdz_czy_cyfra_rowna_liczbie_cyfr(liczba):
    ilosc = 0
    liczba_pom = liczba
    while liczba_pom > 0:
        ilosc += 1
        liczba_pom = liczba_pom // 10
    while liczba > 0:
        if liczba % 10 == ilosc:
            return True
        liczba = liczba // 10
    return False


# print(sprawdz_czy_cyfra_rowna_liczbie_cyfr(25))
