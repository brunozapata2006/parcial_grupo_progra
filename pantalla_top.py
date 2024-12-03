import csv

import pygame

from colores import *
from configuraciones import *
from funciones import *
from funciones_dibujar import *


def dibujar_botones_top_mundial(pantalla, pos_mouse):  
    '''
    ¿Para qua sirve?
    Dibuja los botones en la pantalla para la seccion del ranking mundial de puntuaciones.

    ¿Qua parametro acepta?
    - pantalla: (pygame.Surface) La superficie donde se dibujan los botones.
    - pos_mouse: (tuple) La posicion del mouse para detectar el hover.

    ¿Qua retorna?
    - boton_volver_menu: El rectangulo que representa el boton "Volver al Menu" para su deteccion de colision.
    '''
    pygame.display.set_caption("Vamos a ver el top!")


    boton_volver_menu = dibujar_texto_con_boton_transparente(pantalla, "Volver al Menu", 620, 550, 200, 50, WHEAT1, RED1, pos_mouse)

    return boton_volver_menu


def cargar_top_ranking(path_csv):
    """
    Plantilla Documentacion
    ¿Para qua sirve?
    Esta funcion lee un archivo CSV y devuelve una lista con el top ranking de jugadores. El CSV debe contener dos columnas: nombre y puntuacion. Los datos se ordenan por puntuacion de mayor a menor.

    ¿Qua parametro acepta?
    - path_csv: (Path) Ruta al archivo CSV que contiene los nombres y puntuaciones de los jugadores.

    ¿Qua retorna?
    - top_ranking: (list) Una lista de tuplas con el nombre del jugador y su puntuacion, ordenada de mayor a menor puntuacion.
    """
    if not path_csv.exists():
        return []  # Si el archivo no existe, retorna una lista vacia

    top_ranking = []
    with open(path_csv, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo) #lector de csv, como readlines()
        next(lector)  # Saltar el encabezado
        for fila in lector:
            nombre, puntuacion = fila #desempaquetamos
            top_ranking.append((nombre, int(puntuacion)))  # Guarda el nombre y la puntuacion en tupla para luego usar .sort
            
    top_ranking.sort(key=lambda tupla: tupla[1], reverse=True) #el .sort ordena de menor a mayor y el reverse da vuelta esos valores, x es cada tupla de la lista
    return top_ranking

def dibujar_cuadro_top(pantalla, ranking, posicion_x, posicion_y):
    """
    Plantilla Documentacion
    ¿Para qua sirve?
    Esta funcion dibuja un cuadro en la pantalla donde se muestra el top ranking de jugadores con sus nombres y puntuaciones.

    ¿Qua parametro acepta?
    - pantalla: (Surface) La superficie en la que se dibujaran los elementos del top ranking.
    - top_ranking: (list) Una lista de tuplas con los nombres y puntuaciones de los jugadores.
    - posicion_x: (int) La posicion en el eje X donde se dibujara el cuadro del top.
    - posicion_y: (int) La posicion en el eje Y donde se dibujara el cuadro del top.

    ¿Qua retorna?
    - Ninguno. La funcion solo se encarga de dibujar el cuadro con los datos en la pantalla.
    """

    pygame.draw.rect(pantalla, CYAN3, (posicion_x, posicion_y, 300, 300))  # El cuadro

    font = pygame.font.SysFont('Arial', 24)
    # Titulo
    texto_top = font.render("Top Ranking", True, BLACK)
    pantalla.blit(texto_top, (posicion_x + 75, posicion_y + 10))  # Titulo centrado

    # Muestra el top
    for i, (nombre, puntuacion) in enumerate(ranking):  # Solo muestra los primeros 5
        texto = font.render(f"{i + 1}. {nombre}: {puntuacion}", True, BLACK)
        pantalla.blit(texto, (posicion_x + 20, posicion_y + 40 + (i * 40))) #centrar texto

def mostrar_top(pantalla, path_csv):
    """
    Plantilla Documentacion
    ¿Para qua sirve?
    esta funcion maneja la carga de datos y visualizacion del top ranking en la pantalla.

    ¿Qua parametro acepta?
    - pantalla: (Surface) La superficie de la ventana en la que se dibujaran los elementos del top ranking.
    - path_csv: (Path) Ruta al archivo CSV con los datos de los jugadores.

    ¿Qua retorna?
    - nada. la funcion carga los datos del top ranking y los dibuja en la pantalla.
    """
    # Cargar los datos del top ranking
    top_ranking = cargar_top_ranking(path_csv)

    # Dibujar el cuadro del top
    dibujar_cuadro_top(pantalla, top_ranking, 250, 100)