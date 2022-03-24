def inverter(numero):
    a=numero%10
    numero=numero//10
    b=numero%10
    numero=numero//10
    c=numero%10
    numero=numero//10
    d=numero%10
    numero=numero//10
    numero_invert=(a*1000)+(b*100)+(c*10)+d
    return numero_invert


n=int(input('Digite um número entre 1000 e 9999: '))
print(f'O número {n} invertido será: {inverter(n)}')
