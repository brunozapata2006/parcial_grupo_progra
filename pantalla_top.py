import pygame
from funciones import *
from colores import *
from configuraciones import *
import csv

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


def cargar_top_ranking(path_csv):
    """
    Plantilla Documentacion
    ¿Para qué sirve?
    Esta función lee un archivo CSV y devuelve una lista con el top ranking de jugadores. El CSV debe contener dos columnas: nombre y puntuación. Los datos se ordenan por puntuación de mayor a menor.

    ¿Qué parámetro acepta?
    - path_csv: (Path) Ruta al archivo CSV que contiene los nombres y puntuaciones de los jugadores.

    ¿Qué retorna?
    - top_ranking: (list) Una lista de tuplas con el nombre del jugador y su puntuación, ordenada de mayor a menor puntuación.
    """
    if not path_csv.exists():
        return []  # Si el archivo no existe, retorna una lista vacía

    top_ranking = []
    with open(path_csv, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo) #lector de csv, como readlines()
        next(lector)  # Saltar el encabezado
        for fila in lector:
            nombre, puntuacion = fila
            top_ranking.append((nombre, int(puntuacion)))  # Guarda el nombre y la puntuación en tupla para luego usar .sort
            
    top_ranking.sort(key=lambda x: x[1], reverse=True) #el .sort ordena de menor a mayor y el reverse da vuelta esos valores, x es cada tupla de la lista
    return top_ranking

def dibujar_cuadro_top(pantalla, top_ranking, posicion_x, posicion_y):
    """
    Plantilla Documentacion
    ¿Para qué sirve?
    Esta función dibuja un cuadro en la pantalla donde se muestra el top ranking de jugadores con sus nombres y puntuaciones.

    ¿Qué parámetro acepta?
    - pantalla: (Surface) La superficie en la que se dibujarán los elementos del top ranking.
    - top_ranking: (list) Una lista de tuplas con los nombres y puntuaciones de los jugadores.
    - posicion_x: (int) La posición en el eje X donde se dibujará el cuadro del top.
    - posicion_y: (int) La posición en el eje Y donde se dibujará el cuadro del top.

    ¿Qué retorna?
    - Ninguno. La función solo se encarga de dibujar el cuadro con los datos en la pantalla.
    """
    # Dibuja el cuadro del top
    FONT = pygame.font.SysFont('Arial', 24)

    pygame.draw.rect(pantalla, CYAN3, (posicion_x, posicion_y, 300, 300))  # El cuadro

    # Título
    texto_top = FONT.render("Top Ranking", True, BLACK)
    pantalla.blit(texto_top, (posicion_x + 75, posicion_y + 10))  # Título centrado

    # Muestra el top
    for i, (nombre, puntuacion) in enumerate(top_ranking[:5]):  # Solo muestra los primeros 5
        texto = FONT.render(f"{i + 1}. {nombre}: {puntuacion}", True, BLACK)
        pantalla.blit(texto, (posicion_x + 20, posicion_y + 40 + (i * 40)))

def mostrar_top(pantalla, path_csv):
    """
    Plantilla Documentacion
    ¿Para qué sirve?
    Esta función maneja la carga de datos y visualización del top ranking en la pantalla.

    ¿Qué parámetro acepta?
    - pantalla: (Surface) La superficie de la ventana en la que se dibujarán los elementos del top ranking.
    - path_csv: (Path) Ruta al archivo CSV con los datos de los jugadores.

    ¿Qué retorna?
    - Ninguno. La función carga los datos del top ranking y los dibuja en la pantalla.
    """
    # Cargar los datos del top ranking
    top_ranking = cargar_top_ranking(path_csv)

    # Dibujar el cuadro del top
    dibujar_cuadro_top(pantalla, top_ranking, 250, 100)
