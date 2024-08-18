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
        return -1
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
        return -1
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

# zadanie_3
def print_subnumbers(n, k):
    pass


# print(print_subnumbers(3, 2))

# zadanie_4
def dec2factorial_base(n):
    liczba_10 = 0
    mnoznik = 1
    wynik = 0
    while n != 0:
        cyfra = n % 2
        liczba_10 += cyfra * mnoznik
        n = n // 10
        mnoznik *= 2
    mnoznik = 1
    silnia = 1
    while liczba_10 != 0:
        wynik += (liczba_10 % silnia) * mnoznik
        liczba_10 = liczba_10 // silnia
        silnia += 1
        mnoznik *= 10
    return wynik

# print(dec2factorial_base(101))


def factorial_base2dec(n):
    liczba_10 = 0
    mnoznik = 1
    silnia = 1
    wynik = 0
    while n != 0:
        liczba_10 += (n % 10) * mnoznik
        n = n // 10
        mnoznik *= silnia
        silnia += 1
    mnoznik = 1
    while liczba_10 != 0:
        cyfra = liczba_10 % 2
        wynik += cyfra * mnoznik
        liczba_10 = liczba_10 // 2
        mnoznik *= 10
    return wynik


# print(factorial_base2dec(210))

# zadanie_5


def are_anagrams(a, b):
    c0, c1, c2, c3, c4, c5, c6, c7, c8, c9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    while a > 0:
        cyfra_a = a % 10
        if cyfra_a == 0:
            c0 += 1
        elif cyfra_a == 1:
            c1 += 1
        elif cyfra_a == 2:
            c2 += 1
        elif cyfra_a == 3:
            c3 += 1
        elif cyfra_a == 4:
            c4 += 1
        elif cyfra_a == 5:
            c5 += 1
        elif cyfra_a == 6:
            c6 += 1
        elif cyfra_a == 7:
            c7 += 1
        elif cyfra_a == 8:
            c8 += 1
        elif cyfra_a == 9:
            c9 += 1
        a = a // 10
    while b > 0:
        cyfra_b = b % 10
        if cyfra_b == 0:
            c0 -= 1
        elif cyfra_b == 1:
            c1 -= 1
        elif cyfra_b == 2:
            c2 -= 1
        elif cyfra_b == 3:
            c3 -= 1
        elif cyfra_b == 4:
            c4 -= 1
        elif cyfra_b == 5:
            c5 -= 1
        elif cyfra_b == 6:
            c6 -= 1
        elif cyfra_b == 7:
            c7 -= 1
        elif cyfra_b == 8:
            c8 -= 1
        elif cyfra_b == 9:
            c9 -= 1
        b = b // 10
    if c0 == 0 and c1 == 0 and c2 == 0 and c3 == 0 and c4 == 0 and c5 == 0:
        if c6 == 0 and c7 == 0 and c8 == 0 and c9 == 0:
            return True
    return False


# print(are_anagrams(3455, 543))

# zadanie_6


def sexagecimal_time2hundred(h, m, s):
    sekundy = h * 60 + m * 60 + s
    s_prim = sekundy % 100
    m_prim = (sekundy // 100) % 100
    h_prim = (sekundy // 10000) % 100
    wynik = (h_prim, m_prim, s_prim)
    return wynik

# print(sexagecimal_time2hundred(15, 37, 23))


def hundred_base_time2sexagesimal(h, m, s):
    sekundy = h * 100 + m * 100 + s
    s_prim = sekundy % 60
    m_prim = (sekundy // 60) % 60
    h_prim = (sekundy // 3600) % 60
    wynik = (h_prim, m_prim, s_prim)
    return wynik

# print(hundred_base_time2sexagesimal(15, 37, 23))

# zadanie_7


def add(a, b):
    mnoznik = 1
    liczba = 0
    while a != 0 or b != 0:
        cyfra_a = a % 10
        cyfra_b = b % 10
        if cyfra_a + cyfra_b >= 10:
            liczba += (cyfra_a + cyfra_b - 10) + 10 * mnoznik
        else:
            liczba += (cyfra_a + cyfra_b) * mnoznik
        mnoznik *= 10
        a = a // 10
        b = b // 10
    return liczba


# print(add(117, 23))

# zadanie_8


def div(a, b):
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
            wynik = wynik * 10 + reszta // b
            reszta = reszta % b
        else:
            wynik = wynik * 10
    return wynik


# print(div(51, 17))

# zadanie_9


def sub(a, b):
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

# print(sub(467, 399))

# zadanie_10


def max_len_subnumber(n):
    len = 1
    len_max = 0
    wynik = 0
    pomocnik_1 = 0
    pomocnik_2 = 0
    nowa = 0
    liczba = n
    wynik_max = 0
    while liczba != 0:
        nowa = nowa * 10 + liczba % 10
        liczba = liczba // 10
    liczba = nowa
    while liczba != 0:
        pomocnik_1 = liczba % 10
        liczba = liczba // 10
        pomocnik_2 = liczba % 10
        if pomocnik_1 < pomocnik_2 and len > len_max:
            len +=1
            wynik = wynik * 10 + pomocnik_1
            wynik = wynik * 10 + pomocnik_2
            wynik_max = wynik
        else:
            wynik = 0
            len = 1
    return wynik_max, len_max


# print(max_len_subnumber(572134825))

# zadanie_11


def add_v2(a, b, k):
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
    while liczba_1 != 0 or liczba_2 != 0:
        cyfra_1 = liczba_1 % k
        cyfra_2 = liczba_2 % k
        if cyfra_1 + cyfra_2 >= k:
            nowa += (cyfra_1 + cyfra_2 - k) + k * mnoznik
        else:
            nowa += (cyfra_1 + cyfra_2) * mnoznik
        mnoznik *= 10
        liczba_1 = liczba_1 // 10
        liczba_2 = liczba_2 // 10

    return liczba_1, liczba_2, nowa


# print(add_v2(14, 17, 10))

# zadanie_12


def sub_v2(a, b, k):
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
    wynik = 0
    reszta = 0
    liczba = liczba_1
    while liczba != 0:
        nowa = nowa * 10 + liczba % 10
        liczba = liczba // 10
    liczba = nowa
    while liczba != 0:
        reszta = reszta * 10 + liczba % 10
        liczba = liczba // 10
        if reszta >= liczba_2:
            wynik = wynik * 10 + reszta - liczba_2
            reszta = reszta % liczba_2
        else:
            wynik = wynik * 10
    return wynik


# print(sub_v2(467, 399, 10))


# zadanie_13

def mul(a, b, k):
    liczba_1 = 0
    liczba_2 = 0
    mnoznik = 1
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
    mnoznik_1 = 1
    wynik = 0
    while liczba_1 != 0:
        cyfra_1 = liczba_1 % 10
        liczba_1 = liczba_1 // 10
        # mnoznik_2 = 1
        nowa = 0
        nowy_mnoznik = mnoznik_1
        nowe_2 = liczba_2
        while nowe_2 != 0:
            cyfra_2 = nowe_2 % 10
            nowe_2 = nowe_2 // 10
            wynik_pom = cyfra_1 * cyfra_2
            nowa += wynik_pom * nowy_mnoznik
            nowy_mnoznik = nowy_mnoznik * 10
            wynik += nowa
            mnoznik_1 = mnoznik_1 * 10
    return wynik

# print(mul(12, 11, 10))
# print(12*11)


# zadanie_14

def div_v2(a, b, k):
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
            wynik = wynik * 10 + reszta // b
            reszta = reszta % b
        else:
            wynik = wynik * 10
    mnoznik = 1
    nowy_wynik = 0
    while wynik != 0:
        cyfra_a = wynik % k
        nowy_wynik += cyfra_a * mnoznik
        wynik = wynik // k
        mnoznik *= 10
    return nowy_wynik


# print(div_v2(51, 17, 10))

# zadanie_15

def c(n, k):
    pass


# print(c(8, 2))
