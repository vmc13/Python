print('Conversão de minutos em horas e minutos')
print('')
minutos_t=int(input('Digite uma quantidade de minutos: '))
h = minutos_t//60
m= minutos_t % 60
print(f'{minutos_t} minuto(s) equivale à {h} hora(s) e {m} minuto(s)')
