cont1=0
cont2=0
for c in range(1,101):
    num=int(input(f'Digite o {c}º número: '))
    if num%2==0:
        cont1+=1
    elif num%2!=0:
        cont2+=1
print(f'Possui {cont1} números pares e {cont2} números ímpares')
