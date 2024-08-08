def odwracanie_liczby(liczba):
    tab = []
    nowa = 0
    mnoznik = 1
    while liczba != 0:
        cyfra = liczba % 10
        tab.append(cyfra)
        liczba = liczba//10
    tab.reverse()
    for i in range(len(tab)):
        nowa += tab[i] * mnoznik
        mnoznik *= 10
    return nowa


print(odwracanie_liczby(2567))
