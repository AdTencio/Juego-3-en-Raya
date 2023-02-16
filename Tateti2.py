import os
import sys
import modulo2
import time



#modulo2.dibuja_cuadricula(lista_cuadricula)
#modulo1.dibuja_cuadricula(lista_cuadricula)
#Otras variables

ganadas = 0
perdidas = 0
empates = 0
salir = False

while not salir:
        lista_cuadricula = ['_'] * 9
        check3raya = [(0, 1, 2), (0, 3, 6), (0, 4, 8), (1, 4, 7), (2, 4, 6), (2, 5, 8), (3, 4, 5), (6, 7, 8)]
        lista_inputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 's', 'S']
        vacia = '_'
#Cuando sea True, hizo tateti
        jugador1_tateti = False
        jugador2_tateti = False
#Cuando sea True, es empate
        empate = False
#Turno: Sorteo de turno. (Si True arranca Jugador 1. Si False arranca Jugador 2)
        turno = modulo2.devuelve_numero_random(0, 9)
        if turno < 5:
            print(turno)
            turno = True
        else:
            turno = False
   
        while not empate: #Ejecutando juego
                #os.system('cls')
                modulo2.dibuja_cuadricula(lista_cuadricula)
                jugador1_tateti = modulo2.check_tateti(check3raya, lista_cuadricula, 'X') #Para chequear si hizo tateti Jug1
                jugador2_tateti = modulo2.check_tateti(check3raya, lista_cuadricula, 'O') #Para chequear si hizo tateti Jug2
                empate = modulo2.check_empate(vacia,lista_cuadricula) #Para chequear si hay empate
                if jugador1_tateti: #Si tateti Jug 1: Ganaste
                    print("TATETI Jugador 1!")
                    ganadas = int(ganadas) + 1
                    print(f"Vas ganando {ganadas} partidas")
                    break
                elif jugador2_tateti: #Si tateti Jug 2: Perdiste
                    print("TATETI Jugador 2!")
                    perdidas = int(perdidas) + 1
                    print(f"Vas perdiendo {perdidas} partidas")
                    break
                elif empate: #Si empate: empate
                    print("Empate")
                    empates = int(empates) + 1
                    print(f"Vas empatando {empates} partidas")
                    break         #A quien le toca jugar
                if turno: #Si es True, juega Jug 1
                        turno = modulo2.juega_jugador1(lista_inputs, lista_cuadricula) 
                else: #Sino es True, juega Jug 2
                    jugador2_tateti = modulo2.jugador2_intenta_tateti(check3raya, lista_cuadricula) #Busca dos O para poner la tercera.
                    if not jugador2_tateti:
                        turno = modulo2.jugador2_sedefiende(check3raya, lista_cuadricula)
                        if not turno:
                            tirada_random = modulo2.devuelve_numero_random(0, 8)
                            turno = modulo2.juega_jugador2_random(tirada_random, lista_cuadricula)
                        
                if turno:
                    print("Jugador 2 tirando..")
                    time.sleep(1) 
        otra = str(input('Jugar otra vez? S/N'))      
        if otra == 'S' or otra == 's':
            salir = False
        else:
                salir = True

sys.exit()