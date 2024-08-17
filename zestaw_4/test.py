def sub(a, b, k):
    liczba_1 = 0
    liczba_2 = 0
    mnoznik = 1
    nowa = 0
    while a != 0:
        cyfra_a = a % k
        liczba_1 += cyfra_a * mnoznik
        a = a // k
        mnoznik *= 10
    mnoznik = 1
    while b != 0:
        cyfra_b = b % k
        liczba_2 += cyfra_b * mnoznik
        b = b // k
        mnoznik *= 10
    mnoznik = 1


    wynik = 0
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

print(sub(467, 399, 10))
