from exercicios_post17e18 import *;

#CONTA CORRENTE
contaC1 = ContaCorrente('0136', 6450.62)
contaC2 = ContaCorrente('0187', 10583.14)

#CONTA POUPANÇA
contaP1 = ContaPoupança('0241', 5410.70, 8.5)
contaP2 = ContaPoupança('0241', 15690.00, 12)

#CONTRA IMPOSTO
contraIp1 = ContraImposto('8163', 3410.25, 5)
contraIp2 = ContraImposto('8694', 5987.71, 7.5)

#CC
print(contaC1)
print(contaC2)

#CP
#print(contaP1)
#print(contaP2)

#CI
#print(contraIp1)
#print(contraIp2)

contaC1.creditar(1500)
contaC1.creditar(0)
contaC1.debitar(500)
contaC1.debitar(8000)
contaC1.saldo()
contaC1.transferir(300, contaC2)

contaC2.creditar(400)
contaC2.creditar(0)
contaC2.debitar(2500)
contaC2.debitar(20000)
contaC2.saldo()
contaC2.transferir(900, contaC1)

contaP1.render_juros()
contaP2.render_juros()

contraIp1.calcula_Imposto()
contraIp2.calcula_Imposto()
