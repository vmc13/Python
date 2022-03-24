def sig(x,y):
    if x>=21 and x<=31 and y==3 or x>=1 and x<=19 and y==4:
        return print('Áries')
    elif x>=20 and x<=30 and y==4 or x>=1 and x<=20 and y==5:
        return print('Touro')
    elif x>=21 and x<=31 and y==5 or x>=1 and x<=21 and y==6:
        return print('Gêmeos')
    elif x>=22 and x<=30 and y==6 or x>=1 and x<=22 and y==7:
        return print('Câncer')
    elif x>=23 and x<=31 and y==7 or x>=1 and x<=22 and y==8:
        return print('Leão')
    elif x>=23 and x<=31 and y==8 or x>=1 and x<=22 and y==9:
        return print('Virgem')
    elif x>=23 and x<=30 and y==9 or x>=1 and x<=22 and y==10:
        return print('Libra')
    elif x>=23 and x<=31 and y==10 or x>=1 and x<=21 and y==11:
        return print('Escorpião')
    elif x>=22 and x<=30 and y==11 or x>=1 and x<=21 and y==12:
        return print('Sagitário')
    elif x>=22 and x<=31 and y==12 or x>=1 and x<=19 and y==1:
        return print('Capricórnio')
    elif x>=20 and x<=31 and y==1 or x>=1 and x<=18 and y==2:
        return print('Aquário')
    elif x>=19 and x<=29 and y==2 or x>=1 and x<=20 and y==3:
        return print('Peixes')
    else:()


dia=int(input('Digite o dia do seu nascimento: '))
mes=int(input('Digite o mês do seu nascimento: '))
signo=sig(dia,mes)
