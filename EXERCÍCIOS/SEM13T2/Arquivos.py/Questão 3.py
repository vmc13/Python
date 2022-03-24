A=[]
B=[]
C=[]
valora=valorb=0
for i in range(1, 21):
    valora=int(input(f'Insira o {i}º valor da lista A: '))
    A.append(valora)

for i in range(1, 21):
    valorb=int(input(f'Insira o {i}º valor da lista B: '))
    B.append(valorb)

for i in range(20):
    C.append(A[i]+B[i])

print(f'Lista A:\n{A}')
print(f'Lista B:\n{B}')
print(f'Lista C:\n{C}')
