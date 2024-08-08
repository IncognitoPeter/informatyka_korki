def sprawdz_czy_jest_kwadratem(liczba):
    for i in range(liczba // 2):
        if i * i == liczba:
            return i
    return -1


# print(sprawdz_czy_jest_kwadratem(25))

def sprawdz_czy_jest_szescianem(liczba):
    for i in range(liczba // 2):
        if i * i * i == liczba:
            return i
    return -1


# print(sprawdz_czy_jest_szescianem(8))

def znajdz_rozne_cyfry(liczba):
    zero, jeden, dwa, trzy, cztery, piec = 0, 0, 0, 0, 0, 0
    szesc, siedem, osiem, dziewiec, rozne_cyfry = 0, 0, 0, 0, 0
    while liczba != 0:
        cyfra = liczba % 10
        if cyfra == 0 and zero == 0:
            zero += 1
            rozne_cyfry += 1
        if cyfra == 1 and jeden == 0:
            jeden += 1
            rozne_cyfry += 1
        if cyfra == 2 and dwa == 0:
            dwa += 1
            rozne_cyfry += 1
        if cyfra == 3 and trzy == 0:
            trzy += 1
            rozne_cyfry += 1
        if cyfra == 4 and cztery == 0:
            cztery += 1
            rozne_cyfry += 1
        if cyfra == 5 and piec == 0:
            piec += 1
            rozne_cyfry += 1
        if cyfra == 6 and szesc == 0:
            szesc += 1
            rozne_cyfry += 1
        if cyfra == 7 and siedem == 0:
            siedem += 1
            rozne_cyfry += 1
        if cyfra == 8 and osiem == 0:
            osiem += 1
            rozne_cyfry += 1
        if cyfra == 9 and dziewiec == 0:
            dziewiec += 1
            rozne_cyfry += 1
        liczba = liczba // 10
    return rozne_cyfry


# print(znajdz_rozne_cyfry(1255))

