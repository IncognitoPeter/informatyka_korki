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

# zadanie_7
def czy_arytmetyczny(tablica):
    for i in range(len(tablica) - 2):
        if tablica[i + 1] - tablica[i] == tablica[i + 2] - tablica[i + 1]:
            return tablica[i], tablica[i + 1], tablica[i + 2]
    return -1


# print(czy_arytmetyczny([1, 2, 3, 4, 5]))

# zadanie_8
def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nww(a, b):
    return abs(a * b) // nwd(a, b)

def czy_wzglednie_pierwsze(tablica):
    for i in range(len(tablica) - 2):
        a, b, c = tablica[i], tablica[i + 1], tablica[i + 2]
        return nww(nww(a, b), c)
    return -1

#print(czy_wzglednie_pierwsze([1, 2, 3, 4, 5]))

# zadanie_9
def najmniejszy_trzeci(tablica):
    min1 = min2 = min3 = 0
    for liczba in tablica:
        if liczba < min1:
            min3, min2, min1 = min2, min1, liczba
        elif liczba < min2 and liczba != min1:
            min3, min2 = min2, liczba
        elif liczba < min3 and liczba != min1 and liczba != min2:
            min3 = liczba
    return min3 if min3 != 0 else -1


# print(najmniejszy_trzeci([6,1,9,3,3,10,5,8,1,7]))

# zadanie_10
def srednia(tablica):
    suma = 0
    for liczba in tablica:
        suma += liczba
    return suma/len(tablica)

def najmniejsza_roznica_od_sredniej(tablica):
    najmniejsza = tablica[0]
    for i in range(len(tablica) - 1):
        if srednia(tablica) - najmniejsza > srednia(tablica) - tablica[i]:
            najmniejsza = tablica[i]
    return najmniejsza

# print(najmniejsza_roznica_od_sredniej([1, 2, 3, 4, 5]))

# zadanie_11
def najwieksze_nwd(tablica):
    najwieksze = 0
    wynik = 0
    for i in range(len(tablica) - 1):
        nwd_1 = nwd(tablica[i], tablica[i+1])
        if nwd_1 > najwieksze:
            najwieksze = nwd_1
            wynik = (tablica[i], tablica[i+1])
    return wynik

# print(najwieksze_nwd([1, 2, 3, 4, 5]))

# zadanie_12
def najwieksze_nwd_1(tablica):
    najwieksze = 0
    wynik = 0
    for i in range(len(tablica)):
        for j in range(i + 1, len(tablica)):
            nwd_1 = nwd(tablica[i], tablica[j])
            if nwd_1 > najwieksze:
                najwieksze = nwd_1
                wynik = (tablica[i], tablica[j])
    return wynik

# print(najwieksze_nwd_1([1, 2, 3, 4, 5]))

# zadanie_13
def sortowanie(tablica):
    ilosc = len(tablica)
    for i in range(ilosc):
        for j in range(0, ilosc - i - 1):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
    return tablica


# print(sortowanie([3,7,8,9,9,9,11,14,5]))

# zadanie_14
def nwd_wszystkich(tablica):
    nNwd = nwd(tablica[0], tablica[1])
    for i in range(2,len(tablica) - 1):
        nNwd = nwd(tablica[i], tablica[i + 1])
    return nNwd


# print(nwd_wszystkich([6, 9, 8, 4, 10, 26]))

# zadanie_15
def suma_w(w1, w2):
    n = max(len(w1), len(w2))
    wynik = [0] * n
    for i in range(n):
        if i < len(w1):
            wynik[i] += w1[i]
        if i < len(w2):
            wynik[i] += w2[i]
    return wynik

# print(suma_w([3, 4, 0, 1], [2, 7]))

def horner(w, x):
    wynik = 0
    w.reverse()
    for wsp in w:
        wynik = wynik * x + wsp
    return wynik

# print(horner([3, 4, 0, 0, 1], 2))

def horner_v2(w, a):
    w.reverse()
    n = len(w)
    wynik = [0] * (n - 1)
    wynik[0] = w[0]
    for i in range(1, n - 1):
        wynik[i] =  a * wynik[i-1]+ w[i]
    reszta = a* wynik[-1] + w[-1]
    return wynik, reszta


# print(horner_v2([3, 4, 0, 0, 1], 2))




# zadanie_17
def najdluzszy_podciag_nwd(tablica):
    max_dlugosc = 0
    dlugosc = 0
    poczatek = -1
    for i in range(1, len(tablica)):
        if nwd(tablica[i - 1], tablica[i]) == 1:
            dlugosc += 1
            if dlugosc > max_dlugosc:
                max_dlugosc = dlugosc
                poczatek = i - dlugosc
        else:
            dlugosc = 0
    if max_dlugosc > 0:
        return max_dlugosc, poczatek
    else:
        return -1, -1

# print(najdluzszy_podciag_nwd([6, 9, 3, 12, 15, 10, 7]))

# zadanie_18
def najdluzszy_fibonacci(tablica):
    fib = [1, 1]
    while fib[-1] < max(tablica):
        fib.append(fib[-1] + fib[-2])
    max_dlugosc = 0
    poczatek = 0
    dlugosc = 0
    for i in range(len(tablica)):
        if tablica[i] in fib:
            dlugosc += 1
            if dlugosc > max_dlugosc:
                max_dlugosc = dlugosc
                poczatek = i
        else:
            dlugosc = 0
    return max_dlugosc, poczatek-max_dlugosc+1


print(najdluzszy_fibonacci([5, 5, 7, 1, 1, 2, 3, 9, 1, 1, 2, 3, 5, 6, 6, 9]))
