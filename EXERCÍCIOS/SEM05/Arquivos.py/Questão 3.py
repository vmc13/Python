def duracao_evento(tempo):
    horas=tempo//3600
    minutos=(tempo%3600)//60
    segundos=(tempo%3600)%60
    return f'{horas:.0f}:{minutos:.0f}:{segundos:.0f}'

horario=int(input('Defina o tempo de duração do evento: '))
t_hms=duracao_evento(horario)
print(f'O tempo do evento será de: {t_hms}')
