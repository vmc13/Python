def percentual(preco, porcentagem):
    return preco*(porcentagem/100)


pr=float(input('Defina um preço: '))
prc=float(input('Defina uma porcentagem: '))
p_acrescimo=pr+percentual(pr, prc)
p_desconto=pr-percentual(pr, prc)
print(f'O preço R${pr} com acréscimo de {prc}% será: R${p_acrescimo:.2f}')
print(f'O preço R${pr} com desconto de {prc}% será: R${p_desconto:.2f}')
