num1=int(input('Defina o primeiro número: '))
num2=int(input('Defina o segundo número: '))
num3=int(input('Defina o terceiro número: '))
num4=int(input('Defina o quarto número: '))
num5=int(input('Defina o quinto número: '))

media=(num1+num2+num3+num4+num5)/5
maximo=(max(num1, num2, num3, num4, num5))
minimo=(min(num1, num2, num3, num4, num5))

print(f'O maior número lido é: {maximo}')
print(f'O menor número lido é: {minimo}')
print(f'A média dos 5 números será: {media}')
