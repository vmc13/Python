lista=[]
while True:
    val=int(input('Insira um valor: '))
    if val==0:
        break
    lista.append(val)

quant=int(input('Digite o valor que você quer pesquisar: '))
soma=0
for x in lista:
    if quant==x:
        soma+=1

print(f'Lista dos valores inseridos:\n{lista}')
print(f'O valor que você inseriu para pesquisa foi: {quant}')
print(f'O valor {quant} repetiu {soma} vezes')
