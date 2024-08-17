def add_v2(a, b, k):
    liczba_1 = 0
    liczba_2 = 0
    mnoznik = 1
    nowa = 0
    while a != 0:
        cyfra_a = a % k
        liczba_1 += cyfra_a * mnoznik
        a = a // k
        mnoznik *= 10
    mnoznik = 1
    while b != 0:
        cyfra_b = b % k
        liczba_2 += cyfra_b * mnoznik
        b = b // k
        mnoznik *= 10
    mnoznik = 1
    while liczba_1 != 0 or liczba_2 != 0:
        cyfra_1 = liczba_1 % k
        cyfra_2 = liczba_2 % k
        if cyfra_1 + cyfra_2 >= k:
            nowa += (cyfra_1 + cyfra_2 - k) + k * mnoznik
        else:
            nowa += (cyfra_1 + cyfra_2) * mnoznik
        mnoznik *= 10
        liczba_1 = liczba_1 // 10
        liczba_2 = liczba_2 // 10

    return liczba_1, liczba_2, nowa


print(add_v2(14, 17, 10))
