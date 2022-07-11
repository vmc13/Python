#CLASSE 1
class Gato:
    def __init__(self, peso, idade, raça='indefinido', nome='indefinido'):
        self.__peso = peso
        self.__idade = idade
        self.__raça = raça
        self.__nome = nome

    def __str__(self):
        return f'Nome do gato: {self.__nome} \nRaça: {self.__raça} \nIdade: {self.__idade} \nPeso: {self.__peso}'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def raça(self):
        return self.__raça

    @property
    def idade(self):
        return self.__idade

    @property
    def peso(self):
        return self.__peso

    #MÉTODOS
    def engordar(self, peso):
        self.__peso += peso

    def emagrecer(self, peso):
        self.__peso -= peso

    def envelhecer(self):
        self.idade += 1


#CLASSE 2
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__pet = None

    def __str__(self):
        if self.__pet == None:
            nome_do_gato = 'Não tem gato'
        else:
            nome_do_gato = self.__pet.nome
        return f'Noome da pessoa: {self.__nome} \nNome do gato: {nome_do_gato}'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        a = self.__nome.split(' ')
        b = nome.split(' ')
        if a[0] == b [0]:
            self.__nome = nome
        else:
            print('Primeiro nome não pode ser alterado!')

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        print('Sem permissão!')

    @property
    def pet(self):
        return self.__pet

    #MÉTODOS
    def adotarGato(self, gato):
        if type(gato) == Gato:
            self.__pet = gato
    
    def excluirGato(self):
        self.__pet = None

joao = Pessoa('João', 30)
maria = Pessoa('Maria', 20)

mimi = Gato(1, 1, nome='mimi')
print(mimi)
print(joao)
joao.adotarGato(mimi)
print(joao)