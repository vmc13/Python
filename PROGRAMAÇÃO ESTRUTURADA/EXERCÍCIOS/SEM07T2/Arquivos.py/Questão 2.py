valor=int(input('Digite um valor entre 100 e 999: '))
q=0

x=valor//1%10
y=valor//10%10
z=valor//100%10

if x%2==0:
    q=q+1
    print(f'Esse número possui {q} par(es)')
elif y%2==0:
    q=q+1
    print(f'Esse número possui {q} par(es)')
elif z%2==0:
    q=q+1
    print(f'Esse número possui {q} par(es)')
else:
    print('0')
