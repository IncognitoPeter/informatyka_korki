def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(nwd(24, 6))
