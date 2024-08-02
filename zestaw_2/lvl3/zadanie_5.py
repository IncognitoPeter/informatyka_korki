def czy_pierwsza(liczba):
    if liczba <= 1:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


def suma_dzielnikow_pierwszych(liczba):
    specjalne_liczby = []
    for i in range(2, liczba):
        if liczba % i == 0:
            if czy_pierwsza(i):
                specjalne_liczby.append(i)
    return sum(specjalne_liczby)

print(suma_dzielnikow_pierwszych(26))
