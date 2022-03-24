def area_quadrado(lado):
    return lado*lado


def perimetro_quadrado(lado):
    return lado*4


valor_lado=float(input('Defina um valor para o lado do quadrado: '))
x=area_quadrado(valor_lado)
y=perimetro_quadrado(valor_lado)
print(f'A área do quadrado será: {x:10.4f}')
print(f'O perímetro do quadrado será: {y:10.4f}')
