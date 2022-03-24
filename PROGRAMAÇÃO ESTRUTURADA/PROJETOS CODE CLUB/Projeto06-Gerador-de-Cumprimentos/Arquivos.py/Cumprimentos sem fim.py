from random import *

#O programa continua em execução enquanto a variável for verdadeira 'True'
executa = True

adjetivos = ['maravilhoso' , 'acima da média' , 'excelente']
hobbies = ['andar de bicicleta' , 'programar' , 'fazer chá']

print('Gerador de cumprimentos')
print('-----------------------')

nome = input('Qual é o seu nome?: ')

print('''
Menu
  c = obter cumpirmento
  q = sair
''')

while executa == True:
    menuChoice = input('\n>_').lower()

    #c para um cumpirmento
    if menuChoice == 'c':
        print("Aqui está o seu cumprimento" , nome , ":" )
    #obtém um itemaleatório de ambas ass listas e adiciona-os ao cumprimento
    print(nome , 'você é', choice(adjetivos) , 'em' , choice(hobbies))
    print('De nada!')

    #q para sair
    elif menuChoice == 'q':
         executa = False

    else:
        print('Escolha uma opção válida!')