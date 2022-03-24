def convertF(n):
    return round(((n*(9/5))+32), 4)

#conversão para °C
def convertC(n):
    return round(((n-32)*(5/9)), 4)

def temperatura(temp1, escala1, temp2, escala2):
    graus=()
    if escala1=='C' and escala2=='C':
        soma=temp1+temp2
        som=round(soma, 4)
        graus=(som, 'C')

    elif escala1=='F' and escala2=='F':
        soma=temp1+temp2
        som=round(soma, 4)
        graus=(som, 'F')
    
    elif escala1=='C' and escala2=='F':
        soma=convertF(temp1)+temp2
        som=round(soma, 4)
        graus=(som, 'F')
    
    elif escala1=='F' and escala2=='C':
        soma=convertC(temp1)+temp2
        som=round(soma, 4)
        graus=(som, 'C')

    return graus

def main():
    temp1=float(input('Informe uma temperatura: '))
    escala1=input('Informe uma escala (C/F): ').upper()[0]

    temp2=float(input('Informe uma temperatura: '))
    escala2=input('Informe uma escala (C/F): ').upper()[0]
    print(f'A soma das temperaturas inseridas em °{escala2} será: ')
    print(temperatura(temp1, escala1, temp2, escala2))

if __name__=='__main__':
    main()
