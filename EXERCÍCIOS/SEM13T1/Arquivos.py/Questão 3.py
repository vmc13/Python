invert=[]
n=int(input('Insira um número: '))
for i in range(1, n+1):
      numero=float(input(f'Insira o {i}º valor: '))
      invert.insert(0, numero)
print(invert)

listanota=[]
qnt=0
soma=0
for i in range(1, n+1):
    valor=float(input(f'Insira a {i}ª nota: '))
    soma+=valor
    qnt+=1
    listanota.append(valor)
print(listanota)
if n==0:
      print('SEM NOTAS')
else:
      media=soma/qnt
      print(f'Sua média é: {media:.1f}')

listavogal=[]
listaconso=[]
qnt=0
for i in range(1, n+1):
    vogal=input('Insira a {i}ª letra: ')[0]
    if vogal in 'bcçdfghjklmnpqrstvwxyzBCÇDFGHJKLMNPQRSTVWXYZ':
          listaconso.append(vogal)
    if vogal in 'aeiouAEIOU':
          qnt+=1
print(f'{qnt} vogais foram inseridas.')
print(f'As consoantes inseridas foram: {listaconso}')
