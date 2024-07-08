def podzielnosc(n,a,b):
    for i in range(1,n+1):
        if i%a==0 and i%b!=0:
            print(i)

podzielnosc(10,4,4)