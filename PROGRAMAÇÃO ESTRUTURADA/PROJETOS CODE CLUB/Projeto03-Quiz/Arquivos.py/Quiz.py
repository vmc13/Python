print("No Python, como se chama uma 'caixa' usada para armazenar dados?")
resposta=input()
if resposta == "variável":
    print(' :) ' *100)
else:
    print(" :( " *100)


print("Obrigado por jogar!")

print(=-*15)

print("No Python, como se chama uma 'caixa' usada para armazenar dados?")
resposta=input().lower()

if resposta == "variável":
    print(' :) ' *100)
else:
    print(" :( " *100)


print("Obrigado por jogar!")

print(=-*15)

print('''
Q1 - No Python, como se chama uma 'caixa' usada para armazenar dados?
a - texto
b - variável
c - uma caixa de sapatos
''')
resposta=input().lower()

if resposta=='a':
    print('Não - texto é um tipo de dado :(')
elif resposta=='b':
    print('Correto! :)')
elif resposta=='c':
    print('Não seja bobinho :(')
else:
    print('Você não escolheu a, b ou c :(')

print(=-*15)

print('''
Q1 - No Python, como se chama uma 'caixa' usada para armazenar dados?
a - texto
b - variável
c - uma caixa de sapatos
''')
resposta=input().lower()

if resposta=='a':
    print('Não - texto é um tipo de dado :(')
elif resposta=='b':
    print('Correto! :)')
elif resposta=='c':
    print('Não seja bobinho :(')
else:
    print('Você não escolheu a, b ou c :(')


if resposta=='b':
    score=1
    print(f' Score={score}')
else:
    score=0
    print(f' Score={score}')


print('''
Q2 - No Python, o que significa "Concatenar"?
a - Dividir duas variáveis
b - Conjunto de caracteres
c - Unir dados
''')
resposta=input().lower()

if resposta=='a':
    print('Errado - concatenar NÃO é a divisão de variáveis :(')
elif resposta=='b':
    print('Errado - concatenar NÃO é um conjunto de caracteres :(')
elif resposta=='c':
    print('Correto! Concatenar significa unir dados de forma lógica! :)')
else:
    print('Você não escolheu a, b ou c :(')


if resposta=='c':
    scoreq2=score+1
    print(f' Score={scoreq2}')
else:
    scoreq2=score
    print(f' Score={scoreq2}')


print('''
Q3 - Onde as variáveis ficam armazenadas?
a - Na memória RAM do computador
b - No banco de dados
c - No banco de dados, no software e na memória RAM
''')
resposta=input().lower()

if resposta=='a':
    print('Correto! :)')
elif resposta=='b':
    print('Errado - as variáveis não são armazenadas no banco de dados :(')
elif resposta=='c':
    print('Errado - as variáveis não são armazenadas em todos esses locais :(')
else:
    print('Você não escolheu a, b ou c :(')


if resposta=='a':
    scoreq3=scoreq2+1
    print(f' Final Score={scoreq3}')
else:
    scoreq3=scoreq2
    print(f' Score={scoreq3}')


print('Obrigado por responder todas as perguntas!')
print(':)'*100)
