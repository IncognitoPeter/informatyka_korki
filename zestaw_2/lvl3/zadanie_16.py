def sprawdz_czy_cyfry_tworza_ciag_arytmetyczny(liczba):
    tab = []
    while liczba != 0:
        cyfra = liczba % 10
        tab.append(cyfra)
        liczba = liczba // 10
    roznica_ciagu = tab[0] - tab[1]
    for i in range(len(tab)-1):
        if roznica_ciagu != tab[i] - tab[i+1]:
            return False
    return True


print(sprawdz_czy_cyfry_tworza_ciag_arytmetyczny(123))
