a = 25
b = 17


def czy_wzglednie_pierwsze(liczba1, liczba2):
    while liczba2 != 0:
        liczba1, liczba2 = liczba2, liczba1 % liczba2
    if liczba1 == 1:
        return True
    return False


print(czy_wzglednie_pierwsze(a, b))
