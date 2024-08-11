def dec2bin(liczba):
    a = 0
    mnoznik = 1
    while liczba != 0:
        cyfra = liczba % 2
        a += cyfra * mnoznik
        liczba = liczba // 2
        mnoznik *= 10
    return a

# print(dec2bin(7))


def bin2dec(liczba):
    a = 0
    mnoznik = 1
    while liczba != 0:
        cyfra = liczba % 10
        a += cyfra * mnoznik
        liczba = liczba // 10
        mnoznik *= 2
    return a

# print(bin2dec(111))
