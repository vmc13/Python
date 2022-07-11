class Cartao:
    def __init__(self, numero, titular, validade, cod_seguranca, senha=None, fatura_a_pagar=0, status='bloqueado', limite_de_compras = 100):
        self.__numero = numero
        self.__titular = titular
        self.__validade = validade
        self.__cod_seguranca = cod_seguranca
        self.__senha = senha
        self.__fatura_a_pagar = fatura_a_pagar
        self.__status = status
        self.__limite_de_compras = limite_de_compras
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def senha(self):
        return self.__senha
    
    @property
    def fatura_a_pagar(self):
        return self.__fatura_a_pagar
    
    @property
    def status(self):
        return self.__status
    
    @property
    def limite_de_compras(self):
        return self.__limite_de_compras
    
    def desbloquear(self):
        self.__status = 'liberado'
        print(f'Cartão {self.status}')
        
    def bloquear(self):
        self.__status = 'bloqueado'
        print(f'Cartão {self.status}')
        
    def mudar_senha(self, cod_seguranca):
        if cod_seguranca == self.__cod_seguranca:
            nova_senha = input("Insira a nova senha: ")
            self.__senha = nova_senha
            print(f'Sua nova senha é: {self.senha}')
        else:
            print('Código de seguranca invalido!')
            self.__senha = self.__senha
            
    def comprar(self, senha, valor):
        if valor < self.__limite_de_compras and self.__validade == '06/2026' and senha == self.__senha  and self.__status == 'liberado':
            print('Compra aprovada!')
            self.__limite_de_compras -= valor
            print(f'Seu limite de compras atualizado! R${self.limite_de_compras} Disponiveis.')
            self.__fatura_a_pagar += valor
            print(f'Sua fatura atual é de: R${self.fatura_a_pagar}')
        else:
            print('Compra negada!')
            
    def pagar_fatura(self, valor):
        self.__fatura_a_pagar -= valor
        print(f'Sua fatura paga com sucesso! Valor da fatura: R${self.fatura_a_pagar}.')
        self.__limite_de_compras = self.__limite_de_compras
        print(f'Seu limite de compras atualizado! R${self.limite_de_compras} Disponiveis.')


    def __str__(self):
        return (f'Número do cartao: {self.numero}\n Nome do titular: {self.titular}\n Valor da fatura: R${self.fatura_a_pagar:.2f}')


#número, titular, validade, cod_segurança, senha, fatura, status, limite
itau = Cartao(1, 'Júlio', '06/2026', 48, 'vcx64', 50, 'bloqueado')
caixa = Cartao(2, 'Marina', '06/2026', 15, '34baj*', 0, 'liberado', 2500)
bradesco = Cartao(3, 'Raul', '06/2026', 78, 'qed5!', 130, 'bloqueado', 2200)
hsbc = Cartao(4, 'Pablo', '06/2026', 35, 'fT40@', 1200, 'liberado', 3000)

itau.desbloquear()

caixa.bloquear()

bradesco.mudar_senha(78)

hsbc.pagar_fatura(1200)

hsbc.comprar('fT40@', 1550)

print(itau, caixa, bradesco, hsbc)