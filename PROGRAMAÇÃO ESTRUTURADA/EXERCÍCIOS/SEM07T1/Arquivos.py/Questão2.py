def data(a,b,c,a1,b1,c1):
    d1=(a,b,c)
    d2=(a1,b1,c1)
    if d1>d2:
        return print(f'A data mais recente é: {a}/{b}/{c}')
    else:
        return print(f'A data mais recente é: {a1}/{b1}/{c1}')


d1=int(input('Digite o primeiro dia: '))
m1=int(input('Digite o primeiro mês: '))
a1=int(input('Digite o primeiro ano: '))
d2=int(input('Digite o segundo dia: '))
m2=int(input('Digite o segundo mês: '))
a2=int(input('Digite o segundo ano: '))
dt=data(d1,m1,a1,d2,m2,a2)
