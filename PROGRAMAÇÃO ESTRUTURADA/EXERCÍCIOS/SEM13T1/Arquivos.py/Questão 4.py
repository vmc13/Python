par=[]
impar=[]
lista=[]
valor=0
for i in range(1, 20+1):
    valor=int(input(f'Insira o {i}º valor: '))
    lista.append(valor)
    if valor%2==0:
        par.append(valor)
    else:
        impar.append(valor)

print(f'Valores inseridos: \n{lista}')
print(f'Valores pares: \n{par}')
print(f'Valores ímpares: \n{impar}')
