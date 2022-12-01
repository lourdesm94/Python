import random as r


class Adivinanza:
    def __init__(self, dato):
        self.codigo = ''
        self.cant_digitos = dato

    def generador_num(self):
        for i in range(self.cant_digitos):
            digitos = str(r.randrange(0,9))
            candidato = r.choice(digitos)
            self.codigo = self.codigo + candidato        
        return self.codigo
                 
while True:
    try:
        data = int(input("De cuantos digitos quieres intenar adivinar?: "))
        a = Adivinanza(dato=data)
        num = str(a.generador_num()).strip()
        desicion = True

        print(f"el valor es: {num}")
        print (f"Tienes que adivinar un numero de {len(str(num))} cifra(s) distinta(s)")
        while True:
            try:
                propuesta = input(f"Propón un numero de {len(str(num))} cifra(s): ").title()
                intentos = 0
                
                while propuesta != num:
                    intentos = intentos + 1
                    aciertos = 0
                    coincidencias = 0
                    
                    for i in range(data):
                        if propuesta[i] == num[i]:
                            aciertos =  aciertos + 1
                        elif propuesta[i] in num:
                            coincidencias = coincidencias + 1
                            
                    print (f"Tu propuesta ({propuesta}) tiene {aciertos} aciertos y {coincidencias} coincidencias.")
                        
                    if intentos % 3 == 0:
                        while desicion:       
                            valor = input('¿Desea rendirse?, coloque y/n: ').lower()
                            if valor == 'y':
                                print (f"El codigo era {num}")
                                print ("Suerte la proxima vez!")
                                exit()
                            elif valor == 'n':
                                print("Ok, continuemos con el juego")
                                desicion = False
                            else:
                                print('Valor ingresado incorrecto!!')
                                
                    propuesta = input(f"Propón un numero de {len(str(num))} cifra(s): ").title()
                                
            except IndexError:
                    print (f"Cantidad de numeros ingresados incorrectos")
            
    except ValueError:
            print (f"el dato que ingresaste es incorrecto")