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
