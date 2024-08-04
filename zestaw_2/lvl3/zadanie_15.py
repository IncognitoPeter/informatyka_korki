def sprawdz_czy_cyfry_tworza_ciag_rosnacy(liczba):
    tab = []
    while liczba != 0:
        cyfra = liczba % 10
        tab.append(cyfra)
        liczba = liczba//10
    for i in range(len(tab)-1):
        if tab[i] < tab[i+1]:
            return False
    return True


print(sprawdz_czy_cyfry_tworza_ciag_rosnacy(123))
