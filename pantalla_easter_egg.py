import pygame
from funciones import *
from colores import *
from configuraciones import *

# Funcion para mostrar una animacion o "easter egg" con imagenes de gatos
def easter_egg(pantalla, pos_mouse):
    ''' 
    Plantilla Documentacion
    ¿Para qua sirve? 
    Esta funcion muestra un "Easter Egg" en forma de imagenes de gatos en la pantalla y un boton para volver al menu. Se dibujan tres imagenes diferentes de gatos en varias posiciones y se incluye un boton interactivo para regresar al menu principal.

    ¿Qua parametros acepta?
    - pantalla: (Surface) La superficie de la ventana de Pygame donde se dibujan las imagenes y los botones.
    - pos_mouse: (tuple) Las coordenadas (x, y) actuales del raton. Es utilizado para detectar el hover sobre el boton.

    ¿Qua retorna?
    - boton_volver_menu: (Rect) El boton de "Volver al Menu", que permite al usuario regresar al menu principal cuando es presionado.
    '''
    # Establecer el titulo de la ventana
    pygame.display.set_caption("Easter egg?? o.o")

    # Cargar las imagenes de los gatos para el Easter egg
    ruta_gato_1 = 'assets/gato_easter_egg.jpg'
    imagen_gato_1 = pygame.image.load(ruta_gato_1)
    
    ruta_gato_2 = 'assets/gato_egg.jpg'
    imagen_gato_2 = pygame.image.load(ruta_gato_2)
    
    ruta_gatito = 'assets/gatito.jpg'
    imagen_gatito = pygame.image.load(ruta_gatito)

    # Dibujar las imagenes en la pantalla en diferentes posiciones
    pantalla.blit(imagen_gato_1, (0, 0))  # Gato grande en la parte superior izquierda
    pantalla.blit(imagen_gato_2, (0, 400))  # Gato 2 en la parte inferior izquierda
    pantalla.blit(imagen_gatito, (600, 0))  # Gatito pequeño en la parte superior derecha

    # Obtener la posicion del mouse para manejar la interaccion con el boton
    pos_mouse = pygame.mouse.get_pos()  # Obtiene la posicion actual del mouse

    # Dibujar el boton "Volver al Menu" con deteccion de hover (cambio de color al pasar el mouse)
    boton_volver_menu = dibujar_texto_con_boton_transparente(
        pantalla, 
        "Volver al Menu", 
        620, 550, 200, 50,  # Posicion y tamaño del boton
        WHEAT1, RED1,  # Colores para el estado normal y hover
        pos_mouse  # Posicion del mouse para deteccion de hover
    )

    # Actualizar la pantalla para reflejar los cambios
    pygame.display.flip()

    # Retornar el boton de "Volver al Menu" para manejar la interaccion
    return boton_volver_menu

