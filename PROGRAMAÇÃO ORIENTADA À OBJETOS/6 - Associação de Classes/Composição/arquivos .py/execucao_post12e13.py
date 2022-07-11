from exercicio_post12e13 import *

print('==BATERIAS==')
print(bateriaX)
print(bateriaY)
print(bateriaZ)
print('\n')

print('==CELULARES==')
print('Motorola')
print(motorola)
print('iPhone')
print(iphone)
print('Samsung')
print(samsung)

print('==MÉTODO LIGAR/DESLIGAR==')
motorola.LigarDesligar()
samsung.LigarDesligar()
motorola.retirarBateria()
motorola.LigarDesligar()

print('==MÉTODO COLOCAR BATERIA==')
motorola.colocarBateria(bateriaX)
iphone.colocarBateria(bateriaY)

print('==MÉTODO RETIRAR BATERIA==')
iphone.retirarBateria()
iphone.retirarBateria()

print('==MÉTODO LIGAR/DESLIGAR WIFI==')
motorola.LigarDesligar()
motorola.LigarDesligarWifi()
iphone.LigarDesligarWifi()
samsung.LigarDesligarWifi()
motorola.LigarDesligarWifi()


print('==MÉTODO ASSISTIR VÍDEO==')
motorola.assistirVideo(30)
iphone.assistirVideo(10)
motorola.LigarDesligarWifi()
motorola.assistirVideo(10)
motorola.assistirVideo(10)

print('==MÉTODO CARREGAR==')
motorola.carregar(80)
iphone.carregar(60)
samsung.carregar(30)

print('==MÉTODO DESCARREGAR==')
iphone.descarregar(75)
motorola.descarregar(70)
samsung.descarregar(50)