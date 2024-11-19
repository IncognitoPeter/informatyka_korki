# zadanie_1
tab = [1, 5, 3, 9, 10, 5]


def srednia_wartosc_w_tablicy(tablica):
    licznik = 0
    ilosc = 0
    for i in range(len(tablica)):
        licznik += tablica[i]
        ilosc += 1
    return licznik/ilosc

# print(srednia_wartosc_w_tablicy(tab))

# zadanie_2
def mediana_z_tablicy(tablica):
    ilosc = len(tablica)
    if ilosc % 2 == 1:
        return tablica[ilosc // 2]
    else:
        return (tablica[ilosc // 2 -1] + tablica[ilosc // 2]) /2

# print(mediana_z_tablicy([1, 2, 3, 4, 9, 10]))
# print(mediana_z_tablicy([1, 2, 3, 5, 5, 9, 10]))

# zadanie_3
def posortuj_tablice(tablica):
    ilosc = len(tablica)
    for i in range(ilosc):
        for j in range(0, ilosc - i - 1):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
    return tablica

def mediana_v2(tablica):
    posortuj_tablice(tablica)
    return mediana_z_tablicy(tablica)

# print(mediana_v2([4, 1, 2, 9, 10, 3]))
# print(mediana_v2([5, 1, 2, 5, 9, 10, 3]))

# zadanie_4
def druga_najwieksza_wartosc(tablica):
    return tablica[-2]


#print(druga_najwieksza_wartosc([1, 2, 3, 5, 9, 10]))


# zadanie_5
def druga_najwieksza_wartosc_v2(tablica):
    posortuj_tablice(tablica)
    return tablica[-2]


#print(druga_najwieksza_wartosc_v2([1, 5, 3, 9, 10, 2]))

# zadanie_6
def ile_najwiekszych_wartosci(tablica):
    najwieksza = tablica[-1]
    ilosc = 0
    for i in tablica:
        if tablica[i] == najwieksza:
            ilosc += 1
    return ilosc


#print(ile_najwiekszych_wartosci([1,2,3,4,6,7,7,7,7,9,10,10,10,10,10]))

# zadanie_7
def ile_najwiekszych_wartosci_v2(tablica):
    posortuj_tablice(tablica)
    print(tablica)
    najwieksza = tablica[-1]
    ilosc = 0
    for i in tablica:
        if tablica[i] == najwieksza:
            ilosc += 1
    return ilosc

#print(ile_najwiekszych_wartosci_v2([1,10,1,3,9,10,2,10,5,10,4]))

# zadanie_8
def dominanta(tablica):
    najczestsza = tablica[0]
    licznik_max = 1
    licznik = 1
    for i in range(1, len(tablica)):
        if tablica[i] == tablica[i - 1]:
            licznik += 1
        else:
            if licznik > licznik_max:
                licznik_max = licznik
                najczestsza = tablica[i - 1]
            licznik = 1
    if licznik > licznik_max:
        najczestsza = tablica[-1]
    return najczestsza

# print(dominanta([1,1,3,3,3,3,4,5,5,5,5,5,6,7,8,10]))

# zadanie_9
def dominanta_v2(tablica):
    posortuj_tablice(tablica)
    return dominanta(tablica)

# print(dominanta_v2([1,6,7,8,10,1,3,5,5,3,3,4,5,5,3,5]))

# zadanie_10
def wariancje(tablica):
    suma = 0
    for i in range(len(tablica)):
        suma += tablica[i]
    ilosc = len(tablica)
    srednia = suma / ilosc
    wynik = 0
    for j in range(len(tablica)):
        wynik += (tablica[j] - srednia) ** 2
    return wynik

# print(wariancje([3,6,15,5,5,5]))

# zadanie_11
def sortowanie_parzyste_nieparzyste(tablica):
    nieparzyste = []
    parzyste = []
    for x in tablica:
        if x % 2 == 0:
            parzyste.append(x)
        else:
            nieparzyste.append(x)
    for i in range(len(parzyste)):
        for j in range(0, len(parzyste) - i - 1):
            if parzyste[j] > parzyste[j + 1]:
                parzyste[j], parzyste[j + 1] = parzyste[j + 1], parzyste[j]
    for i in range(len(nieparzyste)):
        for j in range(0, len(nieparzyste) - i - 1):
            if nieparzyste[j] < nieparzyste[j + 1]:
                nieparzyste[j], nieparzyste[j + 1] = nieparzyste[j + 1], nieparzyste[j]
    return parzyste + nieparzyste


# print(sortowanie_parzyste_nieparzyste([1, 5, 3, 9, 10, 2, 10, 5, 10, 4]))