def notas(x, y, z):
    nota1=x
    nota2=y
    nota3=z
    media=(x+y+z)//3
    if z >8:
        return media+1
    else:
        return media


n1=int(input('Digite a primeira nota: '))
n2=int(input('Digite a segunda nota: '))
n3=int(input('Digite a terceira nota: '))

if notas(n1, n2, n3)>10:
    print(f'Sua média é 10')
else:
        print(f'Sua média é {notas(n1, n2, n3)}')
