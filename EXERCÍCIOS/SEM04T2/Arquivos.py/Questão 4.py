def minutos_horas(total_min):
    horas=total_min//60
    minutos=total_min%60
    return f'{horas}:{minutos}'


minutos=int(input('Defina uma quantidade de minutos: '))
horas=minutos_horas(minutos)
print(f'{minutos} minutos convertido para horas e minutos será: {horas}')
