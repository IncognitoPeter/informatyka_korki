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
    if x == 0:
        return 1
    else:
        return silnia(x-1) * x


def szereg_2_n(x, n):
    s = 1
    for i in range(1, n+1):
        s += (x ** i) / silnia(i)
    return s

def szereg_2_eps(x, eps):
    s = 1
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
        s += ((-1) ** (i+1)) / i * x ** i
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
    return math.log1p(x)


# print(szereg_3_n(2, 10), szereg_3_eps(2, 0.001), funkcja_3(2))

# zadanie 4
def szereg_4_n(x, n):
    s = 0
    for i in range(n):
        s += (x ** (2 * i)) / silnia(2 * i)
    return s

def szereg_4_eps(x, eps):
    s = 1
    n = 1
    wyraz = (x ** 2) / silnia(2)
    while abs(wyraz) > eps:
        s += wyraz
        n += 1
        wyraz = (x ** (2 * n)) / silnia(2 * n)
    return s


def funkcja_4(x):
    return math.cosh(x)


# print(szereg_4_n(2, 10), szereg_4_eps(2, 0.001), funkcja_4(2))

# zadanie 5
def szereg_5_n(x, n):
    s = 0
    for i in range(1, n+1):
        s += (-n) ** (n-1) * x ** n / silnia(n)
    return s


def szereg_5_eps(x, eps):
    s = 0
    n = 1
    wyraz = x
    while abs(wyraz) > eps:
        s += wyraz
        n += 1
        wyraz = (-n) ** (n-1) * x ** n / silnia(n)
    return s


def funkcja_5(x):
    return x


# print(szereg_5_n((math.e-0.5), 10), szereg_5_eps((math.e-0.5),0.001), funkcja_5(math.e-0.5))


# zadanie 6
def szereg_6_n(x, n):
    s = 0
    for i in range(n):
        s += (x ** (2 * i + 1)) / (2 * i + 1)
    return s

def szereg_6_eps(x, eps):
    s = 0
    n = 0
    wyraz = x
    while abs(wyraz) > eps:
        s += wyraz
        n += 1
        wyraz = (x ** (2 * n + 1)) / (2 * n + 1)
    return s


def funkcja_6(x):
    return math.atanh(x)


# print(szereg_1_n(0.5, 10), szereg_6_eps(0.5, 0.001), funkcja_6(0.5))

# zadanie 7
def szereg_7_n(x, n):
    s = 0
    for i in range(n):
        s += (x ** (2 * i + 1)) / silnia(2 * i + 1)
    return s

def szereg_7_eps(x, eps):
    s = 0
    n = 0
    wyraz = x
    while abs(wyraz) > eps:
        s += wyraz
        n += 1
        wyraz = (x ** (2 * n + 1)) / silnia(2 * n + 1)
    return s


def funkcja_7(x):
    return math.sinh(x)


# print(szereg_7_n(2, 10), szereg_7_eps(2, 0.001), funkcja_7(2))

# zadanie 8
def szereg_8_n(x, n):
    s = 0
    for i in range(n):
        s += ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
    return s

def szereg_8_eps(x, eps):
    s = 0
    n = 0
    wyraz = x
    while abs(wyraz) > eps:
        s += wyraz
        n += 1
        wyraz = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
    return s


def funkcja_8(x):
    return math.atan(x)


# print(szereg_8_n(0.5, 10), szereg_8_eps(0.5, 0.001), funkcja_8(0.5))

# zadanie 9
def szereg_9_n(x, n):
    s = 0
    for i in range(n):
        s += ((-1) ** i) * (x ** (2 * i)) / silnia(2 * i)
    return s

def szereg_9_eps(x, eps):
    s = 0
    n = 0
    wyraz = 1
    while abs(wyraz) > eps:
        s += wyraz
        n += 1
        wyraz = ((-1) ** n) * (x ** (2 * n)) / silnia(2 * n)
    return s


def funkcja_9(x):
    return math.cos(x)


# print(szereg_9_n(2, 10), szereg_9_eps(2, 0.001), funkcja_9(2))

# zadanie 10
def szereg_10_n(x, n):
    s = 0
    for i in range(n):
        s += ((-1) ** i) * (x ** (2 * i + 1)) / silnia(2 * i + 1)
    return s


def szereg_10_eps(x, eps):
    s = 0
    n = 0
    wyraz = x
    while abs(wyraz) > eps:
        s += wyraz
        n += 1
        wyraz = ((-1) ** n) * (x ** (2 * n + 1)) / silnia(2 * n + 1)
    return s


def funkcja_10(x):
    return math.sin(x)


# print(szereg_10_n(2, 10), szereg_10_eps(2, 0.001), funkcja_10(2))

# zadanie 11
def szereg_11_n(x, n):
    s = 0
    for i in range(1, n + 1):
        s += (-1) ** (i + 1) * silnia(2 * i) * x ** (2 * i + 1) / (4 ** i * silnia(i) ** 2 * (2 * i + 1))
    return s


def szereg_11_eps(x, eps):
    s = 0
    n = 1
    wyraz = (-1) ** (n + 1) * silnia(2 * n) * x ** (2 * n + 1) / (4 ** n * silnia(n) ** 2 * (2 * n + 1))
    while abs(wyraz) > eps:
        s += wyraz
        n += 1
        wyraz = (-1) ** (n + 1) * silnia(2 * n) * x ** (2 * n + 1) / (4 ** n * silnia(n) ** 2 * (2 * n + 1))
    return s


def funkcja_11(x):
    return math.asinh(x)


# print(szereg_11_n(1, 10), szereg_11_eps(1, 0.001), funkcja_11(1))

# zadanie 12
def szereg_12_n(x, n):
    s = 0
    for i in range(1, n + 1):
        s += silnia(2 * i) * x ** (2 * i + 1) / (4 ** i * silnia(i) ** 2 * (2 * i + 1))
    return s


def szereg_12_eps(x, eps):
    s = 0
    n = 1
    wyraz = silnia(2 * n) * x ** (2 * n + 1) / (4 ** n * silnia(n) ** 2 * (2 * n + 1))
    while abs(wyraz) > eps:
        s += wyraz
        n += 1
        wyraz = silnia(2 * n) * x ** (2 * n + 1) / (4 ** n * silnia(n) ** 2 * (2 * n + 1))
    return s


def funkcja_12(x):
    return math.asin(x)


# print(szereg_12_n(1, 10), szereg_12_eps(1, 0.001), funkcja_12(1))

# zadanie 13
def szereg_13_n(x, n):
    s = 0
    for i in range(0, n):
        s += (-1) ** i * silnia(2*i) * x ** i / (4 ** i * silnia(i) ** 2 * (1-2*i))
    return s


def szereg_13_eps(x, eps):
    s = 0
    n = 0
    wyraz = 0
    flaga = True
    while flaga or abs(wyraz) > eps:
        s += wyraz
        wyraz = (-1) ** n * silnia(2*n) * x ** n / (4 ** n * silnia(n) ** 2 * (1-2*n))
        n += 1
        flaga = False
    return s


def funkcja_13(x):
    return math.sqrt(x+1)


# print(szereg_13_n(0.5, 10), szereg_13_eps(0.5, 0.001), funkcja_13(0.5))
# n= 2
# x = 0.5
# print((-1) ** n * silnia(2*n) * x ** n / (4 ** n * silnia(n) ** 2 * (1-2*n)))
