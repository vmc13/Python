agenda=[]
pessoa={}

tamanho=int(input(''))

for c in range(tamanho):
    pessoa.clear()
    pessoa['nome']=input('Nome: ').strip()
    pessoa['cidade']=input('Cidade: ').strip()
    pessoa['UF']=input('Estado: ').strip().upper()
    pessoa['telefone']=input('Tefelone: ')
    agenda.append(pessoa.copy())

for p in agenda:
    print(f"{p['nome']:<25}", end='')
    print(f"{p['cidade']+'('+p['UF']+')':<30}", end='')
    print(f"{p['telefone']}")

