def med (a, b, c, d, e):
    media=(a+b+c+d+e)//5
    return media
    if a>media:
        return a
    if b>media:
        return b
    if c>media:
        return c
    if d>media:
        return d
    if e>media:
        return e

    
n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número: '))
n3=int(input('Digite o terceiro número: '))
n4=int(input('Digite o quarto número: '))
n5=int(input('Digite o quinto número: '))
m=med(n1, n2, n3, n4, n5)
print(f'A média é: {m:.2f}')

if n1>m:
    print(f'{n1} é maior que a média')
if n2>m:
    print(f'{n2} é maior que a média')
if n3>m:
    print(f'{n3} é maior que a média')
if n4>m:
    print(f'{n4} é maior que a média')
if n5>m:
    print(f'{n4} é maior que a média')
