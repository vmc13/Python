populacao=float(input('Infome a população de aves do início do ano 1600: '))
prc_morte=0.06
prc_nasc=0.01
cond_parada=populacao*0.1
ano=1599

while populacao>cond_parada:
    born=populacao*prc_nasc
    death=populacao*prc_morte
    new_pop=populacao-death+born
    ano+=1
    populacao=new_pop
    print(f'{ano},{born:.0f},{death:.0f},{populacao:.0f}')

