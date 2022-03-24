#Desafio: Variáveis e loops

def calculo_angulo(lados):
    angulo=360/lados
    return angulo

def main():
    qnt_lados=int(input('Insira a quantidade de lados da sua figura: '))
    lado=calculo_angulo(qnt_lados)
    print(f'Os ângulos da sua figura serão: {lado:.0f}')

if __name__=='__main__':
    main()

