import pygame
from funciones import *
from colores import *
from configuraciones import *

def dibujar_botones_top_mundial(pantalla, pos_mouse):  

    pygame.display.set_caption("Vamos a cargar preguntas!")

    pos_mouse = pygame.mouse.get_pos                                           #x   #y   
    boton_volver_menu = dibujar_texto_con_boton_transparente(pantalla, "Volver al Menu", 620, 550, 200, 50, WHEAT1, RED1, pos_mouse)
    
    pygame.display.flip()
    
    return boton_volver_menu

def mostrar_ranking(csv):
    with open(csv, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    
    indice = lineas[0].strip().split(",")    
    datos = []
    
    for linea in lineas[1:]:
        fila = linea.strip().split(",")
        datos.append(fila)
    
    indice_ranking = indice.index("Puntuacion")

    for i in range(len(datos)):
        for j in range(len(datos) -i -1):
            pass