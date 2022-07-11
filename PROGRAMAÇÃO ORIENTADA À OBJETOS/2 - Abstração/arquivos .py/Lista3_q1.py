class Relogio_Digital_Simples:
    def __init__(self, marca, cor_pulseira, peso, tipo_pulseira, data, hora):    
        self.marca = marca
        self.cor_pulseira = cor_pulseira
        self.peso = peso
        self.tipo_pulseira = tipo_pulseira
        self.data = data
        self.hora = hora

    def mudar_tipo_pulseira(self, tipo):
        print(f'\nMaterial da pulseira do relógio {self.marca}: {self.tipo_pulseira}')
        print(f'Material da pulseira alterado para: {tipo}')

    def mudar_cor_pulseira(self, cor):
        print(f'\nCor da pulseira do relógio {self.marca}: {self.cor_pulseira}')
        print(f'Cor da pulseira alterada para: {cor}')

    def ajustar_horas(self, horas):
        print(f'\nHora atual do relógio {self.marca}: {self.hora}hrs')
        print(f'Hora alterada para: {horas}hrs')

    def ajustar_data(self, data):
        print(f'\nData atual do relógio {self.marca}: dia {self.data}')
        print(f'Data alterada para dia {data}')
    

relogio1 = Relogio_Digital_Simples('Cartier','marrom', 58, 'couro', 15, 10)
relogio2 = Relogio_Digital_Simples('Omega', 'prateado', 70, 'aço', 15, 10)

print(f'Marca relógio 1: {relogio1.marca}')
print(f'Peso relógio 1: {relogio1.peso}')
print(f'\nMarca relógio 2: {relogio2.marca}')
print(f'Peso relógio 2: {relogio2.peso}')

relogio1.mudar_tipo_pulseira('aço inox')
relogio1.mudar_cor_pulseira('dourado')
relogio2.mudar_tipo_pulseira('silicone')
relogio2.mudar_cor_pulseira('preto')
relogio1.ajustar_horas(18)
relogio1.ajustar_data(20)
relogio2.ajustar_horas(21)
relogio2.ajustar_data(24)
