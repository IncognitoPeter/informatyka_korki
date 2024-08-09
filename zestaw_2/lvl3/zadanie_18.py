def odwroc_liczbe(liczba):
    nowa = 0
    while liczba != 0:
        cyfra = liczba % 10
        nowa = nowa * 10 + cyfra
        liczba = liczba // 10
    return nowa


def znajdz_odwrocone_liczby():
    for i in range(1, 1000000):
        if i % 10 != 0 and odwroc_liczbe(i) * odwroc_liczbe(i) == odwroc_liczbe(i*i):
            print(i, odwroc_liczbe(i))


print(znajdz_odwrocone_liczby())
