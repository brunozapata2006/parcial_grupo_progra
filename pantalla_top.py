import pygame
from funciones import *
from colores import *
from configuraciones import *

def dibujar_botones_top_mundial(pantalla, pos_mouse):  
    '''
    ¿Para qué sirve?
    Dibuja los botones en la pantalla para la sección del ranking mundial de puntuaciones.

    ¿Qué parámetro acepta?
    - pantalla: (pygame.Surface) La superficie donde se dibujan los botones.
    - pos_mouse: (tuple) La posición del mouse para detectar el hover.

    ¿Qué retorna?
    - boton_volver_menu: El rectángulo que representa el botón "Volver al Menu" para su detección de colisión.
    '''
    pygame.display.set_caption("Vamos a cargar preguntas!")

    # Obtener la posición del mouse
    pos_mouse = pygame.mouse.get_pos()  # x, y  

    # Dibujar el botón de "Volver al Menu"
    boton_volver_menu = dibujar_texto_con_boton_transparente(pantalla, "Volver al Menu", 620, 550, 200, 50, WHEAT1, RED1, pos_mouse)
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Retornar el botón para verificar colisión
    return boton_volver_menu

def mostrar_ranking(csv):
    '''
    ¿Para qué sirve?
    Lee los datos de un archivo CSV, ordena los jugadores por su puntuación y los muestra en un ranking.

    ¿Qué parámetro acepta?
    - csv: (str) El archivo CSV que contiene los datos del ranking.

    ¿Qué retorna?
    - datos: Una lista con las filas del archivo CSV ordenadas por puntuación de forma descendente.
    '''
    # Abrir el archivo CSV y leer las líneas
    with open(csv, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    # Obtener los encabezados (índices de las columnas)
    indice = lineas[0].strip().split(",")    
    datos = []

    # Leer los datos del archivo y almacenarlos en una lista
    for linea in lineas[1:]:
        fila = linea.strip().split(",")
        datos.append(fila)
    
    # Obtener el índice de la columna de puntuación
    indice_ranking = indice.index("Puntuacion")

    # Definir una función para obtener la puntuación de cada fila
    def obtener_puntuacion(fila):
        return int(fila[indice_ranking])

    # Ordenar los datos utilizando la función auxiliar
    datos_ordenados = sorted(datos, key=obtener_puntuacion, reverse=True)

    # Devolver los datos ordenados por puntuación
    return datos_ordenados
