nome=input('Digite seu nome: ').strip()

def estadocivil(x):
    caract_nome=len(nome)
    if x==1:
        nome_conj=input('Digite o nome do seu cônjuge: ').strip()
        caract_conj=len(nome_conj)
        totalc=caract_conj+caract_nome
        return print(f'Seus nomes tem {totalc} caracteres')
    elif x==2:
        return print(f'Seu nome tem {caract_nome} caracteres')


es_civ=int(input('Digite 1 para casado ou 2 para solteiro: '))
x=estadocivil(es_civ)
