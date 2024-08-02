def sprawdz_czy_liczba_to_dwa_kwadraty(liczba):
    for i in range(liczba):
        if i * i + (i + 1) * (i + 1) == liczba:
            return i
    return -1


print(sprawdz_czy_liczba_to_dwa_kwadraty(41))
