def cos_z_siedem(n):
    a = 0
    while a < n:
        odpowiedz = int(input('podaj liczbe'))
        if odpowiedz % 10 == 7:
            print(odpowiedz)
        a += 1


cos_z_siedem(4)
