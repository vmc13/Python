a=[]
e=[]
i=[]
o=[]
u=[]
cont=0

frase=input('Escreva uma frase: ').lower()

while cont<1:
    for v in frase:
        if v in 'aáâãà':
            a.append(i)
        elif v in 'eéèê':
            e.append(i)
        elif v in 'iíìî':
            i.append(i)
        elif v in 'oõòóô':
            o.append(i)
        elif v in 'uúùû':
            u.append(i)
    cont+=1

    print('Quantidade de cada vogal no texto: ')
    print(f'A: {len(a)}')
    print(f'E: {len(e)}')
    print(f'I: {len(i)}')
    print(f'O: {len(o)}')
    print(f'U: {len(u)}')
