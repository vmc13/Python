class CLiente: #classe pai
    def __init__(self, pais, dataCadastro):
        self.pais=pais 
        self.dataCadastro = dataCadastro

class PessoaFisica(CLiente): #Herança, subclasse
    def __init__(self, pais, dataCadastro, nome, sobrenome, cpf):
        super().__init__(pais, dataCadastro)
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class PessoaJuridica(CLiente):
    def __init__(self, pais, dataCadastro, razaosocial, nomefantasia, cnpj):
        super().__init__(pais, dataCadastro)
        self.razaosocial = razaosocial
        self.nomefantasia = nomefantasia
        self.cnpj = cnpj

maria = PessoaFisica('Brasil', '12/12/2020', 'Maria', 'Pereira', '8488794856')
google = PessoaJuridica('EUA', '12/01/2005', 'Google', 'Google', '878787878558')
print(maria.pais)
print(google.pais)