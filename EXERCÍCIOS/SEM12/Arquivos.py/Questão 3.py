a=int(input('Informe a populaçao do país A: '))
b=int(input('Informe a população do país B: '))

txa=0.02
txb=0.03
anos=0

paisa=b
paisb=a

if a>b:
    paisa=a
    paisb=b
    
while paisb<=paisa:
    anos+=1
    paisa=paisa+paisa*txa
    paisb=paisb+paisb*txb

print(f'Em {anos} anos, a população do país B irá ultrapassar a população do país A.')
