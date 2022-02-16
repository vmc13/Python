turma=[]
aluno={}

while True:
    aluno.clear()
    aluno['matrícula']=input('Matrícula: ').strip()
    if aluno['matrícula']=='':
        break
    else:
        aluno['nome']=input('Nome: ').strip()
        aluno['nota1']=float(input('Nota 1: ').strip())
        aluno['nota2']=float(input('Nota 2: ').strip())
        aluno['média']=(aluno['nota1']+aluno['nota2'])/2
        turma.append(aluno.copy())



while True:
    aluno['matrícula']=input('Insira a matrícula: ').strip()
    if aluno['matrícula']=='':
        break
    else:
        while True:
            for a in turma:
                if aluno['matrícula']==a['matrícula']:
                    print(f'{a["nome"]}: {a["média"]:.1f}')
                    break
            break
