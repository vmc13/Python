from datetime import datetime

class Relogio_Digital_Simples:
    def __init__(self, estado, hora, minuto):    
        self.estado = estado
        self.hora = hora
        self.minuto = minuto

    def alterar_estado(self, estado):
        print(f'Estado alterado para {estado}')

    def alterar_hora(self, horas):
        print(f'Horas alteradas para {horas}hrs')

    def alterar_minutos(self, minutos):
        print(f'Minutos alterados para {minutos}min')
    

relogio = Relogio_Digital_Simples('desligado', 0, 0)
data = datetime.today()

relogio.alterar_estado('ligado')
relogio.alterar_hora(data.hour)
relogio.alterar_minutos(data.minute)