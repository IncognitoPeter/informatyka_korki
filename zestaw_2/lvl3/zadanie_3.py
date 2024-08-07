def znajdz_rozne_cyfry(liczba):
    tab = []
    while liczba > 0:
        cyfra = liczba % 10
        if cyfra not in tab:
            tab.append(cyfra)
        liczba = liczba // 10
    return len(tab)


print(znajdz_rozne_cyfry(1255))
