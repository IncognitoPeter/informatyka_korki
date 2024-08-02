def suma_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba = liczba // 10
    return suma


print(suma_cyfr(69))
