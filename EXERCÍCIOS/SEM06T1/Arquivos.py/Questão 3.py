def cor(n):
    if n.upper()=='V':
        return 'Siga'
    elif n.upper()=='A':
        return 'Atenção'
    elif n.upper()=='E':
        return 'Pare'


sinal=input('Digite V para verde, A para amarelo e E para vermelho: ')
result=cor(sinal)
print(f'O sinal indica {result}')
    
