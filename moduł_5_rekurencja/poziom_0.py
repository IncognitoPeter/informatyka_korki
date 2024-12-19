# zadanie_1
def silnia(n):
    if n == 0 or n == 1:
        return 1
    return n * silnia(n - 1)


# (silnia(5))

# zadanie_2
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(1))

# zadanie_3
def suma(n):
    if n == 0:
        return 0
    return n + suma(n - 1)


# print(suma(5))

# zadanie_4
def nwd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return nwd(a - b, b)
    return nwd(a, b - a)

# print(nwd(39, 26))


# zadanie_5
def nwd_v1(a, b):
    if b == 0:
        return a
    return nwd_v1(b, a % b)


# print(nwd_v1(39, 26))



# zadanie_6
def dzielniki(n, d=1):
    if d > n:
        return
    if n % d == 0:
        print(d)
    dzielniki(n, d + 1)


#dzielniki(10)


# zadanie_7
def dzielniki_pary(n, d=1):
    if d * d > n:
        return
    if n % d == 0:
        print(d, n // d)
    dzielniki_pary(n, d + 1)


# dzielniki_pary(10)


# zadanie_8
def czynniki_pierwsze(n, d=2):
    if n < 2:
        return
    if n % d == 0:
        print(d)
        czynniki_pierwsze(n // d, d)
    else:
        czynniki_pierwsze(n, d + 1)


# czynniki_pierwsze(30)



# zadanie_9
def zamiana_systemu(n, k):
    if n == 0:
        return ""
    return zamiana_systemu(n // k, k) + str(n % k)

# print(zamiana_systemu(16, 2))



# zadanie_10
def ilosc_cyfr(n):
    if n < 10:
        return 1
    return 1 + ilosc_cyfr(n // 10)

# print(ilosc_cyfr(9850))


# zadanie_11
def suma_cyfr(n):
    if n == 0:
        return 0
    return n % 10 + suma_cyfr(n // 10)


# print(suma_cyfr(9850))
