import re
import csv
import json
import sys
import time

# Expresiones regulares
regex_nombre = r'^[a-zA-Z0-9\s]+$'
patron = r"^(?:[0-9]|1[0-9]|2[0-3])$"
patronIndice = r"^(?:[1-9]|[1-9][0-9]|100)$"


def menu_parcial(datos):
    paso_por_punto_dos = False
    estadisticas_opcion_tres = None
    while True:
        print('--- Menú Desafío #05 ---')
        print('1 - Mostrar la lista de todos los jugadores del Dream Team.')
        print('2 - Seleccionar un jugador por su índice y mostrar sus estadísticas completas.')
        print('3 - Guardar las estadísticas de ese jugador en un archivo CSV.')
        print('4 - Buscar un jugador por su nombre y mostrar sus logros.')
        print('5 - Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre.')
        print('6 - Ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.')
        print('7 - Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.')
        print('8 - Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.')
        print('9 - Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.')
        print('10 - Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.')
        print('11 - Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.')
        print('12 - Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.')
        print('13 - Calcular y mostrar el jugador con la mayor cantidad de robos totales.')
        print('14 - Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.')
        print('15 - Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.')
        print('16 - Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.')
        print('17 - Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.')
        print('18 - Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.')
        print('19 - Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.')
        print('20 - Ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.')
        print('23 - Calcular de cada jugador cuál es su posición en cada uno de los siguientes rankings: Puntos, Rebotes, Asistencias, Robos.')
        print('0 - Salir')

        jugadores=datos["jugadores"]
        opcion = menu_regexOpcion()
        match(opcion):
            case "0":
                print("Programa finalizado... ¡Adiós!")
                time.sleep(3)
                sys.exit()
            case "1":
                mostrar_jugadores(jugadores)
            case "2":
                paso_por_punto_dos=True
                estadisticas_opcion_tres=seleccionar_jugador(jugadores)
            case "3":
                if (paso_por_punto_dos != False):
                    guardar_estadisticas_csv(estadisticas_opcion_tres)
                else:
                    print("no paso por punto 2 para tener las estadisticas.")
            case "4":
                buscar_jugador(jugadores)
            case "5":
                calcular_promedio_puntos(jugadores)
            case "6":
                verificar_miembro_salon_fama(jugadores)
            case "7":
                calcular_estadisticas(jugadores,"rebotes")
            case "8":
                calcular_estadisticas(jugadores,"tiros_campo")
            case "9":
                calcular_estadisticas(jugadores,"asistencias")
            case "10":
                ingresar_valor_estadistica(jugadores, "puntos")
            case "11":
                ingresar_valor_estadistica(jugadores, "rebotes")
            case "12":
                ingresar_valor_estadistica(jugadores, "asistencias")
            case "13":
                calcular_mayor_estadistica(jugadores, "robos")
            case "14":
                calcular_mayor_estadistica(jugadores, "bloqueos")
            case "15":
                ingresar_valor_porcentaje(jugadores,"tiros_libres")
            case "16":
                calcular_promedio_puntos_excluyendo_menor(jugadores)
            case "17":
                calcular_mayor_estadistica(jugadores, "logros")
            case "18":
                ingresar_valor_porcentaje(jugadores,"tiros_triples")
            case "19":
                calcular_mayor_estadistica(jugadores, "temporadas")
            case "20":
                ingresar_valor_porcentaje(jugadores,"tiros_campo")
            case "23":
                calcular_posicion_rankings(jugadores)
            case _:
                print("opcion no valida, intente denuevo...")
                

def seleccionar_jugador(jugadores):
    indice = int(input("favor de ingresar el indice a buscar: "))
    jugador = obtener_jugador_por_indice(jugadores, indice)
    if jugador:
        print("--- Estadísticas completas del jugador seleccionado ---")
        estadisticas_opcion_tres = jugador
        mostrar_estadisticas(jugador)
        return estadisticas_opcion_tres
    else:
        print("No se encontró un jugador con el índice especificado.")

def obtener_jugador_por_indice(jugadores, indice):
    try:
        if indice >= 1 and indice <= len(jugadores):
            jugador=jugadores[indice - 1]
            return jugador
        else:
            print("error de indice, intente denuevo")
            return None
    except ValueError:
        return None

def mostrar_estadisticas(jugador):
    estadisticas = jugador['estadisticas']
    for estadistica, valor in estadisticas.items():
        print(f"{estadistica.capitalize()}: {valor}")

def guardar_estadisticas_csv(jugador):
    if jugador:
        nombre_archivo = input("Ingresa el nombre del archivo CSV para guardar las estadísticas: ")
        with open(nombre_archivo+".csv", 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(['Nombre', 'Temporadas', 'Puntos Totales', 'Promedio Puntos por Partido', 'Rebotes Totales', 'Promedio Rebotes por Partido',
                            'Asistencias Totales', 'Promedio Asistencias por Partido', 'Robos Totales', 'Bloqueos Totales',
                            'Porcentaje Tiros de Campo', 'Porcentaje Tiros Libres', 'Porcentaje Tiros Triples'])
            
            estadisticas = jugador['estadisticas']
            nombre = jugador['nombre']
            row = [nombre] + list(estadisticas.values())
            writer.writerow(row)
        print(f"Las estadísticas de los jugadores han sido guardadas en el archivo '{nombre_archivo}'.")
    else: 
        print("jugador inexistente seleccionado en opcion 2")

def buscar_jugador(jugadores):
    nombre = input("Ingresa el nombre del jugador que deseas buscar: ")
    jugador_encontrado = None
    for jugador in jugadores:
        if jugador['nombre'].lower() == nombre.lower():
            jugador_encontrado = jugador
            break
    if jugador_encontrado:
        logros = jugador_encontrado['logros']
        print(f"Logros del jugador {nombre}:")
        for logro in logros:
            print(f"- {logro}")
    else:
        print("No se encontró un jugador con el nombre especificado.")


def calcular_promedio_puntos(jugadores):
    total_puntos = 0
    total_jugadores = len(jugadores)
    
    for jugador in jugadores:
        estadisticas = jugador['estadisticas']
        promedio_puntos = estadisticas['promedio_puntos_por_partido']
        total_puntos += promedio_puntos

    promedio_general = total_puntos / total_jugadores
    print(f"Promedio general de puntos por partido: {promedio_general}")
    return promedio_general


def verificar_miembro_salon_fama(jugadores):
    nombre = input("Ingresa el nombre del jugador que deseas verificar si es miembro del Salón de la Fama del Baloncesto: ")
    jugador_encontrado = None
    for jugador in jugadores:
        if jugador['nombre'].lower() == nombre.lower():
            jugador_encontrado = jugador
            break
    if jugador_encontrado:
        logros = jugador_encontrado['logros']
        if "Miembro del Salon de la Fama del Baloncesto" in logros:
            print(f"El jugador {nombre} es miembro del Salón de la Fama del Baloncesto.")
        else:
            print(f"El jugador {nombre} no es miembro del Salón de la Fama del Baloncesto.")
    else:
        print("No se encontró un jugador con el nombre especificado.")

def calcular_estadisticas(jugadores, opcion):
    if opcion == "rebotes":
        jugador_mayor_rebotes = max(jugadores, key=lambda x: x['estadisticas']['rebotes_totales'])
        nombre = jugador_mayor_rebotes['nombre']
        rebotes_totales = jugador_mayor_rebotes['estadisticas']['rebotes_totales']
        print(f"El jugador con la mayor cantidad de rebotes totales es {nombre} con {rebotes_totales} rebotes.")
    elif opcion == "tiros_campo":
        jugador_mayor_porcentaje = max(jugadores, key=lambda x: x['estadisticas']['porcentaje_tiros_de_campo'])
        nombre = jugador_mayor_porcentaje['nombre']
        porcentaje_tiros_campo = jugador_mayor_porcentaje['estadisticas']['porcentaje_tiros_de_campo']
        print(f"El jugador con el mayor porcentaje de tiros de campo es {nombre} con {porcentaje_tiros_campo}%.")
    elif opcion == "asistencias":
        jugador_mayor_asistencias = max(jugadores, key=lambda x: x['estadisticas']['asistencias_totales'])
        nombre = jugador_mayor_asistencias['nombre']
        asistencias_totales = jugador_mayor_asistencias['estadisticas']['asistencias_totales']
        print(f"El jugador con la mayor cantidad de asistencias totales es {nombre} con {asistencias_totales} asistencias.")
    else:
        print("Opción inválida.")


def calcular_mayor_estadistica(jugadores, opcion):
    match(opcion):
        case "robos":
            estadistica = "robos_totales"
            mensaje = "robos totales"
        case "bloqueos":
            estadistica = "bloqueos_totales"
            mensaje = "bloqueos totales"
        case "logros":
            estadistica = "logros"
            mensaje = "logros"
        case "temporadas":
            estadistica = "temporadas"
            mensaje = "temporadas"
        case _:
            print("Opción inválida.")
            return 

    if opcion != "logros":
        jugador_mayor_estadistica = max(jugadores, key=lambda x: x['estadisticas'][estadistica])
        nombre = jugador_mayor_estadistica['nombre']
        valor_estadistica = jugador_mayor_estadistica['estadisticas'][estadistica]
        print(f"El jugador con la mayor cantidad de {mensaje} es {nombre} con {valor_estadistica} {mensaje}.")
    else:
        jugador_mayor_estadistica = max(jugadores, key=lambda x: len(x[estadistica]))
        nombre = jugador_mayor_estadistica['nombre']
        cantidad_logros = len(jugador_mayor_estadistica[estadistica])
        print(f"El jugador con la mayor cantidad de {mensaje} es {nombre} con {cantidad_logros} {mensaje}.")



def ingresar_valor_estadistica(jugadores, opcion):
    if opcion == "puntos":
        estadistica = "promedio_puntos_por_partido"
        mensaje = "puntos"
    elif opcion == "rebotes":
        estadistica = "promedio_rebotes_por_partido"
        mensaje = "rebotes"
    elif opcion == "asistencias":
        estadistica = "promedio_asistencias_por_partido"
        mensaje = "asistencias"
    else:
        print("Opción inválida.")
        return

    valor = opcion_indicador()
    jugadores_seleccionados = [jugador for jugador in jugadores if jugador['estadisticas'][estadistica] > float(valor)]
    
    if jugadores_seleccionados:
        print(f"Jugadores con un promedio de {mensaje} por partido mayor a {valor}:")
        for jugador in jugadores_seleccionados:
            nombre = jugador['nombre']
            promedio_estadistica = jugador['estadisticas'][estadistica]
            print(f"- {nombre}: {promedio_estadistica}")
    else:
        print(f"No se encontraron jugadores con un promedio de {mensaje} por partido mayor al valor especificado.")




def calcular_promedio_puntos_excluyendo_menor(jugadores):
    jugadores_ordenados = sorted(jugadores, key=lambda x: x['estadisticas']['promedio_puntos_por_partido'])
    jugadores_excluidos = jugadores_ordenados[:-1]
    promedio_puntos_totales = sum([jugador['estadisticas']['promedio_puntos_por_partido'] for jugador in jugadores_excluidos])
    promedio_puntos_excluyendo_menor = promedio_puntos_totales / len(jugadores_excluidos)
    print(f"El promedio de puntos por partido excluyendo al jugador con el menor promedio es {promedio_puntos_excluyendo_menor}.")



def ingresar_valor_porcentaje(jugadores, opcion):
    
    match(opcion):
        case "tiros_libres":
            estadistica = "porcentaje_tiros_libres"
            mensaje = "tiros libres"
        case "tiros_triples":
            estadistica = "porcentaje_tiros_triples"
            mensaje = "tiros triples"
        case "tiros_campo":
            estadistica = "porcentaje_tiros_de_campo"
            mensaje = "tiros de campo"
        case _:
            print("Opción inválida.")
            return
        
    valor = opcion_indicador(mensaje)
    jugadores_seleccionados = [jugador for jugador in jugadores if jugador['estadisticas'][estadistica] > float(valor)]
    
    if jugadores_seleccionados:
        print(f"Jugadores con un porcentaje de {mensaje} mayor a {valor}%:")
        for jugador in jugadores_seleccionados:
            nombre = jugador['nombre']
            porcentaje_estadistica = jugador['estadisticas'][estadistica]
            print(f"- {nombre}: {porcentaje_estadistica}%")
    else:
        print(f"No se encontraron jugadores con un porcentaje de {mensaje} mayor al valor especificado.")

def calcular_posicion_rankings(jugadores):
    posiciones_rankings = {
        'puntos_totales': 'Puntos',
        'rebotes_totales': 'Rebotes',
        'asistencias_totales': 'Asistencias',
        'robos_totales': 'Robos'
    }
    
    ranking = {}
    for posicion, descripcion in posiciones_rankings.items():
        jugadores_ordenados = sorted(jugadores, key=lambda jugador: jugador['estadisticas'][posicion], reverse=True)
        ranking[descripcion] = jugadores_ordenados
    
    nombre_archivo = input("Ingresa el nombre del archivo CSV para guardar las posiciones en los rankings: ")
    with open(nombre_archivo + ".csv", 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        
        # Escribir encabezados de columnas
        encabezados = ['Jugador']
        for descripcion in posiciones_rankings.values():
            encabezados.append('Posicion en ' + descripcion)
        writer.writerow(encabezados)
        
        # Escribir datos de jugadores y posiciones
        for jugador in jugadores:
            nombre = jugador['nombre']
            row = [nombre]
            for descripcion in posiciones_rankings.values():
                jugadores_ranking = ranking[descripcion]
                posicion = jugadores_ranking.index(jugador) + 1
                row.append(posicion)
            writer.writerow(row)
    
    print(f"Las posiciones en los rankings de los jugadores han sido guardadas en el archivo '{nombre_archivo}.csv'.")


            
def mostrar_jugadores(jugadores):
    print("--- Lista de jugadores del Dream Team ---")
    for i, jugador in enumerate(jugadores):
        nombre = jugador["nombre"]
        posicion = jugador["posicion"]
        print(f"{i + 1}. {nombre} - {posicion}")
    
def imprimir_dato(dato):
    print(dato)
    
def menu_regexOpcion():
    opcion = input('Ingrese una opción: ')
    if re.match(patron, opcion):
        return opcion 
    else:
        return -1
    
def opcion_indicador(mensaje):
    valor = input(f"Ingresa un valor para comparar el porcentaje de {mensaje}: ")
    if re.match(patronIndice, valor):
        return valor 
    else:
        return -1
    
def leer_archivo()->list:
    datos=[]
    with open('dt.json', 'r') as f:
        datos = json.load(f)
    menu_parcial(datos)
    return datos

def main():
    leer_archivo()

main()



