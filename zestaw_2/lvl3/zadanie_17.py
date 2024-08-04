def sprawdz_czy_cyfry_tworza_ciag_geometryczny(liczba):
    tab = []
    while liczba != 0:
        cyfra = liczba % 10
        tab.append(cyfra)
        liczba = liczba // 10
    iloraz_ciagu = tab[0] / tab[1]
    for i in range(len(tab)-1):
        if iloraz_ciagu != tab[i] / tab[i+1]:
            return False
    return True


print(sprawdz_czy_cyfry_tworza_ciag_geometryczny(248))
