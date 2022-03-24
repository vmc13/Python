a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
c=int(input('Digite o terceiro número: '))
d=int(input('Digite o quarto número: '))
e=int(input('Digite o quinto número: '))

maior=a
if b>a and b>c and b>d and b>e:
    maior=b
if c>a and c>b and c>d and c>e:
    maior=c
if d>a and d>c and d>b and d>e:
    maior=d
if e>a and e>c and e>d and e>d:
    maior=e
print(f' O maior núemro é {maior}')


menor=a
if b<a and b<c and b<d and b<e:
    menor=b
if c<a and c<b and c<d and c<e:
    menor=c
if d<a and d<c and d<b and d<e:
    menor=d
if e<a and e<c and e<d and e<d:
    menor=e
print(f'O menor número é {menor}')
