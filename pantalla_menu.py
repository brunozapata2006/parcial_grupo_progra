import pygame
from funciones import *
from colores import *
from configuraciones import *

def dibujar_menu_botones(pantalla, pos_mouse):
    '''
    ¿Para qué sirve?
    Esta función dibuja un menú principal en la pantalla con varias opciones de botones.

    ¿Qué parámetro acepta?
    - pantalla: (pygame.Surface) Superficie en la que se dibujan los botones del menú.
    - pos_mouse: (tuple) Posición actual del mouse (x, y), usada para detectar el hover sobre los botones.

    ¿Qué retorna?
    No retorna ningún valor, pero dibuja los botones del menú en la pantalla.
    '''
    # Dibujar el botón "Jugar"
    dibujar_texto_con_boton_transparente(
        pantalla, 
        "Jugar",  # Texto del botón
        300, 100, 200, 50,  # Posición (x, y) y tamaño (ancho, alto)
        CYAN2, RED1,  # Colores para el estado normal y hover
        pos_mouse  # Posición del mouse para detectar hover
    )

    # Dibujar el botón "Ver top mundiales"
    dibujar_texto_con_boton_transparente(
        pantalla, 
        "Ver top mundiales", 
        300, 200, 200, 50, 
        CYAN2, RED1, 
        pos_mouse
    )

    # Dibujar el botón "Salir"
    dibujar_texto_con_boton_transparente(
        pantalla, 
        "Salir", 
        625, 550, 200, 50, 
        CYAN2, RED1, 
        pos_mouse
    )

    # Dibujar el botón "Cargar preguntas"
    dibujar_texto_con_boton_transparente(
        pantalla, 
        "Cargar preguntas", 
        300, 300, 200, 50, 
        CYAN2, RED1, 
        pos_mouse
    )
