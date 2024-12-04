import pygame

from colores import *
from configuraciones import *
from funciones_eventos import *
from funciones_dibujar import *


# Esta funcion dibuja los botones para cada campo de la pregunta
def dibujar_botones_agregar_pregunta(pantalla, pos_mouse, cuadro_activo, cuadros_texto):
    '''
    Plantilla Documentacion
    ¿Para qua sirve? 
    Esta funcion dibuja los botones y cuadros de texto en la pantalla, permitiendo al usuario agregar una pregunta y sus respuestas. Los cuadros de texto permiten que el usuario ingrese una pregunta y cuatro respuestas.

    ¿Qua parametros acepta?
    - pantalla: (Surface) La superficie de la ventana de Pygame donde se dibujaran los elementos.
    - pos_mouse: (tuple) Las coordenadas (x, y) actuales del raton.
    - cuadro_activo: (int) El indice del cuadro de texto activo (para resaltar el cuadro que esta siendo editado).
    - cuadros_texto: (list) Una lista de cinco cadenas de texto, que representan los valores introducidos en los cuadros de texto (una pregunta y cuatro respuestas).

    ¿Qua retorna?
    - boton_volver_menu: (Rect) El boton de "Volver al Menu" para que el usuario pueda regresar al menu principal.
    '''

    # Definir botones
    boton_volver_menu = dibujar_texto_con_boton_transparente(pantalla, "Volver al Menu", 620, 550, 200, 50, WHEAT1, RED1, pos_mouse)  # Dibuja el boton "Volver al Menu"
    
    # Dibujar los cuadros de texto
    for i in range(5):
        x = (800 - CUADRO_ANCHO) // 2  # Calcula la posicion X centrada de los cuadros de texto
        y = 200 + i * (CUADRO_ALTO + 10)  # Calcula la posicion Y de cada cuadro de texto (espaciados)

        # Determinar color de fondo dependiendo 
        # de si el cuadro es activo o no
        if i == cuadro_activo:
            color = BLUE  # Color azul si el cuadro esta activo
        else:
            color = GRAY  # Color gris si el cuadro no esta activo

        pygame.draw.rect(pantalla, color, (x, y, CUADRO_ANCHO, CUADRO_ALTO))  # Dibuja el rectangulo del cuadro de texto

        # Mostrar texto de fondo si el cuadro esta vacio
        if cuadros_texto[i] == "":
            if i == 0:
                mostrar_texto(pantalla, "PREGUNTA",x + 10, y + 5, color=GRAY)  # Muestra el texto "PREGUNTA" en el primer cuadro
            else:
                mostrar_texto(pantalla, f"RESPUESTA {i}", x + 10, y + 5, color=GRAY)  # Muestra el texto "RESPUESTA i" en los otros cuadros
        else:
            mostrar_texto(pantalla,cuadros_texto[i], x + 10, y + 5)  # Muestra el texto introducido por el usuario en el cuadro
    pygame.display.flip()  # Actualiza la pantalla

    # Retornar el boton de volver al menu
    return boton_volver_menu
