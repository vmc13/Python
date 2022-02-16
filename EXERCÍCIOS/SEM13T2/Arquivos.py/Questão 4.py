height=[]
name=[]
soma=0
for c in range(1, 13):
    nome=input(f'Insira o {c}º nome: ')
    altura=float(input(f'Insira a {c}º altura: '))
    name.append(nome)
    height.append(altura)
    media=sum(height)/len(height)
    
maior_altura=height.index(max(height))
print(f'\nJOGADOR MAIS ALTO DO TIME\n{name[maior_altura]}\n{height[maior_altura]:.2f}')
print(f'\nALTURA MÉDIA DO TIME\n{media:.2f}')

def acima_media(nome,altura,media):
    altura_acima=[]
    nomes_acima=[]   
    alt=len(height)
    i=0
    while i<alt:
        if height[i]>media:
            nomes_acima.append(name[i])
            altura_acima.append(height[i])
        i+=1
    return nomes_acima, altura_acima

jogadores_acima_nome, jogadores_acima_alt=acima_media(nome, altura, media)
print('\nJOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')

alt=len(jogadores_acima_nome)
i=0
while i<alt:
    print(jogadores_acima_nome[i])
    print(f'{jogadores_acima_alt[i]:.2f}')
    i+=1
