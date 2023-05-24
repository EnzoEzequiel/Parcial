import re
import csv
import json
import sys
import time

#validaciones:

regex_nombre = r'^[a-zA-Z0-9\s]+$'

patron = r'^[1-7]$'

patronDigitos = r"^\d{1,3}$"

bandera = False


def menu_parcial(listaJugadores):
    
    while True:
        print('--- Menú Desafío #05 ---')
        print('1 - Mostrar la lista de todos los jugadores del Dream Team.')
        print('2 - seleccionar un jugador por su índice y mostrar sus estadísticas completas')
        print('3 - guardar las estadísticas de ese jugador en un archivo CSV.')
        print('4 - buscar un jugador por su nombre y mostrar sus logros')
        print('5 - promedio de puntos por partido de todo el equipo del Dream Team')
        print('6 - ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.')
        print('7 - Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.')
        print('8 - Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.')
        print('9 - Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.')
        print('10 - ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.')
        print('11 - ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.')
        print('12 - ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.')
        print('13 - Calcular y mostrar el jugador con la mayor cantidad de robos totales.')
        print('14 - Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.')
        print('15 - ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.')
        print('16 - Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.')
        print('17 - Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos')
        print('18 - ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.')
        print('19 - Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas')
        print('20 - ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.')
        print('23 - Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking, Puntos, Rebotes, Asistencias, Robos')
        print('0 - Salir')

        opcion = menu_regexOpcion()
        if opcion == "0":
            print("programa finalizado...ADIOS!!")
            time.sleep(3)
            sys.exit()
        if opcion == "1":
            mostrarJugadores(listaJugadores)

            
def mostrarJugadores(listaJugadores):
    listaDict=[]
    for i in listaJugadores:
            print(listaJugadores[i])
            listaDict.append(listaJugadores[i])
    return listaDict
            
def imprimir_dato(dato):
    print(dato)
    
def menu_regexOpcion():
    opcion = input('Ingrese una opción: ')
    if re.match(patron, opcion):
        return opcion 
    else:
        return -1
    
def leer_archivo()->list:
    listaJugadores=[]
    with open('dt.json', 'r') as f:
        listaJugadores = json.load(f)
    #normalizar_datos(listaJugadores)
    menu_parcial(listaJugadores)
    return listaJugadores

# def normalizar_datos(listaJugadores):
#     if not listaJugadores:
#         print("Error: Lista de héroes vacía")
#         return
    
#     normalizado = False
#     for jugador in listaJugadores:
#         for key, value in jugador:
#             if key in ['']:
#                 jugador[key] = float(value)
#                 normalizado = True
#     if normalizado:
#         print("Datos normalizados")
        
# def condiciones(condiciones):
#     print("entro a opciones de condicion")
#     contador=0
#     termino=False
#     for item in condiciones:
#         contador = contador+1
#         contadorString=str(contador)
#         print(contadorString+" - "+item)
    
#     seleccionIngresada=int(input("favor de ingresar condicion: "))
    
#     print(seleccionIngresada)
#     if (contador >= seleccionIngresada and seleccionIngresada > 0):
#         return condiciones[seleccionIngresada-1]
#     else:
#         print("valor ingresado no valido...")
#         main()
    

# def opciones_dinamicas(puntoElegido)->list:
#     opcion = []
    
#     return opcion
        
def main():
    leer_archivo()

main()



