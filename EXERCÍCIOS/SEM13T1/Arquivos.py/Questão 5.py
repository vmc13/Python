a=[]
b=[]
valora=valorb=0
for i in range(1, 26):
    valora=int(input(f'Insira o {i}º valor: '))
    a.append(valora)

for i in range(1, 26):
    valorb=int(input(f'Insira o {i}º valor: '))
    b.append(valorb)
   
c=[*sum(zip(a,b),())]

print(f'Lista A: \n{a}')
print(f'Lista B: \n{b}')
print(f'Lista C: \n {c}')
