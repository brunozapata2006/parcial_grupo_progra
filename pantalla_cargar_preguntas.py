import pygame
from funciones import *
from colores import *
from configuraciones import *

# Esta función dibuja los botones y cuadros de texto para agregar una nueva pregunta y respuestas
def dibujar_botones_agregar_pregunta(pantalla, pos_mouse, cuadro_activo, cuadros_texto):
    '''
    Dibuja los botones y cuadros de texto en la pantalla para que el usuario pueda agregar una nueva pregunta y respuestas.
    '''
    # Establecer el título de la ventana
    pygame.display.set_caption("Agregar Pregunta!")

    # Definir y dibujar el botón de "Volver al Menu"
    pos_mouse = pygame.mouse.get_pos()  # Obtener la posición actual del mouse
    boton_volver_menu = dibujar_texto_con_boton_transparente(
        pantalla, 
        "Volver al Menu", 
        620, 550, 200, 50,  # Posición y tamaño del botón
        WHEAT1, RED1,  # Colores para el estado normal y hover
        pos_mouse  # Posición del mouse para detección de hover
    )

    # Dibujar los cuadros de texto para la pregunta y respuestas
    for i in range(5):
        # Calcular las posiciones X y Y para los cuadros de texto
        x = (800 - CUADRO_ANCHO) // 2  # Centrado horizontal
        y = 200 + i * (CUADRO_ALTO + 10)  # Espaciado vertical entre los cuadros

        # Determinar el color del cuadro dependiendo de si es el cuadro activo o no
        if i == cuadro_activo:
            color = BLUE  # Cuadro activo en azul
        else:
            color = GRAY  # Cuadro no activo en gris

        # Dibujar el rectángulo que representa el cuadro de texto
        pygame.draw.rect(pantalla, color, (x, y, CUADRO_ANCHO, CUADRO_ALTO))

        # Mostrar texto dentro del cuadro si está vacío
        if cuadros_texto[i] == "":
            if i == 0:
                mostrar_texto("PREGUNTA", pantalla, x + 10, y + 5, color=GRAY)  # Muestra "PREGUNTA" si es el primer cuadro
            else:
                mostrar_texto(f"RESPUESTA {i}", pantalla, x + 10, y + 5, color=GRAY)  # Muestra "RESPUESTA i" para los demás cuadros
        else:
            # Si ya hay texto en el cuadro, lo muestra
            mostrar_texto(cuadros_texto[i], pantalla, x + 10, y + 5)

    # Actualizar la pantalla para reflejar los cambios
    pygame.display.flip()

    # Retornar el botón de "Volver al Menu" para manejar la interacción
    return boton_volver_menu
