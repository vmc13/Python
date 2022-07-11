class BombaCombustivel:
    def __init__(self, numero, valorLitro, capacidade, quantidadeCombustivel, valorFaturado=0, quantidadeVendida=0, tipoCombustivel='gasolina comum'):
        self.__numero = numero
        self.__valorLitro = valorLitro
        self.__capacidade = capacidade
        self.__quantidadeCombustivel = quantidadeCombustivel
        self.__valorFaturado = valorFaturado
        self.__quantidadeVendida = quantidadeVendida
        self.__tipoCombustivel = tipoCombustivel
        if self.__quantidadeCombustivel > self.__capacidade:
            self.__quantidadeCombustivel = self.__capacidade

    @property
    def numero(self):
        return self.__numero

    @property
    def valorLitro(self):
        return self.__valorLitro
    
    @valorLitro.setter #set valor litro
    def valorLitro(self, valor):
        self.__valorLitro = valor

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def quantidadeCombustivel(self):
        return self.__quantidadeCombustivel

    @quantidadeCombustivel.setter #set quantidade de combustível
    def quantidadeCombustivel(self, quantidadeCombustivel):
        self.__quantidadeCombustivel = quantidadeCombustivel

    @property
    def valorFaturado(self):
        return self.__valorFaturado

    @property
    def quantidadeVendida(self):
        return self.__quantidadeVendida

    @property
    def tipoCombustivel(self):
        return self.__tipoCombustivel

    @tipoCombustivel.setter #set tipo de combustível
    def tipoCombustivel(self, tipoCombustivel):
        self.__tipoCombustivel = tipoCombustivel

    #MÉTODOS
    def abastecerBomba(self, quantidadeComb):
        if quantidadeComb <= self.__capacidade:
            self.__quantidadeCombustivel = quantidadeComb
            print(f'\nBomba {self.__numero} abastecida com {quantidadeComb} litros')
            print(f'Quantidade atual de combustível: {self.quantidadeCombustivel}L')
        if quantidadeComb > self.__capacidade:
            self.__quantidadeCombustivel = self.__capacidade
            print(f'\nBomba {self.__numero} abastecida com {self.__quantidadeCombustivel}')
            print(f'Quantidade atual de combustível: {self.quantidadeCombustivel}L')


    def abastecerVeiculoPorValor(self, valor):
        quantidadeL = valor / self.__valorLitro
        if self.__quantidadeCombustivel > quantidadeL:
            print(f'Veículo abastecido com {quantidadeL:.0f} litros.')
            self.__quantidadeCombustivel -= quantidadeL
            self.__valorFaturado += valor
            print(f'Quantidade de combustível da bomba atualizado para {self.quantidadeCombustivel:.0f} litros.')
            print(f'Valor total faturado: R${self.valorFaturado:.2f}')
        else: 
            print('\nImpossível abastecer! Quantidade de combustível indisponível!')
        

    def abastecerVeiculoPorLitro(self, quant):
        valorL = quant * self.__valorLitro
        if self.__quantidadeCombustivel > quant:
            print(f'\nVeículo abastecido com R${valorL:.2f} de combustível.')
            self.__quantidadeCombustivel -= quant
            self.__valorFaturado += valorL
            print(f'Quantidade de combustível da bomba atualizado para {self.quantidadeCombustivel:.0f} litros.')
            print(f'Valor total faturado: R${self.valorFaturado:.2f}')
        else: 
            print('\nImpossível abastecer! Quantidade de combustível indisponível!')
        

    def __str__(self):
        return f'\nNúmero da bomba: {self.numero} \nValor do litro: {self.valorLitro} \nCapacidade: {self.capacidade} \nQuantidade de combustível atual: {self.quantidadeCombustivel} \nValor total faturado: {self.valorFaturado} \nQuantidade vendida: {self.quantidadeVendida} \nTipo de combustível: {self.tipoCombustivel}\n'

#OBJETOS
bomba1 = BombaCombustivel(1, 5, 5000, 850, 20750, 4150, 'gasolina comum')
bomba2 = BombaCombustivel(2, 6, 3500, 2750, 4500, 750, 'gasolina aditivada')
bomba3 = BombaCombustivel(3, 6.5 , 4000, 3500, 3250, 500, 'etanol')
bomba4 = BombaCombustivel(4, 8, 3000, 2150, 6800, 850, 'diesel')

#CHAMADAS
#bomba1
print(f'\nBOMBA 1')
bomba1.abastecerVeiculoPorValor(60)
bomba1.abastecerVeiculoPorLitro(10)
bomba1.abastecerBomba(2000)
#bomba2
print(f'\nBOMBA 2')
bomba2.abastecerVeiculoPorValor(30)
bomba2.abastecerVeiculoPorLitro(20)
bomba2.abastecerBomba(1000)
#bomba3
print(f'\nBOMBA 3')
bomba3.abastecerVeiculoPorValor(50)
bomba3.abastecerVeiculoPorLitro(25)
bomba3.abastecerBomba(500)
#bomba4
print(f'\nBOMBA 4')
bomba4.abastecerVeiculoPorValor(35)
bomba4.abastecerVeiculoPorLitro(15)
bomba4.abastecerBomba(2000)


print(bomba1)
print(bomba2)
print(bomba3)
print(bomba4)

