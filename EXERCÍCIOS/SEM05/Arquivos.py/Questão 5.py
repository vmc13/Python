def avista(x):
    desc=x*0.09
    av=x-desc
    return av


def cinco(x):
    cn=x/5
    return cn


def dez(x):
    dz=(x/10)
    desc=dz*0.17
    dez_desc=dz+desc
    return dez_desc


valor=float(input('Defina o valor da compra: '))
vst=avista(valor)
cnc=cinco(valor)
dez=dez(valor)
print(f'Pagando à vista, com desconto de 9%, o valor final será de: R${vst:.2f}')
print(f'Pagando em 5 vezes, o valor da prestação será de: R${cnc:.2f}')
print(f'Pagando em 10 vezes, com 17% de juros, o valor da prestação será de: R${dez:.2f}')
