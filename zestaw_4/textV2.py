def print_subnumbers(n, k):
    # Oblicz długość liczby n
    n_copy = n
    dlugosc = 0
    while n_copy > 0:
        dlugosc += 1
        n_copy //= 10

    # Maskowanie bitowe
    for maska in range(1 << dlugosc):
        # Liczenie liczby jedynek w masce
        licznik_jedynek = 0
        tmp_maska = maska
        while tmp_maska > 0:
            if tmp_maska % 2 == 1:
                licznik_jedynek += 1
            tmp_maska //= 2

        if licznik_jedynek == k:
            sub_number = 0
            tmp_n = n
            mnoznik = 1
            for i in range(dlugosc):
                if maska & (1 << i):
                    # Pobierz odpowiednią cyfrę z n
                    cyfra = tmp_n % 10
                    sub_number = cyfra * mnoznik + sub_number
                    mnoznik *= 10
                tmp_n //= 10

            print(sub_number)


# Przykład użycia
print_subnumbers(12345, 3)
