a = 126


def sprawdz_parzystosc_ilosc_nieparzystych_cyfr(liczba):
    ilosc = 0
    while liczba > 0:
        if liczba % 10 % 2 != 0:
            ilosc += 1
        liczba = liczba // 10
    if ilosc % 2 == 0:
        return True
    return False


print(sprawdz_parzystosc_ilosc_nieparzystych_cyfr(a))
