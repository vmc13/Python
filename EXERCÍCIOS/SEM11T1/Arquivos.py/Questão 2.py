num=media=soma=cont=maior=menor=0

while True:
    num=int(input('Insira a sua idade: '))
    if num==0: break

    cont+=1
    soma+=num
    media=soma/(cont)
    
    if cont==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num

if cont!=0:
    print(f'\n{cont} pessoas inseriram suas idades.')
if media!=0:
    print(f'\nA média de idade é {media:.2f}.')

if menor!=0:
    print(f'\nA maior idade inserida foi {menor}.')
if maior!=0:
    print(f'\nA menor idade inserida foi {maior}.')
    
