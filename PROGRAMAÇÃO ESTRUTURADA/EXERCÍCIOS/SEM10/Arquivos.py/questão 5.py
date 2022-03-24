salario=int(input('Informe o valor inicial do seu salário: '))
divida=int(input('Informe o valor inicial da sua dívida: '))

aumento_sal=5/100
aumento_div=15/100
mes=10
ano=2016
cont=0

while divida<salario:
    mes+=1
    divida_hoje=divida+(divida*aumento_div)
    divida=divida_hoje
    
    if mes==12:
        ano+=1
        mes=cont
        
    if mes==3:
        sal_hoje=salario*aumento_sal
        salario+=sal_hoje
        
    if divida>salario: break

print(f'O valor da sua dívida irá sueprar o valor do salário em: {mes}/{ano}')
