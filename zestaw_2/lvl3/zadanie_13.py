def podziel_liczbe(liczba):
    super_dzielniki = [2, 3, 5]
    for i in range(1, liczba + 1):
        if i not in super_dzielniki and liczba % i == 0:
            return False
    return True


def szukaj_dziwnych_liczb(n):  # ta funkcja jesli ma być podzielne przez jakiekolwiek z 2,3,5 (łącznie z '1')
    suma = 0
    for i in range(1, n + 1):
        podziel_liczbe(i)
        suma += 1
    return suma

# print(szukaj_dziwnych_liczb(23))


def szukaj_dziwnych_liczb_v2(n):  # a ta funkcja jak ma być równocześnie podzielne przez 2,3,5 (łącznie z '1')
    suma = 1
    for i in range(1, n + 1):
        if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
            suma += 1
    return suma


# print(szukaj_dziwnych_liczb_v2(256))
