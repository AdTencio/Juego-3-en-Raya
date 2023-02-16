import random
import sys
import os
#Dibujar cuadricula
def dibuja_cuadricula(lista_cuadricula):
    print('\n')
    print('                            * *                          ')
    print('     {}      {}      {}     * *     1       2       3   *'.format(lista_cuadricula[0], lista_cuadricula[1], lista_cuadricula[2]))
    print('                            * *                          ')
    print('     {}      {}      {}     * *     4       5       6   *'.format(lista_cuadricula[3], lista_cuadricula[4], lista_cuadricula[5]))
    print('                            * *                          ')
    print('     {}      {}      {}     * *     7       8       9   *'.format(lista_cuadricula[6], lista_cuadricula[7], lista_cuadricula[8]))
    
#Numero random para sorteo
def devuelve_numero_random(cero, ocho):
    return random.randint(cero, ocho)
#Jugada de Jugador1
def juega_jugador1(lista_inputs, lista_cuadricula):
     tirada = ''
     
     while tirada not in lista_inputs:
         tirada = str(input('Turno jugador 1: Elija una casilla valida (1 al 9)'))
    
     if tirada == 's' or tirada == 'S':
        sys.exit()
        
     tirada = int(tirada)   
     if lista_cuadricula[tirada - 1] == '_':
         lista_cuadricula[tirada -1] = 'X' 
         
         return False
     return True
#Jugador 2 busca forma de hacer tateti
def jugador2_intenta_tateti(check3raya, lista_cuadricula):
    for i in range(9):
        if lista_cuadricula[i] == '_':
            lista_cuadricula[i] = 'O'
            for check in check3raya:
                 if lista_cuadricula[check[0]] == 'O' and lista_cuadricula[check[1]] == 'O' and lista_cuadricula[check[2]] == 'O':
                    return True
            lista_cuadricula[i] = '_'
    return False
#Jugador 2 busca defenderse de posible tateti de jug 1
def jugador2_sedefiende(check3raya, lista_cuadricula):
        for i in range(9):
            if lista_cuadricula[i] == '_': 
                lista_cuadricula[i] = 'X'
                for check in check3raya:
                     if lista_cuadricula[check[0]] == 'X' and lista_cuadricula[check[1]] == 'X' and lista_cuadricula[check[2]] == 'X':
                        lista_cuadricula[i] = 'O'
                         #El error esta antes de este dibujo
                        return True
                lista_cuadricula[i] = '_' 
        return False
#Jugador 2 juega random
def juega_jugador2_random(tirada_random, lista_cuadricula):
    if lista_cuadricula[tirada_random] == '_':
        lista_cuadricula[tirada_random] = 'O'
         
        return True
    return False
#Checkear si hay tateti
def check_tateti(check3raya, lista_cuadricula, xo):
        for i in check3raya:
            if lista_cuadricula[i[0]] == xo and lista_cuadricula[i[1]] == xo and lista_cuadricula[i[2]] == xo:
                return True
        return False
#Checkear empate                        
def check_empate(vacia, lista_cuadricula):
        if vacia not in lista_cuadricula:
            return True
        return False 
    