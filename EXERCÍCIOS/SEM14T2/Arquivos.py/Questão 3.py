pessoa={}
grupo=[]

menoresgp=[]
maioresgp=[]

for c in range(20):
    pessoa.clear()
    pessoa['nome']=input('Nome: ').strip()
    pessoa['idade']=int(input('Idade: '))
    pessoa['cpf']=input('CPF: ').strip()
    grupo.append(pessoa.copy())

for p in grupo:
    if p['idade']>=18:
        maioresgp.append(p.copy())
    if p['idade']<18:
        menoresgp.append(p.copy())

print('========== MAIORES DE 18 ANOS ==========')

for p in maioresgp:
    print(f"{p['nome']};{p['idade']};{p['cpf']}")

print('========== MENORES DE 18 ANOS ==========')

for p in menoresgp:
    print(f"{p['nome']};{p['idade']};{p['cpf']}")
