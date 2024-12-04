import pygame

from colores import *
from configuraciones import *
from funciones import *
from funciones_dibujar import *


def dibujar_menu_botones(pantalla, pos_mouse):
    '''
    ¿Para qua sirve?
    Esta funcion dibuja un menu principal en la pantalla con varias opciones de botones.

    ¿Qua parametro acepta?
    - pantalla: (pygame.Surface) Superficie en la que se dibujan los botones del menu.
    - pos_mouse: (tuple) Posicion actual del mouse (x, y), usada para detectar el hover sobre los botones.

    ¿Qua retorna?
    No retorna ningun valor, pero dibuja los botones del menu en la pantalla.
    '''
    # Dibujar el boton "Jugar"
    dibujar_texto_con_boton_transparente(
        pantalla, 
        "Jugar",  # Texto del boton
        300, 100, 200, 50,  # Posicion (x, y) y tamaño (ancho, alto)
        CYAN2, RED1,  # Colores para el estado normal y hover
        pos_mouse  # Posicion del mouse para detectar hover
    )

    # Dibujar el boton "Ver top mundiales"
    dibujar_texto_con_boton_transparente( # Llama a la funcion para dibujar un boton con texto
        pantalla, 
        "Ver top mundiales", 
        300, 200, 200, 50, 
        CYAN2, RED1, 
        pos_mouse
    )

    # Dibujar el boton "Salir"
    dibujar_texto_con_boton_transparente( # Llama a la funcion para dibujar un boton con texto
        pantalla, 
        "Salir", 
        625, 550, 200, 50, 
        CYAN2, RED1, 
        pos_mouse
    )

    # Dibujar el boton "Cargar preguntas"
    dibujar_texto_con_boton_transparente( # Llama a la funcion para dibujar un boton con texto
        pantalla, 
        "Cargar preguntas", 
        300, 300, 200, 50, 
        CYAN2, RED1, 
        pos_mouse
    )
    
    dibujar_texto_con_boton_transparente( # Llama a la funcion para dibujar un boton con texto
        pantalla, 
        "configuracion", 
        300, 400, 200, 50, 
        CYAN2, RED1, 
        pos_mouse
    )
