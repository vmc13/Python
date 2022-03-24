def entrada():
    qnt=30
    nome=[]
    idade=[]
    altura=[]
    cont=0
    while cont < qnt:
        name=input('Nome do aluno: ')
        age=int(input('Idade do aluno: '))
        height=float(input('Altura do aluno: '))
        nome.append(name)
        idade.append(age)
        altura.append(round(height, 2))
        cont+=1
    return nome, idade, altura


def media(lista_h):
    med=sum(lista_h)/len(lista_h)
    return round(med, 2)


def alunos_abaixo(nome, idade, altura, media):
    alunos_abaixo=[]
    alturas_abaixo=[]
    idade_acima=[]
    comp=len(nome)
    i=0
    while i<comp:
        if idade[i] > 13:
            if altura[i] < media:
                alunos_abaixo.append(nome[i])
                alturas_abaixo.append(altura[i])
                idade_acima.append(idade[i])
        i+= 1
    return alunos_abaixo, alturas_abaixo, idade_acima


def main():
    alunos, idade_alunos, altura_alunos=entrada()
    media_altura=media(altura_alunos)
    aluno_menos, altura_menos, idade_mais=alunos_abaixo(alunos, idade_alunos, altura_alunos, media_altura)

    print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
    comp=len(aluno_menos)
    i=0
    while i<comp:
        print(aluno_menos[i])
        i+=1


if __name__ == '__main__':
    main()
