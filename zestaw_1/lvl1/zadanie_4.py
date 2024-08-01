def nieparzyste(n):
    for i in range(n-1, 0, -1):
        if i % 2 != 0:
            print(i)


nieparzyste(10)
