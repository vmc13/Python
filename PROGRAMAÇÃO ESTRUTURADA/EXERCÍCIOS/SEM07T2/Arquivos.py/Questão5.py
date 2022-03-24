def cresc(x,y,z):
    if x<=y and x<=z and y<=z:
        return print(f'{x}\n{y}\n{z}')
    elif x<=y and x<=z and z<=b:
        return print (f'{x}\n{z}\n{y}')
    elif y<=x and y<=z and x<=z:
        return print(f'{y}\n{x}\n{z}')
    elif y<=x and y<=z and z<=x:
        return print(f'{y}\n{z}\n{x}')
    elif z<=x and z<=y and x<=y:
        return print(f'{z}\n{x}\n{y}')
    elif z<=x and z<=y and y<=x:
        return print (f'{z}\n{y}\n{x}')
    else:
        return ValueError


n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número: '))
n3=int(input('Digite o terceiro número: '))
ordem=cresc(n1,n2,n3)
