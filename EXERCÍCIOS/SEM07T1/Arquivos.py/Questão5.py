def imc(x):
    if 18.5 > x:
        return print('Abaixo do peso')
    if 25 > x:
        return print('Peso normal')
    if 30 > x:
        return print('Sobrepeso')
    if 35 > x:
        return print('Obeso leve')
    if 40 > x:
        return print('Obeso moderado')
    if 40<= x:
        return print('Obeso mórbido')



massa=float(input('Digite sua massa: '))
altura=float(input('Digite sua altura: '))
c_imc=massa/(altura**2)
print(f'Seu IMC é: {c_imc:.0f}')
r_imc=imc(c_imc)
