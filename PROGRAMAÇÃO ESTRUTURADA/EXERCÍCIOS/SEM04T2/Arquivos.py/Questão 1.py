def calcular(a, b, c):
    return 2*a+5*b-c



n1=int(input('Dê um valor: '))
n2=int(input('Dê um segundo valor: '))
n3=int(input('Dê um terceiro valor: '))
calcular(n1, n2, n3)
print(f'O resultado do cálculo 2*{n1}+5*{n2}-{n3} será: {calcular(n1, n2, n3)}')
