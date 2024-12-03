import time

import pygame

from colores import *
from configuraciones import *
from funciones import *
from funciones_dibujar import *
from funciones_preguntas import *
from ruleta import *

# Bandera para controlar el clic en el juego

def dibujar_botones_pantalla_juego(pantalla, pos_mouse):  
    '''
    Plantilla Documentacion
    ¿Para qua sirve?
    Esta funcion dibuja la pantalla de juego y coloca un boton para volver al menu principal. El boton se puede interactuar con el mouse para regresar al menu cuando se haga clic sobre al.

    ¿Qua parametro acepta?
    - pantalla: (Surface) Superficie de la ventana en la que se dibujan los elementos.
    - pos_mouse: (tuple) Posicion actual del mouse, utilizada para detectar si el mouse esta sobre el boton.

    ¿Qua retorna?
    - boton_menu: (Rect) Un objeto de tipo `Rect` que representa el area del boton para volver al menu principal. Este valor se utiliza para verificar si el boton ha sido presionado.
    '''
    # Establecer titulo de la ventana del juego
    pygame.display.set_caption("A jugar preguntados!")

    # Obtener la posicion del mouse
    pos_mouse = pygame.mouse.get_pos()  # x, y

    # Dibujar el boton "Volver al Menu"
    boton_volver_menu_juego = dibujar_texto_con_boton_transparente(
        pantalla, 
        "Volver al Menu", 
        620, 550, 200, 50,  # Posicion y tamaño del boton
        WHEAT1, RED1,  # Colores para el estado normal y hover
        pos_mouse  # Posicion del mouse para deteccion de hover
    )
    
    # Actualizar la pantalla
    pygame.display.flip()

    # Retornar el boton de "Volver al Menu"
    return boton_volver_menu_juego



def mostrar_preguntas(pantalla, preguntas, pregunta_actual_index, pos_mouse, vidas):
    '''
    ¿Para qua sirve?
    Muestra la pregunta actual, las posibles respuestas y los botones para responder.
    
    ¿Qua parametro acepta?
    - pantalla: (pygame.Surface) La superficie donde se dibujan los elementos.
    - preguntas: (list) Lista con las preguntas y respuestas.
    - pregunta_actual_index: (int) El indice de la pregunta actual.
    - pos_mouse: (tuple) La posicion actual del mouse para detectar hover en los botones.
    - vidas: (int) El numero de vidas restantes.
    
    ¿Qua retorna?
    - botones: (list) Lista de rectangulos de los botones de respuesta.
    - pregunta_actual_index: (int) El indice de la siguiente pregunta.
    - respuestas: (list) Lista de respuestas disponibles para la pregunta actual.
    - vidas_visual: (pygame.Surface) La superficie de vidas visuales.
    '''
    # Validar si el indice de la pregunta es mayor que el numero de preguntas
    if pregunta_actual_index >= len(preguntas):
        pregunta_actual_index = 0  # Volver al principio si se supero el numero de preguntas

    pregunta_actual = preguntas[pregunta_actual_index]  # Obtener la pregunta actual
    pregunta = pregunta_actual[0]  # La pregunta en si
    respuestas = pregunta_actual[1:]  # Las respuestas posibles (todos los elementos despuas de la primera)

    # Posiciones para cada boton de respuesta
    posiciones = [
        (120, 440),  # Respuesta 1
        (100, 540),  # Respuesta 2
        (540, 450),  # Respuesta 3
        (520, 550),  # Respuesta 4
    ]

    botones = []  # Lista para almacenar los rectangulos de los botones

    # Dibujar la pregunta
    ancho_boton_pregunta = 400
    alto_boton_pregunta = 50
    x_pantalla_pregunta = 600
    y_pantalla_pregunta = 300

    x_centrado = (x_pantalla_pregunta - ancho_boton_pregunta)
    y_centrado = (y_pantalla_pregunta - alto_boton_pregunta)

    # Dibujar la pregunta en un boton transparente
    dibujar_texto_con_boton_transparente(
        pantalla, 
        pregunta, 
        x_centrado, y_centrado, 
        ancho_boton_pregunta, alto_boton_pregunta, 
        GRAY, GREEN, pos_mouse
    )

    # Dibujar las respuestas y guardar sus rectangulos
    for i in range(len(respuestas)):  # Iterar sobre las respuestas
        x, y = posiciones[i]
        # Crear el rectangulo para cada boton de respuesta
        boton_rect = dibujar_texto_con_boton_transparente(
            pantalla, 
            respuestas[i], 
            x, y, 
            200, 50, 
            GRAY, RED1, 
            pos_mouse
        )
        botones.append(boton_rect)  # Guardar el rectangulo de cada boton
        
    # Dibujar las vidas visuales en la pantalla
    vidas_visual = dibujar_vidas(pantalla, vidas)

    # Retornar los botones, indice de la pregunta actual, respuestas y las vidas visuales
    return botones, pregunta_actual_index, respuestas, vidas_visual

def temporizador_descendente(pantalla, segundos, pos_mouse):
    '''
    ¿Para qua sirve?
    Funcion para mostrar un temporizador descendente en la pantalla.
    
    ¿Qua parametro acepta?
    - pantalla: (pygame.Surface) La superficie donde se dibuja el temporizador.
    - segundos: (int) El tiempo en segundos para el temporizador.
    - pos_mouse: (tuple) La posicion del mouse para detectar hover en el temporizador (opcional).
    
    ¿Qua retorna?
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


# Funcion para ingresar nombre de jugador

def ingreso_nombre(pantalla, pos_mouse, puntos):
    '''
    
    
    '''
    
    csv = Path('ranking_top.csv')
    input_box = pygame.Rect(300, 300, 140, 32)
    color_caja = RED1
    fuente = pygame.font.Font(None, 32)
    activo = False
    nombre = ''
    boton_aceptar = pygame.Rect(300, 350, 140, 32)
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(evento.pos):
                    activo = not activo
                else:
                    activo = False
            if evento.type == pygame.KEYDOWN:
                if activo:
                    if evento.key == pygame.K_RETURN:
                        print(nombre)
                        guardar_nombre_csv(nombre, puntos, csv)
                        return nombre
                    elif evento.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]
                    else: #probalo
                        nombre += evento.unicode

        pantalla.fill(WHITE)
        color_caja = RED1 if activo else BLACK
        pygame.draw.rect(pantalla, color_caja, input_box, 2)
        texto = fuente.render(nombre, True, BLACK)
        pantalla.blit(texto, (input_box.x + 5, input_box.y + 5))
        
        pygame.draw.rect(pantalla, BLACK, boton_aceptar)
        texto_aceptar = fuente.render("Aceptar", True, WHITE)
        pantalla.blit(texto_aceptar, (boton_aceptar.x + 5, boton_aceptar.y + 5))
        
        # pygame.display.flip()
        