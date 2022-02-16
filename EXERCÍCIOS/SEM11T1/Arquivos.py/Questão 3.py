while True:
    print('''OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')
    opcao=int(input('\n'))
    valor=opcao
    if valor==0:
        print('0 - Fim de serviço.\n')
        break  
    elif valor==1:
        print('1 - Olá. Como vai?\n')
    elif valor==2:
        print('2 - Vamos estudar mais.\n')
    elif valor==3:
        print('3 - Meus Parabéns!\n')
    else:
        print('Opção inválida.\n')
