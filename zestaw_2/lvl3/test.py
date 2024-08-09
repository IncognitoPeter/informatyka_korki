def sprawdz_czy_cyfry_tworza_ciag_rosnacy(liczba):
    while liczba != 0:
        cyfra_1 = liczba % 10
        liczba = liczba // 10
        cyfra_2 = liczba % 10
        if cyfra_1 <= cyfra_2:
            return False
    return True


print(sprawdz_czy_cyfry_tworza_ciag_rosnacy(123))
