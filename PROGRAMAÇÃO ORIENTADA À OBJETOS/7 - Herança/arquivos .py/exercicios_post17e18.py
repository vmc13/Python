class ContaCorrente:
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo
    
    def __str__(self):
        return f'Número da conta: {self.__numero} \nSaldo da conta: {self.__saldo}\n'
    
    #DECORADORES
    @property
    def numero(self):
        return self.__numero
    
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    #MÉTODOS
    def creditar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'R${valor} depositados! Novo saldo: R${self.__saldo}\n')
        else:
            print(f'Impossível creditar valores negativos!\n')

    def debitar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f'R${valor} sacados! Novo saldo: R${self.__saldo}\n')
        else:
            print(f'Saldo insuficiente!\n')

    def saldo(self):
        print(f'Seu saldo é de: R${self.__saldo}')

    def transferir(self, valor, conta): #conta=obj
        if type(conta) == ContaCorrente or type(conta) == ContaPoupança:
            if valor <= self.__saldo:
                self.__saldo -= valor
                conta.__saldo += valor
                print(f'R${valor} transferidos!\n')
            else:
                print('Saldo insuficiente!\n')
        else:
            print('Informe uma conta válida!\n')

#########################################
class ContaPoupança(ContaCorrente):
    def __init__(self, numero, saldo, taxa_juros):
        super().__init__(numero, saldo)
        self.__numero = numero
        self.__saldo = saldo
        self.__taxa_juros = taxa_juros
    
    def __str__(self):
        return f'Taxa de juros: {self.__taxa_juros}\n'
    
    @property
    def taxa_juros(self):
        return self.__taxa_juros

    #MÉTODO
    def render_juros(self):
        juros = self.__taxa_juros/100
        rendimento = juros*(self.__saldo)
        (self.__saldo) += rendimento
        print(f'Juros de R${rendimento:.2f} aplicados. \nSaldo com juros: R${self.__saldo:.2f}\n')
    
########################################
class ContraImposto(ContaCorrente):
    def __init__(self, numero, saldo, percentual_imposto):
        super().__init__(numero, saldo)
        self.__numero = numero
        self.__saldo = saldo
        self.__percentual_imposto = percentual_imposto
    
    def __str__(self):
        return f'Percentual do imposto: {self.__percentual_imposto}\n'

    @property
    def percentual_imposto(self):
        return self.__percentual_imposto
    
    #MÉTODO
    def calcula_Imposto(self):
        imposto = self.__saldo*self.__percentual_imposto
        self.__saldo -= imposto
        print(f'Imposto de R${imposto} \n')
    


