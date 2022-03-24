from random import *

jogando=True
score=0

print('''
Vinte e um!
===========
Tente fazer exatamente 21 pontos!
''')

while jogando==True:
    num=randint(1,10)
    score=score+num

    print(f'\nSeu próximo número é {num}')
    print(f'Sua pontuação agora é {score}')

    print('\nGostaria de somar mais um número? (s/n)')
    resp=input().lower()
    if resp=='n' or score>21:
        jogando=False

print(f'\nSua pontuação final é {score}')

if score==21:
    print('VOCÊ VENCEU!!')
else:
    print('Que pena!')
