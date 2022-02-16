from math import prod

def lista_num(n):
    num=[]
    for i in range (1, n+1):
        num.append(int(input(f'Insira o {i}º número: ')))
    return num

def soma(num):
    soma=sum(num)
    return soma

def multi(num):
    multi=prod(num)
    return multi

def main():
    numeros=lista_num(10)
    s=soma(numeros)
    m=multi(numeros)
    print(f'Os números inseridos foram: {numeros}')
    print(f'A soma dos números será: {s}')
    print(f'O produto dos números será: {m}')

if __name__=='__main__':
    main()
