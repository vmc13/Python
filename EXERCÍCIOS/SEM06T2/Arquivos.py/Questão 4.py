def voconu(z):
    if z in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return True
    else:
        return False


def main():
    letra=input('Digite um caractere: ').lower()
    vcn=voconu(letra)
    print(f'O caractere {letra} é vogal ou consoante ou número? \n {vcn}')

if __name__=='__main__':
    main()
