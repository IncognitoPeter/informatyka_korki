def czy_pierwsza(liczba):
    if liczba <= 1:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


def szukaj_unikatowych_pierwszych(liczba):
    specjalne_liczby = []
    for i in range(2, liczba):
        if liczba % i == 0:
            if czy_pierwsza(i):
                if i not in specjalne_liczby:
                    specjalne_liczby.append(i)
    return specjalne_liczby


print(szukaj_unikatowych_pierwszych(26))
