def suma_kwadratow_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += (liczba % 10) * (liczba % 10)
        liczba = liczba // 10
    return suma


print(suma_kwadratow_cyfr(69))
