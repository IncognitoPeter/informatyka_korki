def czy_przestepny(rok):
    if rok%400==0:
        print('tak')
    elif rok==2100:
       print('nie')
    elif rok%100!=0 and rok%4==0:
        print('tak')
    else:
        print('nie')

rok=int(input('podaj rok:'))
czy_przestepny(rok)

