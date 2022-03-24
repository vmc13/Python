n=int(input('Digite um número: '))
i=1
cont=0
while i<=n:
    if n%i==0:
        cont+=1
    i+=1
    
if cont>2:
    print('O número inserido não é primo.')
else:
    print('O número inserido é primo.')
