def rozklad_na_iloczyn():
    liczba1 = 0
    liczba2 = 0
    liczba = int(input('podaj liczbe: \n'))
    for i in range(liczba//2):
        if i*i <= liczba:
            liczba1 = i
    for i in range(liczba//2):
        if liczba1*i == liczba:
            liczba2 = i
    return liczba1, liczba2


print(rozklad_na_iloczyn())
