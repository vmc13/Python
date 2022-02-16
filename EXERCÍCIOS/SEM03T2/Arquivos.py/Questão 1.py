print('Cálculo da; circunferência, área do círculo, área da esfera e volume da esfera')
print(' ')
pi=3.141592
raio=float(input('Digite um valor para o raio da esfera: '))
print(' ')
circunferencia=2*pi*raio
a_circulo=pi*raio*raio
a_esfera=4*pi*raio**2
vol_esfera=4/3*pi*raio**3
print("O resultado do cálculo da circunferência da esfera será de: %.6f" % (circunferencia))
print("O resultado do cálculo da área do círculo será de:%.6f" % (a_circulo))
print("O resultado do cálculo da área da esfera será de:%.6f" % (a_esfera))
print("O resultado do cálculo do volume da esfera será de:%.6f" % (vol_esfera))
