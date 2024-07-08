def cena_biletu(H,N,x):
    if N<3 or N>80:
        return 0
    elif H<140:
        return 0.8*x
    elif H>200:
        return 1.2*x
    else:
        return x

print(cena_biletu(144,14,20))
print(cena_biletu(133,13,20))
print(cena_biletu(40,2,30))
print(cena_biletu(210,19,50))