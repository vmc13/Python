ph=float(input('Informe o preço do carro hoje: '))

poup=10000
rend=0.007
tx=0.004
meses=0

while ph>poup:
    poup=poup+poup*rend
    ph=ph+ph*tx
    meses+=1

print(f'Em {meses} meses, você terá dinheiro para comprar o carro à vista.')
