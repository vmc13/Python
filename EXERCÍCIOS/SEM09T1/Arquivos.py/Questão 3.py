soma=0
for c in range(1,101):
    num=int(input(f'Digite o {c}º número: '))
    soma=soma+num
    media=soma/100
print(f'A média desses números é: {media:.2f}')
