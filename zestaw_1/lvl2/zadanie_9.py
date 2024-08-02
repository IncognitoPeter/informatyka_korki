def sprawdz_czy_cyfra_rowna_liczbie_cyfr(liczba):
    ilosc = 0
    liczba_pom=liczba
    while liczba_pom > 0:
        ilosc +=1
        liczba_pom = liczba_pom // 10
    while liczba > 0:
        if liczba % 10 == ilosc:
            return True
        liczba = liczba // 10
    return False


a = 25
print(sprawdz_czy_cyfra_rowna_liczbie_cyfr(a))
