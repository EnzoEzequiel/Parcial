import re
import csv
import json
import sys
import time

# Expresiones regulares
regex_nombre = r'^[a-zA-Z0-9\s]+$'
patron = r"^(?:[0-9]|1[0-9]|2[0-7])$"
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
        print('24 - Determinar la cantidad de jugadores que hay por cada posición.')
        print('25- Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente..')
        print('26- Determinar qué jugador tiene las mejores estadísticas en cada valor.')
        print('27- Determinar qué jugador tiene las mejores estadísticas de todos.')
        print('0 - Salir')

        jugadores=datos["jugadores"]
        #leo la lista de jugadores, que contiene los diccionarios que buscamos, caso contrario chocara con el valor de nombre del equipo o cualquier otro de la lista
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
            case "24":
                cantidad_jugadores_por_posicion(jugadores)
            case "25":
                ordenar_por_all_star(jugadores)
            case "26":
                mejor_estadistica_por_valor(jugadores,"temporadas")
                mejor_estadistica_por_valor(jugadores,"puntos_totales")
            case "27":
                mejor_estadistica_global(jugadores)
            case _:
                print("opcion no valida, intente denuevo...")
                

def seleccionar_jugador(jugadores):
    indice = int(input("favor de ingresar el indice a buscar: "))
    jugador = obtener_jugador_por_indice(jugadores, indice)
    #si existe jugador muestro sus estadisticas
    if jugador:
        print("--- Estadísticas completas del jugador seleccionado ---")
        estadisticas_opcion_tres = jugador
        mostrar_estadisticas(jugador)
         #aca devuelvo las estadisticas para imprimir en la opcion 3
        return estadisticas_opcion_tres
    else:
        print("No se encontró un jugador con el índice especificado.")

def obtener_jugador_por_indice(jugadores, indice):
    try:
        #INTENTA, si el indice esta dentro del rango de jugadores lo devuelve
        if indice >= 1 and indice <= len(jugadores):
            #las posiciones arrancan en 0 asique devuelvo la opcion menos 1
            jugador=jugadores[indice - 1]
            return jugador
        else:
            #caso contrario error y no devuelve nada ademas del mensaje
            print("error de indice, intente denuevo")
            return None
    except ValueError:
        return None

def mostrar_estadisticas(jugador):
    estadisticas = jugador['estadisticas']
    for estadistica, valor in estadisticas.items():
        #muestro el valor dentro de las estadisticas capitalizado para q se vea lindo
        print(f"{estadistica.capitalize()}: {valor}")

def guardar_estadisticas_csv(jugador):
    #si existe el jugador
    if jugador:
        nombre_archivo = input("Ingresa el nombre del archivo CSV para guardar las estadísticas: ")
        with open(nombre_archivo+".csv", 'w', newline='') as archivo:
            #escribo el archivo con el nombre concatenado y una cabecera en la primer linea para darle columnas de clasificacion al archivo
            writer = csv.writer(archivo)
            writer.writerow(['Nombre', 'Temporadas', 'Puntos Totales', 'Promedio Puntos por Partido', 'Rebotes Totales', 'Promedio Rebotes por Partido',
                            'Asistencias Totales', 'Promedio Asistencias por Partido', 'Robos Totales', 'Bloqueos Totales',
                            'Porcentaje Tiros de Campo', 'Porcentaje Tiros Libres', 'Porcentaje Tiros Triples'])
            
            estadisticas = jugador['estadisticas']
            nombre = jugador['nombre']
            #tomo el nombre y las estadisticas que ya estan ordenadas para encajar con las columnas del archivo (en el orden por defecto)
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
            #si el nombre a buscar pasado todo a minuscula es igual al del indice actual TAMBIEN pasado todo a minuscula entonces matchea
            jugador_encontrado = jugador
            break
    if jugador_encontrado:
        logros = jugador_encontrado['logros']
        #tomo sus logros y los muestro iterandolo luego del print
        print(f"Logros del jugador {nombre}:")
        for logro in logros:
            print(f"- {logro}")
    #en caso de q no exista
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
    #basicamente la misma documentacion para buscar jugador especifico
    nombre = input("Ingresa el nombre del jugador que deseas verificar si es miembro del Salón de la Fama del Baloncesto: ")
    jugador_encontrado = None
    for jugador in jugadores:
        if jugador['nombre'].lower() == nombre.lower():
            jugador_encontrado = jugador
            break
    if jugador_encontrado:
        logros = jugador_encontrado['logros']
        #recorro y pregunto si ese string esta ahi
        if "Miembro del Salon de la Fama del Baloncesto" in logros:
            print(f"El jugador {nombre} es miembro del Salón de la Fama del Baloncesto.")
        else:
            print(f"El jugador {nombre} no es miembro del Salón de la Fama del Baloncesto.")
    else:
        print("No se encontró un jugador con el nombre especificado.")
        
        

def calcular_estadisticas(jugadores, opcion):
    if opcion == "rebotes":
        #busco al valor MAXIMO con  el metodo max que toma la lista de jugadores y el parametro a comparar, con una key que dentro tiene un lambda(funcion anonima) que devuelve el valor 
        #que existe dentro de la clave estadisticas que en este caso es rebotes totales 
        #lo mismo para el resto
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
        #pase la opcion por parametro y la matcheo con la estadistica que quiero buscar para usarla posteriormente
        #y el mensaje para el print
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
            return []

    if opcion != "logros":
        #ordeno la lista jugadores por el valor pasado por parametro dentro de la estadistica, se que suena repetitivo pero es lo que son.
        #luego doy vuelta la lista para que me queden los mayores adelante de todo, ya que por defecto me devuelve de menor a mayor y no de mayor a menor
        jugadores_mayor_estadistica = sorted(jugadores, key=lambda x: x['estadisticas'][estadistica], reverse=True)
        jugadores_seleccionados = []
        #lista vacia de jugadores
        max_valor_estadistica = jugadores_mayor_estadistica[0]['estadisticas'][estadistica]
        #tomo el primer valor de la lista ordenada de mayor a menor
        
        for jugador in jugadores_mayor_estadistica:
            #si hay alguno que matchee cn el primero de la lista lo agrego
            if jugador['estadisticas'][estadistica] == max_valor_estadistica:
                jugadores_seleccionados.append(jugador)
                
        print(f"El/los jugadores con la mayor cantidad de {mensaje} son:")   
        if jugadores_seleccionados:
            for jugador in jugadores_seleccionados:
                nombre = jugador['nombre']
                valor_estadistica = jugador['estadisticas'][estadistica]
                #guardo el valor dentro de nombre y estadistica buscada dentro de estadistica para mostrarlo
                print(f"{nombre} con {valor_estadistica} {mensaje}.")
        else:
            print("No se encontraron jugadores que cumplan con el requisito.")
    
    else:
        jugador_mayor_estadistica = max(jugadores, key=lambda x: len(x[estadistica]))
        #el que tenga la mayor cantidad de logros
        nombre = jugador_mayor_estadistica['nombre']
        cantidad_logros = len(jugador_mayor_estadistica[estadistica])
        #mido el largo de los logros xd
        #no comparo con mas como lo hice arriba porque michael jordan hay uno solo
        print(f"El jugador con la mayor cantidad de {mensaje} es {nombre} con {cantidad_logros} {mensaje}.")


#recibo la lista de jugadores y una opcion hardcodeada para el punto especifico(porque si eligio el punto en particular ya sabemos si es puntos, rebotes o asistencias)
def ingresar_valor_estadistica(jugadores, opcion):
    #misma logica que el metodo de arriba solo que comparo el valor flotante de lo que ingreso el usuario para que devuelva jugador en caso de la estadistica lo supere en la iteracion 
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

    valor = opcion_indicador(mensaje)
    #iteracion para comparar
    jugadores_seleccionados = [jugador for jugador in jugadores if jugador['estadisticas'][estadistica] > float(valor)]
    
    if jugadores_seleccionados:
        print(f"Jugadores con un promedio de {mensaje} por partido mayor a {valor}:")
        for jugador in jugadores_seleccionados:
            nombre = jugador['nombre']
            promedio_estadistica = jugador['estadisticas'][estadistica]
            print(f"- {nombre}: {promedio_estadistica}")
    else:
        print(f"No se encontraron jugadores con un promedio de {mensaje} por partido mayor al valor especificado.")



#recibo los jugadores de parametro, excluyo al q tiene el promedio mas bajo para luego sacar el promedio con la suma de los jugadores dividido los jugadores que exclui
def calcular_promedio_puntos_excluyendo_menor(jugadores):
    jugadores_ordenados = sorted(jugadores, key=lambda x: x['estadisticas']['promedio_puntos_por_partido'])
    jugadores_excluidos = jugadores_ordenados[1:]
    promedio_puntos_totales = sum([jugador['estadisticas']['promedio_puntos_por_partido'] for jugador in jugadores_excluidos])
    promedio_puntos_excluyendo_menor = promedio_puntos_totales / len(jugadores_excluidos)
    print(f"El promedio de puntos por partido excluyendo al jugador con el menor promedio es {promedio_puntos_excluyendo_menor}.")


#misma logica que en ingresar_valor_estadistica
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
    #creo diccionario de rankings
    posiciones_rankings = {
        'puntos_totales': 'Puntos',
        'rebotes_totales': 'Rebotes',
        'asistencias_totales': 'Asistencias',
        'robos_totales': 'Robos'
    }
    #diccionario vacio
    ranking = {}
    #por cada clave, valor dentro de posiciones rankings
    for posicion, descripcion in posiciones_rankings.items():
        jugadores_ordenados = sorted(jugadores, key=lambda jugador: jugador['estadisticas'][posicion], reverse=True)
        #ordeno de mayor a menor segun la clave de posiciones_rankings,ejemplo puntos_totales, rebotes_totales, etc...
        ranking[descripcion] = jugadores_ordenados
        #seteo una descripcion con el jugador ordenado segun la clave de posicion ranking
        
    nombre_archivo = input("Ingresa el nombre del archivo CSV para guardar las posiciones en los rankings: ")
    #concateno nombre del archivo csv
    with open(nombre_archivo + ".csv", 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        
        #Escribo encabezados de columnas
        encabezados = ['Jugador']
        for descripcion in posiciones_rankings.values():
            encabezados.append('Posicion en ' + descripcion)
        writer.writerow(encabezados)
        
        #Escribo datos de jugadores y posiciones
        for jugador in jugadores:
            nombre = jugador['nombre']
            row = [nombre]
            for descripcion in posiciones_rankings.values():
                #por cada estadistica de  ranking seteo los jugadores guardados en ranking
                jugadores_ranking = ranking[descripcion]
                #la nueva posicion es el index del jugador indice mas uno y la agrega a la LINEA
                posicion = jugadores_ranking.index(jugador) + 1
                row.append(posicion)
            writer.writerow(row)
    
    print(f"Las posiciones en los rankings de los jugadores han sido guardadas en el archivo '{nombre_archivo}.csv'.")


###########################################################################
#EJERCICIOS EXTRA
###########################################################################

def cantidad_jugadores_por_posicion(jugadores):
    jugadores_por_posicion = {}
    for jugador in jugadores:
        posicion = jugador["posicion"]
        if posicion in jugadores_por_posicion:
            jugadores_por_posicion[posicion] += 1
        else:
            jugadores_por_posicion[posicion] = 1
    
    for posicion, cantidad in jugadores_por_posicion.items():
        print(posicion + ": " + str(cantidad))

def ordenar_por_all_star(jugadores):
    jugadores_ordenados = sorted(jugadores, key=lambda jugador: obtener_cantidad_all_star(jugador), reverse=True)
    for jugador in jugadores_ordenados:
        all_star_count = obtener_cantidad_all_star(jugador)
        print(jugador["nombre"] + " (" + str(all_star_count) + " veces All-Star)")

def obtener_cantidad_all_star(jugador):
    logros = jugador["logros"]
    all_star_count = 0
    for logro in logros:
        if "veces All-Star" in logro:
            cantidad = "".join(filter(str.isdigit, logro))
            all_star_count = int(cantidad)
            break
    return all_star_count


def mejor_estadistica_por_valor(jugadores, valor):
    mejor_jugador = max(jugadores, key=lambda jugador: jugador["estadisticas"][valor])
    print("Mayor cantidad de " + valor + ": " + mejor_jugador["nombre"] + " (" + str(mejor_jugador["estadisticas"][valor]) + ")")

def mejor_estadistica_global(jugadores):
    mejor_jugador = max(jugadores, key=lambda jugador: sum(jugador["estadisticas"].values()))
    print("Mejor jugador en todas las estadísticas: " + mejor_jugador["nombre"])
    print("aunque no importa porque el mejor es michael jordan")

#####################################################################################################
#####################################################################################################



            
def mostrar_jugadores(jugadores):
    print("--- Lista de jugadores del Dream Team ---")
    for i, jugador in enumerate(jugadores):
        nombre = jugador["nombre"]
        posicion = jugador["posicion"]
        print(f"{i + 1}. {nombre} - {posicion}")
    
def imprimir_dato(dato):
    print(dato)
    
def menu_regexOpcion():
    #compara el patron de expresion regular cn la opcion ingresada
    opcion = input('Ingrese una opción: ')
    if re.match(patron, opcion):
        return opcion 
    else:
        return -1
    
def opcion_indicador(mensaje):
    #el parametro es la opcion hardcodeada en la llamada al metodo de este mismo.
    valor = input(f"Ingresa un valor para comparar el porcentaje de {mensaje}: ")
    if re.match(patronIndice, valor):
        return valor 
    else:
        return -1
    
def leer_archivo()->list:
    datos=[]
    #cargo datos jotason en lista vacia
    with open('dt.json', 'r') as f:
        datos = json.load(f)
    menu_parcial(datos)
    return datos

def main():
    leer_archivo()

main()



