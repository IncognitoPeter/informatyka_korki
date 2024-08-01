def pary(n):
    if n <= 1:
        print('brak')
    else:
        for a in range(1, n+1):
            b = n - a
            if a != 0 and b != 0:
                print(a, b)


pary(4)
