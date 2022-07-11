#CLASSE 1
class Funcionario:
    def __init__(self, matricula, nome, salario, dependente=None):
        self.__matricula = matricula
        self.__nome = nome
        self.__salario = salario
        if type(dependente) == Dependente:
            self.__dependente = dependente
        else:
            self.__dependente = None

    @property
    def dependente(self):
        return self.__dependente.nome

    def __str__(self):
        if self.__dependente == None:
            nome_dep = 'Não possui dependente.'
            return f'Nome do funcionário: {self.__nome} \nNome do dependente: {nome_dep}'
        else:
            nome_dep = self.__dependente.nome
            grau_parentesco = self.__dependente.parentesco
            return f'Nome do funcionário: {self.__nome} \nNome do dependente: {nome_dep} \nGrau de parentesco: {grau_parentesco}'

    def adiciona_dependente(self, dependente):
        self.__dependente = dependente

    def exclui_dependente(self):
        self.__dependente = None

#CLASSE 2 
class Dependente:
    def __init__(self, nome, data_nasc, parentesco):
        self.__nome = nome
        self.__data_nasc = data_nasc
        self.__parentesco = parentesco

    @property
    def nome(self):
        return self.__nome

    @property
    def parentesco(self):
        return self.__parentesco

#julia = Dependente('Júlia', '12/12/2015', 'Filha')
pedro = Funcionario(1, 'Pedro', 2000, Dependente('Júlia', '12/12/2015', 'Filha'))
print('\n', pedro)

francisco = Funcionario(2 , 'Francisco', 5000)
print('\n', francisco)
francisco.adiciona_dependente(Dependente('Ana', '25/02/2010', 'Filha'))
print('\n', francisco)
