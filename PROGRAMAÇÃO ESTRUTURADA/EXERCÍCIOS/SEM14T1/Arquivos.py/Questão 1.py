#conversão para °F:
def convertF(n):
    return round(((n*(9/5))+32), 4)

#conversão para °C
def convertC(n):
    return round(((n-32)*(5/9)), 4)

def temperatura(temp1, escala1, temp2, escala2):
    graus=()
    if escala1=='C' and escala2=='F':
        #temp2 convertida em °C assim como a temp1
        temp2c=convertC(temp2)
        #condições
        if temp1>temp2c:
            graus=(temp1, escala1)
        if temp1<temp2c:
            graus=(temp2, escala2)

    elif escala1=='F' and escala2=='C':
        #temp1 convertida em °C assim como a temp2
        temp1c=convertC(temp1)
        #condições
        if temp1c>temp2:
            graus=(temp1, escala1)
        if temp1c<temp2:
            graus=(temp2, escala2)

    #se as duas escalas forem iguais
    elif escala1==escala2:
        if temp1>temp2:
            graus=(temp1, escala1)
        if temp1<temp2:
            graus=(temp2, escala2)
    return graus

def main():
    temp1=float(input('Informe uma temperatura: '))
    escala1=input('Informe uma escala (C/F): ').upper()[0]

    temp2=float(input('Informe uma temperatura: '))
    escala2=input('Informe uma escala (C/F): ').upper()[0]
    print('A maior temperatura é: ')
    print(temperatura(temp1, escala1, temp2, escala2))

if __name__=='__main__':
    main()
