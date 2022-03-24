from random import *
print('Gerador de cumprimentos')
print('-----------------------')

adjetivos = ["maravilhoso", "incrível", "acima da média", "excelente", 
            "atencioso", "ótimo", "astuto"]

hobbies = ["andar de bicicleta", "programar", "fazer chá",
            "desenhar", "cozinhar", "aconselhar"]

nome=input('Qual o seu nome?: ')
print(f'Aqui está o seu cumprimento {nome}: ')

#Obtém um item aleatório de ambas as listas e adiciona-os ao cumprimento
print(nome, 'você é' , choice(adjetivos) , 'em' , choice(hobbies))
print('De nada!')
