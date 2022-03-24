print('Game Ímpar ou Par')
print('=-'*20)

import random

nome=input('Insira o nome do jogador: ')
a=0
pc=random.randint(0,10)

while True:
    ult=input('Ímpar ou par? ').lower()
    if (ult=='par' or ult=='ímpar'):
        break
    else:
        print('Insira ímpar ou par: ')

if ult=='par':
    par=ult
    ímpar=pc
elif ult=='ímpar':
    ímpar=ult
    par=pc

num=input('Insira um número de 0 a 10: ')
pc=random.randint(1,10)
print(f'\nComputador escolheu: {pc}')
print(f'{nome} escolheu {num}')

total=int(num)+pc
print(f'A soma é: {total}')

print('=-'*20)

pc='0'
if total%2==0:
    print('O resultado é par!')
    pc='par'

else:
    print('O resultado é ímpar!')
    pc='ímpar'

if ult=='par' and pc =='par':
    print(f'Vencedor: {nome}')
elif ult=='ímpar' and pc=='ímpar':
    print(f'Vencedor: {nome}')
else:
    print(f'Vencedor: Computador')
