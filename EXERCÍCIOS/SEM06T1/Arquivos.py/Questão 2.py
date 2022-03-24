def numero(n):
    if (n%2==0):
        return False
    else:
        return True


num=int(input('Digite um valor inteiro: '))
result=numero(num)
print(f' Seu número é impar? {result}')
