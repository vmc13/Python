from random import *

executa = True
macho = ['Ace' , 'Bóris' , 'Coldie' , 'Dankan' , 'Eagle' , 'Fidel' , 'Gordon' , 
        'Hasso' , 'Ike' ,  'Jango' ,  'Kodak' , 'Luiggi' , 'Musk' , 
        'Níquel' , 'Orion' , 'Polo' , 'Redy' , 'Saik' , 'Tommy' , 
        'Urano' , 'Wide' , 'Xarope' , 'Yorick' , 'Ziggs']

femea = ['Aika' , 'Betsy' , 'Charlotte' , 'Dara' , 'Ema' , 
        'Floribella' , 'Garapa' , 'Indira' , 'Jade' , 
        'Kiara' , 'Lilith' , 'Meg' , 'Nadja' , 
        'Ohana' ,  'Priscilla' , 'Redy' , 'Shira' , 'Talita' , 
        'Úrsula' , 'Valeska' , 'Whiska' ,  'Xena' , 'Yuca' , 'Zyra']

print('Serviço de escolha de nome para animais de estimação')
print('====================================================')

animal = input('Qual é o seu animal?: ')

print(''' 
Menu
  c = Obter nome
  a = Adicionar nome
  d = Remover nome
  p = Imprimir nomes
  q = Sair
''')

while executa == True:
    menuChoice = input('\n>_').lower()[0]

    #'c' para um nome
    if menuChoice == 'c':
        sexo=input('Seu animal é macho ou fêmea?: ').lower()[0]
        print('Aqui está o nome para o seu' , animal , ':')
        #obtém um item aleatório de ambas ass listas e adiciona-os ao cumprimento
        if sexo == 'f':
            print(choice(femea))
        elif sexo == 'm':
            print(choice(macho))
        else:
            print('Entrada inválida')

    #'a' para adicionar outro nome
    elif menuChoice == 'a':
        itemToAdd = input("Adicione um nome: ")
        form=input('Esse nome é masculino ou feminino?:').lower()[0]
        if form == 'f':
            if itemToAdd not in femea:
                femea.append(itemToAdd)
                print('Nome adicionado!')
            else:
                print('O nome já está na lista!')
        elif form == 'm':
            if itemToAdd not in macho:
                macho.append(itemToAdd)
                print('Nome adicionado!')
            else:
                print('O nome já está na lista!')
        else:
            print('Entrada inválida')

    #'d' para remover um nome
    elif menuChoice == 'd':
        itemToDelete = input('Insira o nome a ser removido: ')
        if itemToDelete in femea:
            femea.remove(itemToDelete)
            print('Nome removido!')
        elif itemToDelete in macho:
            macho.remove(itemToDelete)
            print('Nome removido!')
        else:
            print('O nome não está na lista!')

    #'p' para imprimir a lista de nomes
    elif menuChoice == 'p':
        print(f'Nomes para macho: {macho}')
        print(f'Nomes para fêmea: {femea}')

    #'q' para sair
    elif menuChoice == 'q':
        executa = False
        print('Obrigado por usar o programa!')
    
    else:
        print('Insira uma opção válida')