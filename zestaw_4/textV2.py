def div(a, b):
    nowa = 0
    liczba = a
    wynik = 0
    while liczba != 0:
        cyfra = liczba % 10
        nowa = nowa * 10 + cyfra
        liczba = liczba // 10


print(div(51, 17))