a = 125


def suma_kwadratow_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += (liczba % 10) * (liczba % 10)
        liczba = liczba // 10
    return suma


def czy_jest(liczba):
    if liczba == suma_kwadratow_cyfr(liczba):
        return True
    else:
        return False


print(czy_jest(a))
