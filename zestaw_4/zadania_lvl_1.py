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

# zadanie_3
def print_subnumbers(n, k):
    pass


# print(print_subnumbers(3, 2))

# zadanie_4
def dec2factorial_base(n):
    pass


# print(dec2factorial_base(10))

def factorial_base2dec(n):
    pass

# print(factorial_base2dec(10))

# zadanie_5


def are_anagrams(a, b):
    pass


# print(are_anagrams(345, 543))

# zadanie_6

def sexagecimal_time2hundred(h, m, s):
    pass


# print(sexagecimal_time2hundred(15, 37, 3))

def hundred_base_time2sexagesimal(h, m, s):
    pass


# print(hundred_base_time2sexagesimal(15, 37, 3))

# zadanie_7

def add(a, b):
    pass


# print(add(17, 23))

# zadanie_8

def div(a, b):
    pass


# print(div(51, 17))

# zadanie_9

def sub(a, b):
    pass

# print(sub(173, 13))

# zadanie_10


def max_len_subnumber(n):
    pass

# print(max_len_subnumber(572134825))

# zadanie_11


def add(a, b, k):
    pass


# print(add(14, 17, 6))

# zadanie_12

def sub(a, b, k):
    pass


# print(sub(21, 15, 4))

# zadanie_13

def mul(a, b, k):
    pass


# print(mul(7, 4, 3))

# zadanie_14

def div(a, b, n):
    pass


# print(div(100, 3, 5))

# zadanie_15

def c(n, k):
    pass


#print(c(8, 2))
# cos