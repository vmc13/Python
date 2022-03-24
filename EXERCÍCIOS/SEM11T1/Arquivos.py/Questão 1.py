print('Soma de números inteiros\n')

prog=True
num=0
soma=0
while prog==True:
    num=int(input('Digite um número inteiro: '))
    soma+=num
    if num==0:
        break

print(f'\nA soma dos números digitados é {soma}')
