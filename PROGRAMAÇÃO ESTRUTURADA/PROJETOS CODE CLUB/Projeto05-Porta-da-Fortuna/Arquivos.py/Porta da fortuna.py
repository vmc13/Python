from random import *

#O usuário muda esta variável para terminar o jogo
jogando = True
score=0

#Imprima as 3 portas e as instruções do jogo
print('''
Porta da fortuna!
=================

Existe um super prêmio atrás de uma desats 3 portas!
Advinhe qual é a porta certa para ganhar o prêmio!

    _____   _____   _____
   |     | |     | |     |
   | [1] | | [2] | | [3] |
   |    0| |    o| |    o|
   |_____| |_____| |_____|

    ''')

#Repetir, enquanto a variável 'jogando estiver com o valor 'True'
while jogando==True:

    print('\nEscolha uma porta (1, 2 ou 3): ')

    #pegue a porta escolhida e a armazene como um numero inteiro(int)
    portaEscolhida=int(input())

    #Escolha aleatoriamente a porta que esconde o prêmio (entre 1 e 3)
    portaCerta=randint(1,3)

    #Mostre ao jogador qual a porta ele escolheu e qual era a certa
    print(f'A porta escolhida foi a {portaEscolhida}')
    print(f'A porta certa é a {portaCerta}')

    #O jogador ganha se o número da porta escolhida e o da porta certa forem o mesmo
    if portaEscolhida==portaCerta:
        print('Parabens!')
        score+=1
    else:
        score=0
        print('Que peninha!')

    print(f'Sua pontuação é: {score}')

    #Pergunte ao jogador se ele quer continuar jogando
    print('\nVocê quer jogar de novo? (s/n)')
    resposta=input().lower()
    #Termina o jogo se digitar 'n'
    if resposta =='s':
        jogando=True
        
    else:
       jogando=False

print('Obrigado por jogar!')
print(f'Sua pontuação final é de: {score}')
