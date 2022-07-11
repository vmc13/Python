class Bicicleta:
    #atributos
    peso = None
    altura = None 
    veloc_atual = 0         #colocar limite máximo e mínimo
    cor = None
    aro = None 
    altura_cela = 0         #colocar limite máximo e mínimo
    calibragem_pneus = 0    #colocar limite máximo e mínimo

    #métodos
    def pedalar(self):
        if self.veloc_atual > 40:
            print(f'Você já está na velocidade máxima.')
        else:
            self.veloc_atual += 1
            print(f'Velocidade atual: {self.veloc_atual}')

    def frear(self):
        if self.veloc_atual == 0:
            print('Bicicleta está parada.')
        else:
            self.veloc_atual -= 1
            print(f'Velocidade atual: {self.veloc_atual}')

    def regular_cela(self, valor): # Apenas se a bike estiver parada
        if self.veloc_atual == 0:
            if valor < 8 and valor > 1:
                self.altura_cela = valor
                print(f'Altura atual da cela: {self.altura_cela}')
            else:
                if valor > 8:
                    print(f'Você não pode aumentar a além de 8cm.')
                if valor < 1:
                    print('Você não pode diminur a cela além de 1cm.')
        else:
            print('Para regular a cela sua bicicleta deve estar parada.')

    def calibrar_pneus(self,valor): # apenas se a bike estiver parada
        if self.veloc_atual == 0:
            if valor > 20 and valor <30:
                self.calibragem_pneus = valor
                print(f'Calibragem atual dos pneus: {self.calibragem_pneus} libras')
            else:
                if valor > 30:
                    print('A calibragem não pode ser maior 30.')
                if valor <20:
                    print('A calibragem não pode ser menor que 20.')
        else:
            print(f'Para calibrar os pneus sua bicicleta deve estar parada.')

bike = Bicicleta()
bike.peso = 10
bike.altura = 100
bike.cor = 'amarela'
bike.aro = 29

print(f'Velocidade máxima: 40Km/h \nVelocidade mínima: 20km/h \nVelocidade atual: {bike.veloc_atual}')
print(f'Altura máxima da cela: 8cm \nAltura mínima: 1cm \nAltura atual: {bike.altura_cela}')
print(f'Calibragem máxima: 30 \nCalibragem mínima: 20 \nCalibragem atual: {bike.calibragem_pneus}')

bike.regular_cela(5)
bike.calibrar_pneus(25)
bike.pedalar()
bike.pedalar()
bike.frear()
bike.frear()
print(f'Cor: {bike.cor}')
print(f'Aro: {bike.aro}')