import pygame
from funciones import *
from colores import *
from configuraciones import *

def dibujar_menu_botones(pantalla, pos_mouse):
    '''
    Plantilla Documentacion
    ¿Para que sirve? Para mostar un menu en la pantalla
    ¿Que parametro acepta?
    -pantalla : superficie en donde se va a mostrar la pantalla
    -pos_mouse : la posicion de mouse 
    ¿Que Retorna?
    xxxx
    '''
    dibujar_texto_con_boton_transparente(pantalla, "Jugar", 300, 100, 200, 50, CYAN2, RED1, pos_mouse)
    dibujar_texto_con_boton_transparente(pantalla, "Ver top mundiales", 300, 200, 200, 50, CYAN2, RED1, pos_mouse)
    dibujar_texto_con_boton_transparente(pantalla, "Salir", 625, 550, 200, 50, CYAN2, RED1, pos_mouse)
    dibujar_texto_con_boton_transparente(pantalla, "Cargar preguntas", 300, 300, 200, 50, CYAN2, RED1, pos_mouse)