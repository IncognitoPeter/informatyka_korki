# zadanie_1
def czy_palindrom(napis):
    return napis == napis[::-1]

# print(czy_palindrom('nan'))


# zadanie_2
def czy_palindrom2(napis):
    napis = napis.lower()
    napis = napis.strip()
    napis = napis.replace(' ', '')
    napis = napis.replace(',', '')
    napis = napis.replace('?', '')
    napis = napis.replace('(', '')
    napis = napis.replace(')', '')
    return napis == napis[::-1]


# print(czy_palindrom2("Ado, pyta bandzior komu mokro? I z dna baty poda?"))

# zadanie_3
def palindromowy_preffiks(napis):
    for i in range(len(napis), 0, -1):
        if czy_palindrom(napis[:i]):
            return napis[:i]


# print(palindromowy_preffiks('kajakiem opływam polske'))

# zadanie_4


def prefiks_sufiks(napis):
    napis = napis.lower()
    for i in range(len(napis) - 1, 0, -1):
        if napis[:i] == napis[-i:]:
            return napis[:i]


# print(prefiks_sufiks("Ranna Panna Anna czyta Koran"))

# zadanie_5
def lipogram(napis):
    napis = napis.lower()
    for i in napis:
        napis = napis.replace(i, '')
    return napis

print(lipogram('Słońce tego dnia wstało jakieś dziwnie leniwe, matowe bez blasku. Około południa na powleczone niezwykłą bladością niebo wypełzły'))

# zadanie_6
def panagram(napis):
    return napis.isalpha()

#print(panagram('fdf3d'))

# zadanie_7
def alfabeton():
    pass

# zadanie_8
def minimalne_podsłowo():
    pass

# zadanie_9
def nieczytelne_liczby():
    pass

# zadanie_10
def kod_DNA():
    pass


