import pygame
from funciones import *
from colores import *
from configuraciones import *

def dibujar_botones_config(pantalla, pos_mouse):
    
    pygame.display.set_caption("Configuracion!")
    
    boton_volver_menu = dibujar_texto_con_boton_transparente(pantalla, "Volver al Menu", 620, 550, 200, 50, WHEAT1, RED1, pos_mouse)  # Dibuja el boton "Volver al Menu"
    
    pygame.display.flip()
    
    return boton_volver_menu