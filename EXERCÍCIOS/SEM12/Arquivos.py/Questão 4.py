n=int(input('Digite a sua data de nascimento (ddmmaaaa): '))
soma=0
while n>0:
    rest=n%10
    n=(n-rest)/10
    soma=soma+rest

print(f'O seu número da sorte é: {soma:.0f}')
