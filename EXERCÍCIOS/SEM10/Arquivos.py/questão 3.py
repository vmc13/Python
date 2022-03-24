num=0
maior=0
menor=0
cont=0
while True:
    n=int(input('Insira um número inteiro positivo: '))
    cont+=1
    if n==0: break
    if cont==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n 

if maior!=0:
    print(f'O maior número lido é: {maior:.0f}')

if menor!=0:
    print(f'O menor número lido é: {menor:.0f}')
        
