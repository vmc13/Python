class Carro:
    def __init__(self, nome, ano, cor, vel_m, vel_a, estado):
        self.nome = nome
        self.ano = ano
        self.cor = cor
        self.vel_m = vel_m
        self.vel_a = vel_a
        self.estado = estado

    def Ligar(self):
        print(f'{self.nome} está ligado.')

    def Desligar(self):
        print(f'{self.nome} está desligado.')

    def Parar(self):
        print(f'{self.nome} está parado.')

    def Acelerar(self, vel_a):
        if vel_a == 40:
            print(f'{self.nome} está a 40km/h')
        if vel_a == 200:
            print(f'{self.nome} está a 200km/h')
        if vel_a == 320:
            print(f'{self.nome} está a 320km/h')
        if vel_a == 100:
            print(f'{self.nome} está a 100km/h.')

carroBarato= Carro('Fusca', 1965, 'preto', 80, 20, 'ligado')
carroCaro= Carro('Ferrari_sr2000', 2014, 'vermelho', 300, 0, 'desligado')

carroBarato.Acelerar(40)
carroCaro.Acelerar(200)
carroBarato.Desligar()
carroCaro.Ligar()
carroCaro.Acelerar(320)
carroCaro.Parar()
carroCaro.Desligar()
carroBarato.Ligar()
carroBarato.Acelerar(100)
carroBarato.Desligar()