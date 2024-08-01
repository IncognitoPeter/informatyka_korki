def potega(a, n):
    wynik = 1
    for i in range(n):
        wynik *= a
    return wynik


print(potega(4, 2))
