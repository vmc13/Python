valor=int(input('Digite um valor inteiro entre 10 e 99: '))
q=0

u=valor//1%10
d=valor//10%10

if u%2!=0:
    q=q+1
if d%2!=0:
    q=q+1
else:
    print('Nenhum dígito é ímpar.')

if q==1:
    print('Apenas um dígito é ímpar.')

if q==2:
    print('Os dois dígitos são ímpares.')

