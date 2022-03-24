n=int(input('Digite um número: '))
n1=0
n2=1
cont=soma=0
for i in range(0, n):
    n1=n2
    n2=soma
    print(f'{n2}', end=', ' if cont<n-1 else ' ')
    soma=n1+n2
    cont+=1
