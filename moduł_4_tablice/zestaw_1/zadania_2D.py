# zadanie_1
def ile_liczb_potegi_3(tablica):
    licznik = 0
    for liczba in tablica:
        if liczba < 1:
            return False
        while liczba % 3 == 0:
            liczba //= 3
        if liczba == 1:
            licznik += 1
    return licznik

# print(ile_liczb_potegi_3([24, 6, 7, 6, 120, 5, 1]))


# zadanie_2
def ile_liczb_potegi_czegos(tablica):
    licznik = 0
    for liczba in tablica:
        if liczba < 0:
            continue
        i = 0
        while i * i <= liczba:
            if i * i == liczba:
                licznik += 1
            i += 1
        i = 0
    return licznik

# print(ile_liczb_potegi_czegos([24, 6, 7, 6, 120, 5, 1]))

# zadanie_3
def ile_liczb_silni(tablica):
    licznik = 0
    for liczba in tablica:
        silnia = 1
        k = 1
        while silnia <= liczba:
            if silnia == liczba:
                licznik += 1
            k += 1
            silnia *= k
    return licznik

# print(ile_liczb_silni([24, 6, 7, 6, 120, 5, 1]))

# zadanie_4
def ile_z_fibonaciego(tablica):
    licznik = 0
    for liczba in tablica:
        a, b = 0, 1
        while a <= liczba:
            if a == liczba:
                licznik += 1
            a, b = b, a + b
    return licznik


# print(ile_z_fibonaciego([9,10,2,3,7,21,34,33,5,8,13,17]))

# zadanie_5
def fib(a):
    if a == 0:
        return 0
    liczba = fib(a-1) + a
    return liczba

#print(fib(10))

def ile_z_fibonaciego_mniejsze10(tablica):
    licznik = 0
    for liczba in tablica:
        a, b = 0, 1
        while a <= liczba:
            if a == liczba and liczba <= 55:
                licznik += 1
            a, b = b, a + b
    return licznik


# print(ile_z_fibonaciego_mniejsze10([9,10,2,3,7,21,34,33,5,8,13,17]))

# zadanie_6
def rozniace_sie_o_kwadrat(tablica):
    pass


# print(rozniace_sie_o_kwadrat([9,10,2,3,7,21,34,33,5,8,13,17]))
