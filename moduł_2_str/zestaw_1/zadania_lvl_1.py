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
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    napis = napis.lower()
    for i in napis:
        alfabet = alfabet.replace(i, '')
    return alfabet

# print(lipogram('Słońce tego dnia wstało jakieś dziwnie leniwe, matowe bez blasku. Około południa na powleczone'))

# zadanie_6


def panagram(napis):
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in napis:
        if i not in alfabet:
            return False
    return True

# print(panagram('fdf3d'))

# zadanie_7


def alfabeton(napis):
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    alfabet_1 = ''
    napis = napis.lower()
    for i in napis:
        if i in alfabet:
            if i in alfabet_1:
                return False
        alfabet_1 += i
    return True

# print(alfabeton('aabcdefghijklmnopqrstuvwxyz'))

# zadanie_8


def minimalne_podslowo(napis):
    slowo = ''
    napis = napis.replace(' ', '')
    napis = napis.lower()
    print(min(napis))
    for i in range(3):
        a = min(napis)
        slowo += a
        napis = napis.replace(a, '')
    return slowo


# print(minimalne_podslowo('Halina pije wodę w Kołaczycach'))

# zadanie_9


def nieczytelne_liczby(liczba_1, liczba_2):
    if len(liczba_1) != len(liczba_2):
        if len(liczba_1) > len(liczba_2):
            return 1
        else:
            return 2
    for i in range(len(liczba_1)):
        cyfra_1 = liczba_1[i]
        cyfra_2 = liczba_2[i]
        if cyfra_1 == '?' and cyfra_2 == '?':
            continue
        elif cyfra_1 == '?' and cyfra_2 != '?':
            return -1
        elif cyfra_1 != '?' and cyfra_2 == '?':
            return -1
        elif cyfra_1 > cyfra_2:
            return 1
        elif cyfra_1 < cyfra_2:
            return 2


# print(nieczytelne_liczby('?31418?1249?00111????','931?919191?11919?????'))

# zadanie_10


def kod_dna_v1(koddna):
    dlugosc_v0 = 0
    start_v0 = 1
    dlugosc_v1 = 0
    start_v1 = -1
    for i in range(len(koddna)):
        if koddna[i] == 'T':
            if dlugosc_v1 == 0:
                start_v1 = i
            dlugosc_v1 += 1
        else:
            if dlugosc_v1 > dlugosc_v0:
                dlugosc_v0 = dlugosc_v1
                start_v0 = start_v1
            dlugosc_v1 = 0
    if dlugosc_v1 > dlugosc_v0:
        dlugosc_v0 = dlugosc_v1
        start_v0 = start_v1
    return start_v0, dlugosc_v0


# print(kod_dna_v1('GTATGTTATTTTTTAAGCACTCACTCGGGGTTACGTTCTTTATGCTATTGCCTCG'))


def kod_dna_v2(koddna):
    fragment_v0 = ""
    fragment_v1 = koddna[0]
    for i in range(1, len(koddna)):
        if koddna[i] != koddna[i - 1]:
            fragment_v1 += koddna[i]
        else:
            if len(fragment_v1) > len(fragment_v0):
                fragment_v0 = fragment_v1
            fragment_v1 = koddna[i]
    if len(fragment_v1) > len(fragment_v0):
        fragment_v0 = fragment_v1
    return fragment_v0


# print(kod_dna_v2('GTATGTTATTTTTTAAGCACTCACTCGGGGTTACGTTCTTTATGCTATTGCCTCG'))
