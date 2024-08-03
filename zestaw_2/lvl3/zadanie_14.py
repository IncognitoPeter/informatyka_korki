def rozklad_na_iloczyn():
    roznica = 1000000
    liczba1 = 0
    liczba2 = 0
    liczba = int(input("podaj liczbe:\n"))
    for i in range(1, liczba + 1):
        for j in range(1, roznica + 1):
            if i * j == liczba:
                if roznica > j - i or roznica > i - j:
                    liczba1 = i
                    liczba2 = j

    return liczba1, liczba2

print(rozklad_na_iloczyn())