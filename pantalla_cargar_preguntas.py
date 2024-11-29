import pygame
from funciones import *
from colores import *
from configuraciones import *

# Esta función dibuja los botones para cada campo de la pregunta
def dibujar_botones_agregar_pregunta(pantalla, pos_mouse, cuadro_activo, cuadros_texto):
    '''
    Plantilla Documentacion
    ¿Para qué sirve? 
    Esta función dibuja los botones y cuadros de texto en la pantalla, permitiendo al usuario agregar una pregunta y sus respuestas. Los cuadros de texto permiten que el usuario ingrese una pregunta y cuatro respuestas.

    ¿Qué parámetros acepta?
    - pantalla: (Surface) La superficie de la ventana de Pygame donde se dibujarán los elementos.
    - pos_mouse: (tuple) Las coordenadas (x, y) actuales del ratón.
    - cuadro_activo: (int) El índice del cuadro de texto activo (para resaltar el cuadro que está siendo editado).
    - cuadros_texto: (list) Una lista de cinco cadenas de texto, que representan los valores introducidos en los cuadros de texto (una pregunta y cuatro respuestas).

    ¿Qué retorna?
    - boton_volver_menu: (Rect) El botón de "Volver al Menú" para que el usuario pueda regresar al menú principal.
    '''
    pygame.display.set_caption("Agregar Pregunta!")  # Establece el título de la ventana

    # Definir botones
    pos_mouse = pygame.mouse.get_pos  # Obtiene la posición del ratón
    boton_volver_menu = dibujar_texto_con_boton_transparente(pantalla, "Volver al Menu", 620, 550, 200, 50, WHEAT1, RED1, pos_mouse)  # Dibuja el botón "Volver al Menu"
    
    # Dibujar los cuadros de texto
    for i in range(5):
        x = (800 - CUADRO_ANCHO) // 2  # Calcula la posición X centrada de los cuadros de texto
        y = 200 + i * (CUADRO_ALTO + 10)  # Calcula la posición Y de cada cuadro de texto (espaciados)

        # Determinar color de fondo dependiendo de si el cuadro es activo o no
        if i == cuadro_activo:
            color = BLUE  # Color azul si el cuadro está activo
        else:
            color = GRAY  # Color gris si el cuadro no está activo

        pygame.draw.rect(pantalla, color, (x, y, CUADRO_ANCHO, CUADRO_ALTO))  # Dibuja el rectángulo del cuadro de texto

        # Mostrar texto de fondo si el cuadro está vacío
        if cuadros_texto[i] == "":
            if i == 0:
                mostrar_texto("PREGUNTA", pantalla, x + 10, y + 5, color=GRAY)  # Muestra el texto "PREGUNTA" en el primer cuadro
            else:
                mostrar_texto(f"RESPUESTA {i}", pantalla, x + 10, y + 5, color=GRAY)  # Muestra el texto "RESPUESTA i" en los otros cuadros
        else:
            mostrar_texto(cuadros_texto[i], pantalla, x + 10, y + 5)  # Muestra el texto introducido por el usuario en el cuadro
    pygame.display.flip()  # Actualiza la pantalla

    # Retornar el botón de volver al menú
    return boton_volver_menu
