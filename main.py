import imagen
import codigo

import random
dibujoahorcado = ['''

   _____
   |   |
       |
       |
       |
       |

__________''', '''

  _____
  |   |
  O   |
      |
      |
      |
__________''','''

  _____
  |   |
  O   |
  |   |
      |
      |
__________''','''

  _____
  |   |
  O   |
 /|   |
      |
      |
__________''','''

  _____
  |   |
  O   |
 /|\  |
      |
      |
__________''','''

  _____
  |   |
  O   |
 /|\  |
 /    |
      |
__________''','''

  _____
  |   |
  O   |
 /|\  |
 / \  |
      |
__________''']

palabraspj = 'taza','carro','gato','murcielago','laptop','cubo','colores','estrella','ajedrez','bocina','tijeras','lapicera'.split()
 
def palabraAA(palabrael):
    eligpalab = random.randint(0, len(palabrael) - 1)
    return palabrael[eligpalab]
 



def tableroMost(dibujoahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(dibujoahorcado[len(letrasIncorrectas)])
    print()
 


 
    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()
 
    espaciosVacíos = '_' * len(palabraSecreta)
 



    for i in range(len(palabraSecreta)): 
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]
 
# mostrar la palabra dejando espacio
    for letra in espaciosVacíos: 
        print(letra, end=' ')
    print()
 




def obtenerIntento(letrasProbadas):
    #Verificar que el jugador ha ingresado sólo una letra.
    while True:
        print('Adivina la letra :).')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return intento
 



def jugarDeNuevo():
    print('¿Jugar de nuevo? (sí o no)')
    return input().lower()
 
print('A H O R C A D O  KNT')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = palabraAA(palabraspj)
juegoTerminado = False
 



while True:
    tableroMost(dibujoahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta)
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
        # ver si ganó.
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break


                
        if encontradoTodasLasLetras:
            print('¡GANASTE! La palabra secreta es "' + palabraSecreta)
            juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento
        if len(letrasIncorrectas) == len(dibujoahorcado) - 1:
            tableroMost(dibujoahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
            juegoTerminado = True
    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = palabraAA(palabraspj)
        else:
            break