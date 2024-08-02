def sprawdz_czy_da_sie_zsumowac(liczba, m):
    suma = 0
    for i in range(1, m, 2):
        if suma == liczba:
            return True
        suma += i


print(sprawdz_czy_da_sie_zsumowac(13, 7))
