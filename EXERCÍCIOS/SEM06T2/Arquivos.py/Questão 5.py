def caractere(x):
    if x in ('a', 'e', 'i', 'o', 'u'):
        return print('Vogal')
    if x in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
        return print('Consoante')
    if x in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return print('Número')
    else:
        print('Símbolo')


def main():
    letra=input('Digite um caractere: ').lower()
    vcns=caractere(letra)


if __name__=='__main__':
    main()
