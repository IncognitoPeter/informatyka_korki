def sprawdz_czy_da_sie_zsumowac_kwadraty(liczba):
    suma = 0
    for i in range(1, liczba, 2):
        suma += i * i
        if suma == liczba:
            return True
    return False


print(sprawdz_czy_da_sie_zsumowac_kwadraty(10))
