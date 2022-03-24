def vogal(x):
    if x in ('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False

def main():
    letra=input('Digite uma letra: ').lower()
    vog=vogal(letra)
    print(f' A letra {letra} é vogal? \n {vog}')

if __name__=='__main__':
    main()
