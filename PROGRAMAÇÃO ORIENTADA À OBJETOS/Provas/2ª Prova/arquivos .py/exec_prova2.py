from prova2 import *

#clientes
cliente1 = Cliente(25987413698, 'Paulo', 34)
cliente2 = Cliente(18963548127, 'Carol', 25)
cliente3 = Cliente(20014895321, 'Jonas', 68)

#seguros
seg1 = Seguro(1023, cliente1)
seg2 = Seguro(9641, cliente2)
seg3 = Seguro(8503, cliente3)

#seguros de vida
segVida1 = SeguroVida(3687, cliente1, 'Geovana')
segVida2 = SeguroVida(1289, cliente2, 'Lucas')
segVida3 = SeguroVida(3654, cliente3, 'Roberto')

#seguros de automóveis
segAut1 = SeguroAutomovel(8720, cliente1, 1001, 'Onix', '2022', 70000)
segAut2 = SeguroAutomovel(9756, cliente2, 1023, 'Jetta', '2019', 100000)
segAut3 = SeguroAutomovel(7622, cliente3, 1896, 'Kwid', '2019', 40000)

#controle de seguros
mitsi = ControleDeSeguros()

#CHAMADAS
#seg
print(f'SEGURO\n=-=-=-=-=--=-=-=-=--=-={seg1}')
print(f'SEGURO\n=-=-=-=-=--=-=-=-=--=-={seg2}')
print(f'SEGURO\n=-=-=-=-=--=-=-=-=--=-={seg3}')

#seg vida
print(segVida1)
print(segVida2)
print(segVida3)

#seg auto
print(segAut1)
print(segAut2)
print(segAut3)

#valor - seg vida
print(f'O valor do seu seguro de vida é: R${segVida1.calculaValor():.0f}')
totalseg.append(segVida1.calculaValor())

print(f'O valor do seu seguro de vida é: R${segVida2.calculaValor():.0f}')
totalseg.append(segVida2.calculaValor())

print(f'O valor do seu seguro de vida é: R${segVida3.calculaValor():.0f}')
totalseg.append(segVida3.calculaValor())

#premio - seg vida
segVida1.calculaPremio()
segVida2.calculaPremio()
segVida3.calculaPremio()

#valor - seg auto
print(f'O valor do seu seguro do seu automóvel: R$ {segAut1.calculaValor():.0f}')
totalseg.append(segAut1.calculaValor())

print(f'O valor do seu seguro do seu automóvel: R$ {segAut2.calculaValor():.0f}')
totalseg.append(segAut2.calculaValor())

print(f'O valor do seu seguro do seu automóvel: R$ {segAut3.calculaValor():.0f}')
totalseg.append(segAut3.calculaValor())

#premio - seg auto
segAut1.calculaPremio()
segAut2.calculaPremio()
segAut3.calculaPremio()

#fraqnuia - seg auto
segAut1.franquia()
segAut2.franquia()
segAut3.franquia()

#cadastro de seguros
mitsi.cadastrar(segVida1)
mitsi.cadastrar(segVida2)
mitsi.cadastrar(segVida3)

mitsi.cadastrar(segAut1)
mitsi.cadastrar(segAut2)
mitsi.cadastrar(segAut3)

print('\n=-=-=-=RELATÓRIO=-=-=-=-=\n')
mitsi.relatorio()
