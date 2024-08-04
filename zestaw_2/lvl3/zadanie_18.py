def odwroc_liczbe(liczba):
    tab = []
    mnoznik = 1
    nowa_liczba = 0
    while liczba != 0:
        cyfra = liczba % 10
        tab.append(cyfra)
        liczba = liczba//10
    tab.reverse()
    for i in tab:
        nowa_liczba += i * mnoznik
        mnoznik *= 10
    return nowa_liczba


def znajdz_odwrocone_liczby():
    for i in range(1, 1000000):
        if i % 10 == 0:
            continue
        if odwroc_liczbe(i) * odwroc_liczbe(i) == odwroc_liczbe(i*i):
            print(i, odwroc_liczbe(i))


print(znajdz_odwrocone_liczby())
