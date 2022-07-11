# Dois ou mais objetos de formas diferentes
# Imprimir valores dos atributos do objeto
# Parêmetro obrigatório: peso, cor, altura e aro
# Valores padrões para atributos:
#   vel_atual: 0
#   altura_cela: 0
#   calibragem_pneus: 20

class Bicicleta:
    def __init__(self, peso, cor, altura, aro):
        self.veloc_atual = 0
        self.altura_cela = 0
        self.calibragem_pneus = 20
        self.peso = peso
        self.cor = cor
        self.altura = altura
        self.aro = aro

    #métodos
    def pedalar(self, bike):
        if self.veloc_atual > 40:
            print(f'{bike} já está na velocidade máxima.')
        else:
            self.veloc_atual += 1
            print(f'Velocidade atual: {self.veloc_atual}km/h')

    def frear(self, bike):
        if self.veloc_atual == 0:
            print(f'{bike} está parada.')
        else:
            self.veloc_atual -= 1
            print(f'Velocidade atual da {bike}: {self.veloc_atual}km/h')

    def regular_cela(self, valor, bike): # Apenas se a bike estiver parada
        if self.veloc_atual == 0:
            if valor < 8 and valor > 1:
                self.altura_cela = valor
                print(f'Altura atual da cela da {bike}: {self.altura_cela}cm')
            else:
                if valor > 8:
                    print(f'Você não pode aumentar a além de 8cm.')
                if valor < 1:
                    print('Você não pode diminur a cela além de 1cm.')
        else:
            print('Para regular a cela sua bicicleta deve estar parada.')

    def calibrar_pneus(self, valor, bike): # apenas se a bike estiver parada
        if self.veloc_atual == 0:
            if valor > 20 and valor <30:
                self.calibragem_pneus = valor
                print(f'Calibragem atual dos pneus da {bike}: {self.calibragem_pneus} libras')
            else:
                if valor > 30:
                    print('A calibragem não pode ser maior 30.')
                if valor <20:
                    print('A calibragem não pode ser menor que 20.')
        else:
            print(f'Para calibrar os pneus sua bicicleta deve estar parada.')

# peso, cor, altura, aro
bike1 = Bicicleta(10, 'Cinza', 160, 26)
bike2 = Bicicleta(8, 'Bordô', 154, 26)

print(f'Bicicleta 1:\nPeso: {bike1.peso}kg \nCor: {bike1.cor} \nAltura: {bike1.altura}cm \nAro: {bike1.aro}')
print(f'\nBicicleta 2:\nPeso: {bike2.peso}kg \nCor: {bike2.cor} \nAltura: {bike2.altura}cm \nAro: {bike2.aro}\n')

bike1.regular_cela(5, 'bike 1')
bike1.calibrar_pneus(25, 'bike 1')
bike1.pedalar('bike 1')
bike1.pedalar('bike 1')
bike1.frear('bike 1')
bike1.frear('bike 1')
print('\n')
bike1.regular_cela(5, 'bike 2')
bike1.calibrar_pneus(25, 'bike 2')
bike1.pedalar('bike 2')
bike1.pedalar('bike 2')
bike1.frear('bike 2')
bike1.frear('bike 2')