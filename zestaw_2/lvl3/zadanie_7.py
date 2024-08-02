def sprawdz_czy_liczba_to_trzy_kwadraty(liczba):
    for i in range(liczba):
        if i * i + (i + 1) * (i + 1) + (i + 2) * (i + 2) == liczba:
            return i
    return -1


print(sprawdz_czy_liczba_to_trzy_kwadraty(50))
