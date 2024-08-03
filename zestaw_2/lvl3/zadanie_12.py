def zaszyfruj_cyfry_w_liczbie(liczba):
    zaszyfrowane = []
    cyfry = 0
    liczba_pom = liczba
    while liczba_pom != 0:
        liczba_pom = liczba_pom // 10
        cyfry += 1
    while liczba > 0:
        if cyfry == 1:
            if liczba == 9:
                zaszyfrowane.append(0)
                zaszyfrowane.append(1)
        cyfra = liczba % 10
        if liczba == 9:
            zaszyfrowane.append(0)
        else:
            cyfra += 1
            zaszyfrowane.append(cyfra)
        liczba = liczba // 10
    zaszyfrowane.reverse()
    for i in zaszyfrowane:
        print(i, end="")


zaszyfruj_cyfry_w_liczbie(156)
