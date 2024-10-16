import math
# zadanie 1


def szereg_1_n(x, n):
    s = 0
    for i in range(1, n+1):
        s += x ** i
    return s


def szereg_1_eps(x, eps):
    s = 0
    n = 1
    wyraz = x
    while abs(wyraz) > eps:
        s += wyraz
        n += 1
        wyraz = x ** n
    return s


def funkcja_1(x):
    return x / (1 - x)


# print(szereg_1_n(0.5, 10), szereg_1_eps(0.5, 0.001), funkcja_1(0.5))

# zadanie 2
def silnia(x):
    if x == 1:
        return 1
    else:
        return silnia(x-1) * x


def szereg_2_n(x, n):
    s = 0
    for i in range(1, n+1):
        s += (x ** n) / silnia(n)
    return s


def szereg_2_eps(x, eps):
    s = 0
    n = 1
    wyraz = x
    while abs(wyraz) > eps:
        s += wyraz
        n += 1
        wyraz = (x ** n) / silnia(n)
    return s


def funkcja_2(x):
    return math.e ** x


# print(szereg_2_n(2, 10), szereg_2_eps(2, 0.001), funkcja_2(2))

# zadanie 3
def szereg_3_n(x, n):
    s = 0
    for i in range(1, n+1):
        s += ((-1) ** (n+1)) / n * x ** n
    return s


def szereg_3_eps(x, eps):
    s = 0
    n = 1
    wyraz = x
    while abs(wyraz) > eps:
        s += wyraz
        n += 1
        wyraz = ((-1) ** (n+1)) / n * x ** n
    return s


def funkcja_3(x):
    return math.log(x + 1, math.e)


# print(szereg_3_n(2, 10), szereg_3_eps(2, 10), funkcja_3(2))

# zadanie 4
def szereg_4_n(x, n):
    s = 0
    for i in range(1, n+1):
        s += (x ** (2*n)) / silnia(2*n)
    return s


def szereg_4_eps(x, eps):
    s = 0
    n = 1
    wyraz = x
    while abs(wyraz) > eps:
        s += wyraz
        n += 1
        wyraz = (x ** (2*n)) / silnia(2*n)
    return s


def funkcja_4(x):
    return math.cosh(x)


# print(szereg_4_n(2, 10), szereg_4_eps(2, 10), funkcja_4(2))

# zadanie 5
def szereg_5_n(x, n):
    pass


def szereg_5_eps(x, eps):
    pass


def funkcja_5(x):
    pass


# zadanie 6
def szereg_6_n(x, n):
    pass


def szereg_6_eps(x, eps):
    pass


def funkcja_6(x):
    return math.atanh(x)


# zadanie 7
