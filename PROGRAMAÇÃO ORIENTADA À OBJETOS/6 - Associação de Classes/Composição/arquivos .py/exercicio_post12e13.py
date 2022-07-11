class Bateria:
    def __init__(self, codigo, capacidade, percentualCarga):
        self.__codigo = codigo
        self.__capacidade = capacidade
        self.__percentualCarga = percentualCarga

    def __str__(self):
        return f'Código: {self.__codigo} \nCapacidade: {self.__capacidade} \nPercentual da carga: {self.__percentualCarga}'


    #DECORADORES
    @property
    def codigo(self):
        return self.__codigo

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def percentualCarga(self):
        return self.__percentualCarga

    @percentualCarga.setter
    def percentualCarga(self, valor):
        self.__percentualCarga = valor


    #MÉTODOS
    def carregar(self, valor):
        if self.__percentualCarga+valor >100:
            print(f'Bateria em {self.__percentualCarga}%! Carga máxima de 100%')
        else:
            self.__percentualCarga += valor
            print(f'Sua bateria carregou {valor}%! Bateria em {self.__percentualCarga}%')

    def descarregar(self, valor):
        if self.__percentualCarga-valor <0:
            print(f'Bateria em 0%')
        else:
            self.__percentualCarga -= valor
            print(f'Bateria desscarregou {valor}%! Bateria em {self.__percentualCarga}%')

#INSTÂNCIAS
bateriaX = Bateria(1, 5000, 100)
bateriaY = Bateria(2, 4500, 65)
bateriaZ = Bateria(3, 4000, 0)



#CLASSE 2
class Celular:
    def __init__(self, imei, bateria=None, wifi='desligado', estado='desligado'):
        self.__imei = imei
        if type(bateria) == Bateria:
            self.__bateria = bateria
        else:
            self.__bateria = None
        self.__wifi = wifi
        self.__estado = estado

    def __str__(self):
        return f'IMEI: {self.__imei} \nBateria: {self.__bateria} \nWiFi: {self.__wifi} \nEstado: {self.__estado} \n'


    #DECORADORES
    @property
    def mei(self):
        return self.__imei

    @property
    def bateria(self):
        return self.__bateria

    @bateria.setter
    def bateria(self, estado):
        self.__bateria = estado

    @property
    def wifi(self):
        return self.__wifi

    @wifi.setter
    def wifi(self, valor):
        self.__wifi = valor

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        self.__estado = valor


    #MÉTODOS
    def LigarDesligar(self):
        if self.__bateria != None:
            if self.__bateria.percentualCarga > 0:
                self.__estado = 'ligado'
                print(f'Celular {self.__estado}! \nBateria em {self.__bateria.percentualCarga}% \n')
            else:
                self.__estado='desligado'
                print(f'Celular {self.__estado} \nAparelho sem carga! \n')
        else:
            self.__estado='desligado'
            print(f'Celular {self.__estado} \nAparelho sem bateria! \n')
        

    def colocarBateria(self, bateria):
        if self.__bateria == None:
            if type(bateria) == Bateria:
                self.__bateria = bateria
                print(f'Bateria adicionada!')
        else:
            print(f'Aparelho já possui uma bateria!\n')

    def retirarBateria(self):
        if self.__bateria != None:
            self.__bateria = None
            print(f'Bateria retirada!')
        else:
            print(f'Aparelho já está sem bateria!\n')

    def LigarDesligarWifi(self):
        if self.__bateria != None:
            if self.__estado == 'ligado':
                if self.__wifi == 'ligado':
                    self.__wifi = 'desligado'
                else:
                    self.__wifi = 'ligado'
                print(f'Wifi {self.__wifi} \n')
            else:
                print('Impossível executar esta ação! Celular está desligado!\n')
        else:
            print(f'Impossível executar ação! Celular não possui bateria!\n')

    def assistirVideo(self, tempo):
        if tempo < 20:
            if self.__estado == 'ligado':
                if self.__wifi == 'ligado':
                    if self.__bateria.percentualCarga > 0:
                        bateria_gasta = tempo * 5
                        new_perc = self.__bateria.percentualCarga - bateria_gasta
                        print(f'Assistindo vídeo... \nBateria gasta: {bateria_gasta}% \nPercentual atual de bateria: {new_perc}% \n')
                        if bateria_gasta > self.__bateria.percentualCarga:
                            self.__estado = 'desligado'
                            print(f'Você gastou toda a bateria!')
                        self.__bateria.percentualCarga -= bateria_gasta
                    else:
                        print(f'Impossível executar ação! Celular sem bateria!')
                else:
                    print(f'Impossível executar ação! Wifi está desligado!')
            else:
                print('Impossível executar esta ação! Celular está desligado!\n')
        else:
            print(f'Você excedeu o limite de tempo! Bateria não pode ficar negativa!')

    def carregar(self, valor):
        if self.__bateria != None:
            self.__bateria.carregar(valor)
        else:
            print('Impossível carregar! Celular não possui bateria!')

    def descarregar(self, valor):
        if self.__bateria != None:
            self.__bateria.descarregar(valor)
        else:
            print('Impossível carregar! Celular não possui bateria!')

#INSTÂNCIAS:
motorola = Celular(748596, Bateria(1, 5000, 100))
iphone = Celular(102365, Bateria(2, 4500, 65))
samsung = Celular(892016, Bateria(3, 4000, 0))



