def vogecon(z):
    if z in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'):
        return True
    else:
        return False


def main():
    letra=input('Digite um caractere: ').lower()
    vc=vogecon(letra)
    print(f'O caractere {letra} é vogal ou consoante? \n {vc}')

if __name__=='__main__':
    main()
