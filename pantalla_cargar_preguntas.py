import pygame
from funciones import *
from colores import *
from configuraciones import *

# Esta función dibuja los botones para cada campo de la pregunta
def dibujar_botones_agregar_pregunta(pantalla, pos_mouse, cuadro_activo, cuadros_texto):
    '''
    Dibuja los botones para que el usuario pueda agregar la pregunta y respuestas.
    '''
    pygame.display.set_caption("Agregar Pregunta!")

    # Definir botones
    pos_mouse = pygame.mouse.get_pos
    boton_volver_menu = dibujar_texto_con_boton_transparente(pantalla, "Volver al Menu", 620, 550, 200, 50, WHEAT1, RED1, pos_mouse)
    
            # Dibujar los cuadros de texto
    for i in range(5):
        x = (800 - CUADRO_ANCHO) // 2  # Posición X de los cuadros de texto
        y = 200 + i * (CUADRO_ALTO + 10)  # Posición Y de los cuadros de texto

        # Determinar color de fondo dependiendo de si el cuadro es activo o no
        if i == cuadro_activo:
            color = BLUE  # Cuadro activo en azul
        else:
            color = GRAY  # Cuadro no activo en gris

        pygame.draw.rect(pantalla, color, (x, y, CUADRO_ANCHO, CUADRO_ALTO))  # Dibuja el rectángulo del cuadro

        # Mostrar texto de fondo si el cuadro está vacío
        if cuadros_texto[i] == "":
            if i == 0:
                mostrar_texto("PREGUNTA", pantalla, x + 10, y + 5, color=GRAY)  # Muestra "PREGUNTA" en el primer cuadro
            else:
                mostrar_texto(f"RESPUESTA {i}", pantalla, x + 10, y + 5, color=GRAY)  # Muestra "RESPUESTA i" en los otros cuadros
        else:
            mostrar_texto(cuadros_texto[i], pantalla, x + 10, y + 5)  # Muestra el texto introducido
    pygame.display.flip()

    # Retornar el boton de volver menu
    return boton_volver_menu
