def calc_idade(a,b,c,x,y,z):
    if a == x and b == y:
        return (c-z)
    elif x>a and b == y:
        return (c-z-1)
    elif b<y:
        return (c-z-1)
    else:
        return (c-z)

    
def main():
    d1=int(input('Dia atual: '))
    m1=int(input('Mês atual: '))
    a1=int(input('Ano atual: '))

    d2=int(input('Dia do nascimento: '))
    m2=int(input('Mês do nascimento: '))
    a2=int(input('Ano do nascimento: '))

    data=calc_idade(d1,m1,a1,d2,m2,a2)
    print(f'Sua idade é: {data}')


if __name__=='__main__':
    main()
