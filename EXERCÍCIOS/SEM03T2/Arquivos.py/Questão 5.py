print('Cálculo do valor da bonificação')
print('')
anos=int(input('Digite a quantidade de anos de serviço: '))
valor_ano=float(input('Digite o valor recebido por ano: '))
bonus=anos*valor_ano
print("Seu bônus será de: RS %5.2f" % bonus)
