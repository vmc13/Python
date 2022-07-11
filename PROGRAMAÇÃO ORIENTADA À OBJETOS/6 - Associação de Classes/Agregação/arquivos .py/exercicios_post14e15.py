class Banco:
    def __init__(self, nome):
        self.__nome = nome 
        self.__contas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def contas(self):
        return self.__contas

    #MÉTODOS
    def adicionar(self, conta):
        if type(conta) == Conta:
            self.__contas.append(conta)
            print(f'Conta número {conta.numero} adicionada ao banco {self.__nome}!')
        else:
            print('Impossível adicionar conta!')

    def remover(self, conta):
        if type(conta) == Conta:
            if conta.saldo == 0:
                self.__contas.remove(conta)
                print(f'Conta número {conta.numero} removida do banco {self.__nome}!')
            else:
                print('Impossível remover conta! Necessário que o saldo esteja zerado.')
        else:
            print('Impossível remover conta!')

    def valorTotal(self):
            soma = 0
            for i in self.contas:
                soma += i.saldo
            return f'O valor total do saldo das contas é de: R${soma}'

    def __str__(self):
        #nome do banco e valor total depositado
        return (f'{self.__nome}: \n{self.valorTotal()} \nTotal de contas: {len(self.contas)}')


class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.__numero = numero 
        if type(titular) == Cliente:
            self.__titular = titular #instância da classe CLiente
        self.__saldo = saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def titular(self):
        return self.__titular

    #MÉTODOS
    def depositar(self, valor):
        if valor>0:
            self.__saldo += valor
            print(f'R${valor} adicionados! Saldo atual da conta: R${self.__saldo}')
        else:
            print('Impossível depositar valores negativos!')

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f'R${valor} sacado! Saldo atual da conta: R${self.__saldo}')
        else:
            print(f'Impossível reaizar operação! Saldo Insuficiente.')

    def __str__(self):
        return f'Conta {self.__numero}: \nTirular: {self.__titular} \nSaldo: R${self.__saldo}'


class Cliente:
    def __init__(self, cpf, nome):
        self.__cpf = cpf 
        self.__nome = nome 

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    #MÉTODOS
    def __str__(self):
        return f'CPF: {self.__cpf} Nome: {self.__nome}'
    

