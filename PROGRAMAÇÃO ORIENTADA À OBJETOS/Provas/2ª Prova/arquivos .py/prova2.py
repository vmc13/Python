totalseg = []

#SUPERCLASSE
class Seguro:
    def __init__(self, num_apolice, proprietario):
        self._num_apolice = num_apolice
        if type(proprietario) == Cliente:
            self._proprietario = proprietario
        else:
            print('Poprietário não confere!')

    def __str__(self):
        return f'\nNúmero da apolice: {self._num_apolice} \nProprietário: \n{self._proprietario}\n'

    #MÉTODOS
    def calculaValor(self):
        pass
    
    def calculaPremio(self):
        pass

#COMPOSIÇÃO
class Cliente:
    def __init__(self, cpf, nome, idade):
        self.__cpf = cpf
        self.__nome = nome
        if idade < 0 or idade > 150:
            print('Idade inválida!')
        else:
            self.__idade = idade
    
    def __str__(self):
        return f'Nome: {self.__nome} \nCPF: {self.__cpf} \nIdade: {self.__idade}'

    @property
    def idade(self):
        return self.__idade

    @property
    def nome(self):
        return self.nome



#SUBCLASSES
class SeguroVida(Seguro):
    def __init__(self, num_apolice, proprietario, nome_beneficiario):
        super().__init__(num_apolice, proprietario)
        self.__num_apolice = num_apolice
        self.__proprietario = proprietario
        self.__nome_beneficiario = nome_beneficiario

    def __str__(self):
        return f'SEGURO DE VIDA\n=-=-=-=-=--=-=-=-=--=-={super().__str__()}Nome do benefciário: {self.__nome_beneficiario} \n'

    #MÉTODOS
    def calculaValor(self):
        if str(self.__proprietario.idade) <='30':
            valor = 800
        if str(self.__proprietario.idade) >='31' and str(self.__proprietario.idade) <='50':
            valor = 1300
        if str(self.__proprietario.idade) > '50':
            valor = 1600

        return valor

    def calculaPremio(self):
        if str(self.__proprietario.idade) <='30':
            premio = 50000
        if str(self.__proprietario.idade) >='31' and str(self.__proprietario.idade) <='50':
            premio = 30000
        if str(self.__proprietario.idade) > '50':
            premio = 20000
        print (f'Seu prêmio é de R${premio}')



class SeguroAutomovel(Seguro):
    def __init__(self, num_apolice, proprietario, numero_licenca, nome_modelo, ano, valor_automovel):
        super().__init__(num_apolice, proprietario)
        self.__num_apolice = num_apolice
        self.__proprietario = proprietario
        self.__numero_licenca = numero_licenca
        self.__nome_modelo = nome_modelo
        self.__ano = ano
        self.__valor_automovel = valor_automovel

    def __str__(self):
        return f'SEGURO DE AUTOMÓVEL\n=-=-=-=-=--=-=-=-=--=-={super().__str__()}No. Licença: {self.__numero_licenca} \nModelo: {self.__nome_modelo} \nAno: {self.__ano} \nValor: R${self.__valor_automovel}\n'

    #MÉTODOS
    def calculaValor(self):
        #3% do aut
        valor = self.__valor_automovel * 0.03

        return valor

    def calculaPremio(self):
        #80% do aut
        premio = self.__valor_automovel * 0.8
        print (f'Seu prêmio é de R${premio:.0f}')

    def franquia(self):
        #40% do seg
        franq = self.calculaValor() * 0.4
        print(f'O valor da sua franquia é: R${franq:.0f}')

#MAIN
class ControleDeSeguros:
    def __init__(self):
        self.seguros = []

    def cadastrar(self, seguro):
        if isinstance(seguro, Seguro):
            self.seguros.append(seguro)
            print('Seguro cadastrado com sucesso!')
        else:
            print('Objeto inváido!')


    def relatorio(self):
        auto = []
        vida = []
        for i in self.seguros:
            print(i)
            if type(i) == SeguroAutomovel:
                auto.append(i)
            if type(i) == SeguroVida:
                vida.append(i)

        print(f'Total de seguros de automóvel: {len(auto)}')
        print(f'Total de seguros de vida: {len(vida)}')
        
        soma = 0
        for i in totalseg:
            soma += i
        
        print(f'O Valor total dos seguros é de: R${soma:.0f}')
            






