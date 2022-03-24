def sexo(n):
    if n == 1:
        return 'Ilmo Sr.'
    elif n ==2:
        return 'Ilma Sra.'


nome=input('Digite seu nome: ')
inf_sex=int(input('Defina seu sexo; Digite 1 para masculino ou 2 para feminino: '))
result=sexo(inf_sex)
print(f'{result} {nome}')
