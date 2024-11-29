import pygame
from funciones import *
from colores import *
from configuraciones import *
from funciones_preguntas import *
from ruleta import *
import time

# Bandera para controlar el clic en el juego

def dibujar_botones_pantalla_juego(pantalla, pos_mouse):  
    '''
    Plantilla Documentacion
    ¿Para qué sirve?
    Esta función dibuja la pantalla de juego y coloca un botón para volver al menú principal. El botón se puede interactuar con el mouse para regresar al menú cuando se haga clic sobre él.

    ¿Qué parámetro acepta?
    - pantalla: (Surface) Superficie de la ventana en la que se dibujan los elementos.
    - pos_mouse: (tuple) Posición actual del mouse, utilizada para detectar si el mouse está sobre el botón.

    ¿Qué retorna?
    - boton_menu: (Rect) Un objeto de tipo `Rect` que representa el área del botón para volver al menú principal. Este valor se utiliza para verificar si el botón ha sido presionado.
    '''
    # Establecer título de la ventana del juego
    pygame.display.set_caption("A jugar preguntados!")

    # Obtener la posición del mouse
    pos_mouse = pygame.mouse.get_pos()  # x, y

    # Dibujar el botón "Volver al Menu"
    boton_volver_menu_juego = dibujar_texto_con_boton_transparente(
        pantalla, 
        "Volver al Menu", 
        620, 550, 200, 50,  # Posición y tamaño del botón
        WHEAT1, RED1,  # Colores para el estado normal y hover
        pos_mouse  # Posición del mouse para detección de hover
    )
    
    # Actualizar la pantalla
    pygame.display.flip()

    # Retornar el botón de "Volver al Menu"
    return boton_volver_menu_juego



def mostrar_preguntas(pantalla, preguntas, pregunta_actual_index, pos_mouse, vidas):
    '''
    ¿Para qué sirve?
    Muestra la pregunta actual, las posibles respuestas y los botones para responder.
    
    ¿Qué parámetro acepta?
    - pantalla: (pygame.Surface) La superficie donde se dibujan los elementos.
    - preguntas: (list) Lista con las preguntas y respuestas.
    - pregunta_actual_index: (int) El índice de la pregunta actual.
    - pos_mouse: (tuple) La posición actual del mouse para detectar hover en los botones.
    - vidas: (int) El número de vidas restantes.
    
    ¿Qué retorna?
    - botones: (list) Lista de rectángulos de los botones de respuesta.
    - pregunta_actual_index: (int) El índice de la siguiente pregunta.
    - respuestas: (list) Lista de respuestas disponibles para la pregunta actual.
    - vidas_visual: (pygame.Surface) La superficie de vidas visuales.
    '''
    # Validar si el índice de la pregunta es mayor que el número de preguntas
    if pregunta_actual_index >= len(preguntas):
        pregunta_actual_index = 0  # Volver al principio si se superó el número de preguntas

    pregunta_actual = preguntas[pregunta_actual_index]  # Obtener la pregunta actual
    pregunta = pregunta_actual[0]  # La pregunta en sí
    respuestas = pregunta_actual[1:]  # Las respuestas posibles (todos los elementos después de la primera)

    # Posiciones para cada botón de respuesta
    posiciones = [
        (120, 440),  # Respuesta 1
        (100, 540),  # Respuesta 2
        (540, 450),  # Respuesta 3
        (520, 550),  # Respuesta 4
    ]

    botones = []  # Lista para almacenar los rectángulos de los botones

    # Dibujar la pregunta
    ancho_boton_pregunta = 400
    alto_boton_pregunta = 50
    x_pantalla_pregunta = 600
    y_pantalla_pregunta = 300

    x_centrado = (x_pantalla_pregunta - ancho_boton_pregunta)
    y_centrado = (y_pantalla_pregunta - alto_boton_pregunta)

    # Dibujar la pregunta en un botón transparente
    dibujar_texto_con_boton_transparente(
        pantalla, 
        pregunta, 
        x_centrado, y_centrado, 
        ancho_boton_pregunta, alto_boton_pregunta, 
        GRAY, GREEN, pos_mouse
    )

    # Dibujar las respuestas y guardar sus rectángulos
    for i in range(len(respuestas)):  # Iterar sobre las respuestas
        x, y = posiciones[i]
        # Crear el rectángulo para cada botón de respuesta
        boton_rect = dibujar_texto_con_boton_transparente(
            pantalla, 
            respuestas[i], 
            x, y, 
            200, 50, 
            GRAY, RED1, 
            pos_mouse
        )
        botones.append(boton_rect)  # Guardar el rectángulo de cada botón
        
    # Dibujar las vidas visuales en la pantalla
    vidas_visual = dibujar_vidas(pantalla, vidas)

    # Retornar los botones, índice de la pregunta actual, respuestas y las vidas visuales
    return botones, pregunta_actual_index, respuestas, vidas_visual


def temporizador_descendente(pantalla, segundos, pos_mouse):
    '''
    ¿Para qué sirve?
    Función para mostrar un temporizador descendente en la pantalla.
    
    ¿Qué parámetro acepta?
    - pantalla: (pygame.Surface) La superficie donde se dibuja el temporizador.
    - segundos: (int) El tiempo en segundos para el temporizador.
    - pos_mouse: (tuple) La posición del mouse para detectar hover en el temporizador (opcional).
    
    ¿Qué retorna?
    - segundos_pantalla: (pygame.Surface) La superficie que muestra el temporizador actualizado.
    '''
    while segundos > 0:
        time.sleep(1)  # Espera 1 segundo
        segundos -= 1  # Decrementa el tiempo del temporizador
        
        # Mostrar el tiempo restante en la pantalla
        segundos_pantalla = dibujar_texto_con_boton_transparente(
            pantalla, 
            segundos, 
            0, 0, 
            30, 30, 
            RED1, BLACK, 
            pos_mouse
        )
        
    # Retornar la superficie del temporizador
    return segundos_pantalla
