# szyfr cezara
def szyfruj_cezarem(napis, klucz):
    zaszyfrowane = ''
    for i in napis:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            zaszyfrowane += chr((ord(i) - ord('A') + klucz) % 26 + ord('A'))
        elif ord(i) >= ord('a') and ord(i) <= ord('z'):
            zaszyfrowane += chr((ord(i) - ord('a') + klucz) % 26 + ord('a'))
    return zaszyfrowane


def odszyfruj_cezarem(napis, klucz):
    odszyfrowane = ''
    for i in napis:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            odszyfrowane += chr((ord(i) - ord('A') + klucz) % 26 + ord('A'))
        elif ord(i) >= ord('a') and ord(i) <= ord('z'):
            odszyfrowane += chr((ord(i) - ord('a') + klucz) % 26 + ord('a'))
    return odszyfrowane


# print(szyfruj_cezarem('kamilekmanilek', 3))
# print(odszyfruj_cezarem(szyfruj_cezarem('kamilekmanilek', 3),-3))


# szyfr płotowy
def szyfruj_plotowo(napis, poziomy):
    zaszyfrowane = ''
    for i in range(poziomy):
        poziom = i
        while i < len(napis):
            zaszyfrowane += napis[i]
            i += 1
    return zaszyfrowane


# print(szyfruj_plotowo('kamilekmanilek', 3))


# szyfr rsa
def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def rsa():
    p = 7
    q = 17
    n = p * q
    fi = (p - 1) * (q - 1)
    e = 2
    while e < fi:
        if nwd(e, fi) == 1:
            break
        e += 1
    d = 2
    while d * e % fi != 1:
        d += 1
    return (n, e), (n, d)

# print(rsa())
