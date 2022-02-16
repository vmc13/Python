def numero(n):
    if n >= '0' and n <= '9' :
        return True
    else:
        return False

num=input('Digite um valor: ')
result=numero(num)
print(f' O número está entre 0 e 9? {result}')
