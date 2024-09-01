def czy_przestepny(rok):
    if rok % 400 == 0:
        print('tak')
    elif rok == 2100:
        print('nie')
    elif rok % 100 != 0 and rok % 4 == 0:
        print('tak')
    else:
        print('nie')


# year = int(input('podaj rok:'))
# czy_przestepny(year)

def cena_biletu(h, n, x):
    if n < 3 or n > 80:
        return 0
    elif h < 140:
        return 0.8 * x
    elif h > 200:
        return 1.2 * x
    else:
        return x


# print(cena_biletu(144, 14, 20))
# print(cena_biletu(133, 13, 20))
# print(cena_biletu(40, 2, 30))
# print(cena_biletu(210, 19, 50))

def pary(n):
    if n <= 1:
        print('brak')
    else:
        for a in range(1, n+1):
            b = n - a
            if a != 0 and b != 0:
                print(a, b)


# pary(4)

def nieparzyste(n):
    for i in range(n-1, 0, -1):
        if i % 2 != 0:
            print(i)


# nieparzyste(10)

def podzielne_przez_trzy(n):
    for i in range(1, n+1):
        if i % 3 == 0:
            print(i)


# podzielne_przez_trzy(17)

def dzielniki(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)


# dzielniki(17)

def cos_z_siedem(n):
    a = 0
    while a < n:
        odpowiedz = int(input('podaj liczbe'))
        if odpowiedz % 10 == 7:
            print(odpowiedz)
        a += 1


# cos_z_siedem(4)


def liczenie_cyfr(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count


# print(liczenie_cyfr(123421))


def suma_dzielnikow(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += i
    return count


# print(suma_dzielnikow(15))

def czy_doskonala(n):
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += i
    print(count)
    if count == n:
        print('Tak')
    else:
        print('Nie')


# czy_doskonala(20)

def podzielnosc(n, a, b):
    for i in range(1, n+1):
        if i % a == 0 and i % b != 0:
            print(i)


# podzielnosc(10, 4, 4)


def pary_1(n):
    if n < 1:
        print('brak')
    else:
        for a in range(1, n+1):
            b = n // a
            if a != 0 and b != 0:
                if a * b == n:
                    print(a, b)


# pary_1(7)
