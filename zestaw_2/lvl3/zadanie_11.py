def zamiana_na_dwojkowy(liczba):
    tab = []
    while liczba != 0:
        cyfra = liczba % 2
        tab.append(cyfra)
        liczba = liczba // 2
    tab.reverse()
    for i in tab:
        print(i, end="")


zamiana_na_dwojkowy(54)
