valor=soma=H=C=M=A=Q=X=0
opcao=''
while opcao!='X':
    print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
    opcao=input().upper()[0]
    soma+=valor
    
    if opcao=='H':
        valor=5.50
    elif opcao=='C':
        valor=6.80
    elif opcao=='M':
        valor=4.50
    elif opcao=='A':
        valor=7.00
    elif opcao=='Q':
        valor=4.00
    elif opcao=='X':
        break
    else:
        print('Opção inválida')

     
print(f'A soma dos itens será: {soma:.2f}')
    
