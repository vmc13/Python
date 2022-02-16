livro={}
codigo=100

while True:
    livro['Título'] = input('Título: ').strip()
    if livro['Título'] == '':
        break
    else:
        livro['ISBN'] = input('ISBN: ').strip()
        livro['Autor'] = input('Autor: ').strip()
        livro['Preço'] = float(input('Preço: ').strip())
        codigo+=1
    print(f'Código: {codigo}')
    print(f'Título: {livro["Título"]}')
    print(f'ISBN: {livro["ISBN"]}')
    print(f'Autor: {livro["Autor"]}')
    print(f'Preço: {livro["Preço"]:.2f}')
