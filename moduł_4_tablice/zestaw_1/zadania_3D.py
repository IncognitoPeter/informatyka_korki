# zadanie_1
def ile_podzielnych_przez_7(tablica):
    licznik = 0
    for liczba in tablica:
        if liczba % 7 == 0:
            licznik += 1
    return licznik

# print(ile_podzielnych_przez_7([7, 14, 10, 21, 5]))


# zadanie_2
def suma_nieparzystych(tablica):
    suma = 0
    for liczba in tablica:
        if liczba % 2 != 0:
            suma += liczba
    return suma


# print(suma_nieparzystych([1, 2, 3, 4, 5]))


# zadanie_3
def czy_istnieje_element_rowny_sredniej(tablica):
    if len(tablica) == 0:
        return False
    srednia = sum(tablica) / len(tablica)
    for liczba in tablica:
        if liczba == srednia:
            return True
    return False


# print(czy_istnieje_element_rowny_sredniej([1, 2, 3, 4, 5]))

# zadanie_4
def iloczyn_jednocyfrowych(tablica):
    iloczyn = 1
    znaleziono = False
    for liczba in tablica:
        if -9 <= liczba <= 9:
            iloczyn *= liczba
            znaleziono = True
    return iloczyn if znaleziono else 1


# print(iloczyn_jednocyfrowych([1, 2, 10, 3]))


# zadanie_5
def ile_mniejszych_od_x(tablica, x):
    licznik = 0
    for liczba in tablica:
        if liczba < x:
            licznik += 1
    return licznik


# print(ile_mniejszych_od_x([1, 2, 3, 4, 5], 3))


# zadanie_6
def roznica_miedzy_min_a_max(tablica):
    if len(tablica) == 0:
        return 0
    return max(tablica) - min(tablica)


# print(roznica_miedzy_min_a_max([1, 2, 3, 4, 5]))

# zadanie_7
def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, int(liczba ** 0.5) + 1):
        if liczba % i == 0:
            return False
    return True

def ile_liczb_pierwszych(tablica):
    licznik = 0
    for liczba in tablica:
        if czy_pierwsza(liczba):
            licznik += 1
    return licznik


# print(ile_liczb_pierwszych([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# zadanie_8
def czy_istnieje_srednia_sasiadow(tablica):
    for i in range(1, len(tablica) - 1):
        if tablica[i] == (tablica[i - 1] + tablica[i + 1]) / 2:
            return True
    return False


# print(czy_istnieje_srednia_sasiadow([1, 2, 3, 4, 5]))

# zadanie_9
def czy_liczba_jest_iloczynem(tablica):
    for liczba in tablica:
        for i in range(len(tablica)):
            for j in range(len(tablica)):
                if i != j and tablica[i] * tablica[j] == liczba:
                    return True
    return False


# print(czy_liczba_jest_iloczynem([1, 2, 3, 6]))


# zadanie_10
def liczba_z_najwiecej_czworkami(tablica):
    maks_czworek = -1
    wynik = -1
    for liczba in tablica:
        licznik = str(liczba).count('4')
        if licznik > maks_czworek:
            maks_czworek = licznik
            wynik = liczba
    return wynik



# print(liczba_z_najwiecej_czworkami([44, 444, 123]))


# zadanie_11
def ile_trojkatow(tablica):
    tablica.sort()
    licznik = 0
    maks_obwod = 0
    trojkat = ()
    for i in range(len(tablica) - 2):
        for j in range(i + 1, len(tablica) - 1):
            for k in range(j + 1, len(tablica)):
                if tablica[i] + tablica[j] > tablica[k]:
                    licznik += 1
                    obwod = tablica[i] + tablica[j] + tablica[k]
                    if obwod > maks_obwod:
                        maks_obwod = obwod
                        trojkat = (tablica[i], tablica[j], tablica[k])
    return licznik, trojkat


# print(ile_trojkatow([3, 4, 5, 6, 7]))

# zadanie_13
def najdluzszy_rosnacy(tablica):
    dlugosc = 1
    maks_dlugosc = 0
    poczatek = 0
    for i in range(1, len(tablica)):
        if tablica[i] > tablica[i - 1]:
            dlugosc += 1
        else:
            if dlugosc > maks_dlugosc:
                maks_dlugosc = dlugosc
                poczatek = i - dlugosc
            dlugosc = 1
    return tablica[poczatek:poczatek + maks_dlugosc]


print(najdluzszy_rosnacy([4, 5, 6, 1, 7, 9, 10, 8, 41]))

# zadanie_14
def najdluzszy_podciag_pierwszych(tablica):
    def czy_pierwsza(liczba):
        if liczba < 2:
            return False
        for i in range(2, int(liczba**0.5) + 1):
            if liczba % i == 0:
                return False
        return True

    dlugosc = 0
    maks_dlugosc = 0
    poczatek = 0
    for i in range(len(tablica)):
        if czy_pierwsza(tablica[i]):
            dlugosc += 1
            if dlugosc > maks_dlugosc:
                maks_dlugosc = dlugosc
                poczatek = i - dlugosc + 1
        else:
            dlugosc = 0
    return tablica[poczatek:poczatek + maks_dlugosc]


# print(najdluzszy_podciag_pierwszych([4, 5, 6, 2, 7, 5, 31, 8, 41]))

# zadanie_15
def sortuj_rosnaco(tablica):
    tablica = tablica.sort()

def sortuj_malejaco(tablica):
    tablica = tablica.sort(reverse=True)
    return tablica


def sortuj_leksykograficznie(tablica):
    n = len(tablica)
    tablica = [str(x) for x in tablica]
    for i in range(n):
        for j in range(0, n - i - 1):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
    return tablica


# print(sortuj_leksykograficznie([4, 5, 6, 1, 7, 9, 10, 8, 41]))
