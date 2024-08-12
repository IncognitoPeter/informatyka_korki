# zadanie_1
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


def bin2kbase(liczba, k):
    if k > 10:
        return "zle k"
    a = 0
    mnoznik = 1
    liczba_k = 0
    while liczba != 0:
        cyfra = liczba % 10
        a += cyfra * mnoznik
        liczba = liczba // 10
        mnoznik *= 2
    mnoznik = 1
    while a != 0:
        cyfra = a % k
        liczba_k += cyfra * mnoznik
        a = a // k
        mnoznik *= k
    return liczba_k

# print(bin2kbase(111, 10))


def kbase2bin(liczba, k):
    if k > 10:
        return "zle k"
    a = 0
    mnoznik = 1
    liczba_bin = 0
    while liczba != 0:
        cyfra = liczba % 10
        a += cyfra * mnoznik
        liczba = liczba // 10
        mnoznik *= k
    mnoznik = 1
    while a != 0:
        cyfra = a % 2
        liczba_bin += cyfra * mnoznik
        a = a // 2
        mnoznik *= k
    return liczba_bin


# print(kbase2bin(7,10))

# zadanie_2

def bit_and(a, b):
    mnoznik = 1
    wynik = 0
    while a != 0 or b != 0:
        cyfra_a = a % 2
        cyfra_b = b % 2
        if cyfra_a == 1 and cyfra_b == 1:
            wynik += mnoznik
        a = a // 2
        b = b // 2
        mnoznik *= 2
    return wynik


# print(bit_and(5, 7))

