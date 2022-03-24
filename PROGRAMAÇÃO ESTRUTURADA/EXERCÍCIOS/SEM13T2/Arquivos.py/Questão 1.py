L=[]
n=0
maior=0
menor=0
while True:
    val=int(input('Insira um valor: '))
    if val==0:
        break
    n+=1
    L.append(val)
    x=L[::-1]

print(f'Comprimento: {L}')
print(f'Quantidade de valores inserios: {n}')
print(f'Lista invertida: {x}')
    
def menor(lista):
    menor=lista[0]
    for i in lista:
        if i<menor:
            menor=i
    return menor

def maior(lista):
    maior=lista[0]
    for i in lista:
        if i>maior:
            maior=i
    return maior

def somar_elementos(lista):
    soma=0
    for i in lista:
        soma+=i
    return soma

mar=maior(L)
men=menor(L)
som=somar_elementos(L)
print(f'Menor valor: {men}')
print(f'Maior valor: {mar}')
print(f'Soma dos valores: {som}')
        



