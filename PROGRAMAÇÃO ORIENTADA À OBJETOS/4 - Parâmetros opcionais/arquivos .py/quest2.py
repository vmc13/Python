
estacoes = {89.5:'Cocais', 91.5:'Mix', 94.1:'Boa', 99.1:'Clube'}

class RadioFM:
    def __init__(self, vol_max, estacoes):
        self.volume_min = 0
        self.volume_max = vol_max
        self.freq_min = 88
        self.freq_max = 108
        self.estacoes = estacoes
        self.volume = None
        self.ligado = False
        self.estacao_atual = None
        self.frequencia_atual = None
        self.antena_habilitada = False

    def ligar(self, ligado, antena, radio='Rádio'):
        if ligado == True:
            self.ligado = True
            self.volume = self.volume_min
            print(f'{radio} ligado no volume {self.volume}')
            if antena == True:
                for valor in self.estacoes.keys():
                    print(f'{radio} na frequência {valor}')
                    break
                for valor in self.estacoes.values():
                    print(f'{radio} na frequência {valor}')
                    break

    def desligar(self, radio='Rádio'):
        self.ligado == False
        self.volume == None
        self.frequencia_atual == None
        self.estacao_atual == None
        print(f'{radio} desligado')

    def aumentar_volume(self, aumentar=1):
        if self.ligado == True:
            if self.volume < 100:
                self.volume += aumentar
                print(f'Volume aumentado para {self.volume}')
            else:
                print(f'Você não pode aumentar o volume à cima de 100!')
        else:
            print('Rádio não está ligado!')

    def diminuir_volume(self, diminuir=1):
        if self.ligado == True:
            if self.volume > 0:
                self.volume -= diminuir
                print(f'Volume diminuido para {self.volume}')
            else:
                print(f'Você não pode diminuir volume à baixo de 0!')
        else:
            print('Rádio não está ligado!')

    
    def mudar_frequencia(self, freq=0):
        if self.ligado == True:
            if freq in self.estacoes.keys():
                print(f'Rádio na frequência {freq}, estação {estacoes[freq]}')
            elif freq == 0:
                print(f'Rádio ligado na frequência 85.5, estação Cocais')
            else:
                print('Estação inexistente!')
        else:
            print('Rádio não está ligado!')


#print(estacoes[91.5])
#3 objetos
radio1 = RadioFM(100, estacoes)
radio2 = RadioFM(100, estacoes)
radio3 = RadioFM(100, estacoes)

radio1.ligar(True, True, 'Rádio 1')
radio1.aumentar_volume(15)
radio1.aumentar_volume()
radio1.diminuir_volume(10)
radio1.diminuir_volume()
radio1.mudar_frequencia()
radio1.mudar_frequencia(99.1)
radio1.desligar('Rádio 1')
print('\n')
radio2.ligar(True, True, 'Rádio 2')
radio2.aumentar_volume(15)
radio2.aumentar_volume()
radio2.diminuir_volume(10)
radio2.diminuir_volume()
radio2.mudar_frequencia()
radio2.mudar_frequencia(99.1)
radio2.desligar('Rádio 2')
print('\n')
radio3.ligar(True, True, 'Rádio 3')
radio3.aumentar_volume(15)
radio3.aumentar_volume()
radio3.diminuir_volume(10)
radio3.diminuir_volume()
radio3.mudar_frequencia()
radio3.mudar_frequencia(99.1)
radio3.desligar('Rádio 3')
print('\n')


