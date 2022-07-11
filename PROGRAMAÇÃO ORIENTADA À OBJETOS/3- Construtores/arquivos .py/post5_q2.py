class Bicicleta:
    def __init__(self, veloc_atual, veloc_maxima, altura_cela, altura_maxima):
        self.veloc_atual = veloc_atual
        self.veloc_maxima = veloc_maxima
        self.altura_cela = altura_cela
        self.altura_maxima = altura_maxima

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


bike = Bicicleta(0, 40, 0, 8)

print(f'Velocidade máxima: 40Km/h \nVelocidade mínima: 20km/h \nVelocidade atual: {bike.veloc_atual}')
print(f'\nAltura máxima da cela: 8cm \nAltura mínima: 1cm \nAltura atual: {bike.altura_cela}\n')

bike.regular_cela(5)
bike.pedalar()
bike.pedalar()
bike.frear()
bike.frear()

