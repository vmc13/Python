def consoante(z):
    if z in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
        return True
    else:
        return False


def main():
    letra=input('Digite um caractere: ').lower()
    con=consoante(letra)
    print(f'O caractere {letra} é consoante? \n {con}')


if __name__=='__main__':
    main()
