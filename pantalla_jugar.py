import pygame
from funciones import *
from colores import *
from configuraciones import *
from funciones_preguntas import *
from ruleta import *

def dibujar_botones_pantalla_juego(pantalla, pos_mouse):  
    '''
    Plantilla Documentacion
    ¿Para que sirve? Dibuja uma pantalla que muestra las preguntas para poder jugar
    ¿Que parametro acepta?
    -None
    ¿Que Retorna?
    -boton_menu : un boton con colision que devuele al menu principal
    '''
    pygame.display.set_caption("A jugar preguntados!")
    
    pos_mouse = pygame.mouse.get_pos                                           #x   #y
    boton_volver_menu_juego = dibujar_texto_con_boton_transparente(pantalla, "Volver al Menu", 620, 550, 200, 50, WHEAT1, RED1, pos_mouse)
    
    pygame.display.flip()
    
    return boton_volver_menu_juego

def mostrar_preguntas(pantalla, preguntas, pregunta_actual_index):
    # Obtener la pregunta actual
    pregunta_actual = preguntas[pregunta_actual_index]
    pregunta = pregunta_actual[0]
    respuestas = pregunta_actual[1:]

    # Posiciones predefinidas para los botones
    posiciones = [
        (120, 440),  # Respuesta 1
        (100, 540),  # Respuesta 2
        (540, 450),  # Respuesta 3
        (520, 550),  # Respuesta 4
    ]

    pos_mouse = pygame.mouse.get_pos()

    # Dibujar la pregunta
    ancho_boton_pregunta = 400
    alto_boton_pregunta = 50
    x_pantalla_pregunta = 600
    y_pantalla_pregunta = 300

    x_centrado = (x_pantalla_pregunta - ancho_boton_pregunta)
    y_centrado = (y_pantalla_pregunta - alto_boton_pregunta)
    dibujar_texto_con_boton_transparente(pantalla, pregunta, x_centrado, y_centrado, ancho_boton_pregunta, alto_boton_pregunta, GRAY, RED1, pos_mouse)

    # Dibujar las respuestas y guardar sus rectángulos

    botones = []
    for i in range(len(respuestas)):                                            #x              #y          #ancho #alto
        boton = dibujar_texto_con_boton_transparente(pantalla,respuestas[i],posiciones[i][0],posiciones[i][1], 200, 50,GRAY, RED1,pos_mouse)
        botones.append(boton)

    return botones



    