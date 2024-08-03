def sprawdz_czy_palindrom(liczba):
    tab = []
    liczba_pom = liczba
    nowa = 0
    mnoznik = 1
    while liczba_pom != 0:
        cyfra = liczba_pom % 10
        tab.append(cyfra)
        liczba_pom = liczba_pom // 10
    tab.reverse()
    for i in range(len(tab)):
        nowa += tab[i] * mnoznik
        mnoznik *= 10
    if nowa == liczba:
        return True
    else:
        return False


print(sprawdz_czy_palindrom(167))
