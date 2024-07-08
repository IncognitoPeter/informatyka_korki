def czy_doskonala(n):
    count=0
    for i in range(1,n):
        if n % i == 0:
            count+=i
    print(count)
    if count==n:
        print('Tak')
    else:
        print('Nie')

czy_doskonala(20)