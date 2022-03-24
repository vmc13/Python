d=float(input('Insira o valor do depósito inicial: '))
t=float(input('Insira a taxa de juros ao ano: '))
obj=d*2
tj=t/100
anos=0
while d<obj:
    juro=d*tj
    d+=juro
    anos+=1

print(f'Em {anos} anos, o valor acumulado será o dobro do depósito inicial.')
