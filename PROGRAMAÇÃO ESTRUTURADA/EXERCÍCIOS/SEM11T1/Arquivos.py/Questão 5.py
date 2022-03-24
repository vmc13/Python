nota=0
while True:
    nota=float(input('Digite sua nota: '))
    if 8.5<=nota<=10:
        print('A')
        break
    elif 7.0<=nota<=8.4:
        print('B')
        break
    elif 5.0<=nota<=6.9:
        print('C')
        break
    elif 4.0<=nota<=4.9:
        print('D')
        break
    elif 0.0<=nota<3.9:
        print('E')
        break
    else:
         print('Nota inválida.')

