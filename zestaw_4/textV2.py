def sub(a, b):
    wynik = 0
    mnoznik = 0
    reszta = 0
    liczba = a
    nowa = 0
    while liczba != 0:
        nowa = nowa * 10 + liczba % 10
        liczba = liczba // 10
    liczba = nowa
    while liczba != 0:
        reszta = reszta * 10 + liczba % 10
        liczba = liczba // 10
        if reszta >= b:
            wynik = wynik * 10 + reszta - b
            reszta = reszta % b
        else:
            wynik = wynik * 10
    return wynik

print(sub(467, 399))
