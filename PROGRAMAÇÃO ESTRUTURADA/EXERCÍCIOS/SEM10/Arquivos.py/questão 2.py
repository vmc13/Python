num=0
soma=0
media=0
cont=0
while True:
    n=int(input('Insira um número: '))
    if n!=0:
        soma+=n
        cont+=1
        media=soma/cont
    if n==0: break

if media!=0:
    print(f'A média aritmética de todos os números inserios será: {media:.2f}')
        
