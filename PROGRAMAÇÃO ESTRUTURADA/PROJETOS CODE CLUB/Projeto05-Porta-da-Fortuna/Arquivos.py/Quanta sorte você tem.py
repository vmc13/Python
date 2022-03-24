from random import *

#Essa variável guarda o número de vezes que o jogo já foi jogado
tentativas=0
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

#Repita enquanto a variável score for menor do que 3
while score<3:
    #Soma 1 ao número de tentativas
    tentativas+=1

    print('\nTentativa', tentativas, ': Escolha uma porta (1, 2 ou 3).')

    #Pegue a porta escolhida e a armazene como um número interio
    portaEscolhida=int(input())

    #Escolha aleatoriamente a porta que esconde o prêmio(entre 1 e 3)
    portaCerta=randint(1,3)

    #mostre ao jogador qual porta ele escolheu e qual era a porta certa
    print('A porta escolhida foi a', portaEscolhida)
    print('A porta certa é a', portaCerta)

    #O jogador ganha se o número da porta escolhida e o da porta certa forem o mesmo
    if portaEscolhida==portaCerta:
        print('Parabéns!')
        score+=1
    else:
        print('Que peninha!')

    print('Sua pontuação atual é', score)

print('\n**Você conseguiu! Terminou o jogo em', tentativas, 'tentativas **')
