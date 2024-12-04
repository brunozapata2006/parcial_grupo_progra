import pygame
from colores import *
from configuraciones import *
from funciones_eventos import *
from funciones_dibujar import *
import csv


# Esta funcion dibuja 2 botenes para configurar el tiempo y las vidas del juego

def dibujar_botones_configuraciones(pantalla, pos_mouse, cuadro_activo, cuadros_texto):
    '''
    Plantilla Documentacion
    ¿Para qua sirve? 
    Esta funcion dibuja los botones y cuadros de texto en la pantalla, permitiendo al usuario configurar el tiempo y las vidas del juego.

    ¿Qua parametros acepta?
    - pantalla: (Surface) La superficie de la ventana de Pygame donde se dibujaran los elementos.
    - pos_mouse: (tuple) Las coordenadas (x, y) actuales del raton.
    - cuadro_activo: (int) El indice del cuadro de texto activo (para resaltar el cuadro que esta siendo editado).
    - cuadros_texto: (list) Una lista de dos cadenas de texto, que representan los valores introducidos en los cuadros de texto (tiempo y vidas).

    ¿Qua retorna?
    - boton_volver_menu: (Rect) El boton de "Volver al Menu" para que el usuario pueda regresar al menu principal.
    '''
    boton_volver_menu = dibujar_texto_con_boton_transparente(pantalla, "Volver al Menu", 620, 550, 200, 50, WHEAT1, RED1, pos_mouse) # Dibujar el botón "Volver al Menú"
    boton_guardar = dibujar_texto_con_boton_transparente(pantalla, "Guardar", 620, 450, 200, 50, WHEAT1, RED1, pos_mouse)  # Dibujar el botón "Guardar"
    
    for i in range(3):
        x = (800 - CUADRO_ANCHO) // 2 # Centrar el cuadro de texto
        y = 200 + i * (CUADRO_ALTO + 10) # Espaciar verticalmente los cuadros de texto
        color = WHEAT2 if i == cuadro_activo else GOLDENROD1 # Resaltar el cuadro activo
        pygame.draw.rect(pantalla, color, (x, y, CUADRO_ANCHO, CUADRO_ALTO)) # Dibujar el cuadro de texto
        
        if cuadros_texto[i] == "":
            texto = ["vidas", "tiempo(en seg)", "puntos"][i] # Texto predeterminado para cada cuadro
            mostrar_texto(pantalla, texto, x + 10, y + 5, color=GRAY, font_size=25) # Mostrar el texto predeterminado
        else:
            mostrar_texto(pantalla, cuadros_texto[i], x + 10, y + 5) # Mostrar el texto introducido en el cuadro de texto
    
    return boton_volver_menu, boton_guardar


def guardar_cfg(vida, tiempo, punto, csv_path):
    '''
    Plantilla Documentacion
    ¿Para qua sirve?
    Guarda los valores de vida, tiempo y punto en un archivo CSV.
    
    ¿Qua parametros acepta?
    - vida: (str) La cantidad de vidas que se guardarán en el archivo.
    - tiempo: (str) El tiempo que se guardará en el archivo.
    - punto: (str) La cantidad de puntos que se guardarán en el archivo.
    - csv_path: (str) La ruta del archivo CSV donde se guardarán los valores.
    
    ¿Qua retorna?
    No retorna ningun valor, pero guarda los valores en el archivo CSV especificado.
    '''
    with open(csv_path, mode='w', newline='', encoding='utf-8') as archivo: # Modo escritura
        escritor = csv.writer(archivo) # Crear objeto escritor
        escritor.writerow(["vida", "tiempo(en seg)", "punto"]) # Escribir la cabecera
        escritor.writerow([vida, tiempo, punto]) # Escribir los valores de vida, tiempo y punto

def eventos_configuracion(evento, cuadro_activo, cuadros_texto):
    '''
    Plantilla Documentacion
    ¿Para qué sirve?
    Gestiona los eventos de teclado para escribir en los cuadros de texto o cambiar de cuadro. Dependiendo del archivo CSV proporcionado, 
    los datos introducidos pueden ser preguntas y respuestas o nombre y puntuación.
    
    ¿Qué parámetros acepta?
    - evento: (pygame.event.Event) El evento generado por la acción de la tecla (por ejemplo, pulsar una tecla para escribir).
    - cuadro_activo: (int) El índice del cuadro de texto actualmente activo, de 0 a 3 (solo hay 4 cuadros de texto: vidas, tiempo y puntos).
    - cuadros_texto: (list) Lista de cadenas de texto que representan el contenido en cada cuadro de texto.
    
    ¿Qué retorna?
    - (int, list): Devuelve una tupla con el índice del cuadro activo actualizado y la lista de textos actualizada.
    
    '''
    if evento.type == pygame.KEYDOWN: # Si se presiona una tecla
        if cuadro_activo < 3: # Solo se permite escribir en los cuadros 0, 1 y 2
            if evento.key == pygame.K_BACKSPACE: # Si se presiona la tecla BACKSPACE
                cuadros_texto[cuadro_activo] = cuadros_texto[cuadro_activo][:-1] # Elimina el último carácter
            elif evento.key == pygame.K_RETURN: # Si se presiona la tecla ENTER
                cuadro_activo = (cuadro_activo + 1) % 3 # Cambia al siguiente cuadro de texto
            else:
                cuadros_texto[cuadro_activo] += evento.unicode # Añade el carácter al cuadro activo
    return cuadro_activo, cuadros_texto

def pantalla_configuraciones(pantalla, pos_mouse, csv_path):
    '''
    Plantilla Documentacion
    ¿Para qué sirve?
    Esta función maneja la pantalla de configuraciones del juego, permitiendo al usuario modificar la cantidad de vidas, tiempo y puntos.
    
    ¿Qué parámetros acepta?
    - pantalla: (Surface) La superficie de la ventana de Pygame donde se dibujarán los elementos.
    - pos_mouse: (tuple) Las coordenadas (x, y) actuales del ratón.
    - csv_path: (str) La ruta del archivo CSV donde se guardarán los valores de vida, tiempo y punto.
    
    ¿Qué retorna?
    - str: Retorna "menu" si el usuario decide volver al menú principal.
    
    '''
    cuadros_texto = ["", "", ""] # Inicializar los cuadros de texto
    cuadro_activo = 0 # Inicializar el cuadro activo
    while True:
        for evento in pygame.event.get(): # Iterar sobre los eventos de Pygame
            if evento.type == pygame.QUIT: #    Si se cierra la ventana
                pygame.quit() # Salir de Pygame
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN: # Si se presiona un botón del ratón
                pos = pygame.mouse.get_pos() # Obtener la posición del ratón
                if boton_volver_menu.collidepoint(pos): # Si se hace clic en el botón "Volver al Menú"
                    return "menu"
                elif boton_guardar.collidepoint(pos): # Si se hace clic en el botón "Guardar"
                    guardar_cfg(cuadros_texto[0], cuadros_texto[1], cuadros_texto[2], csv_path) # Guardar la configuración
                    pantalla.fill(BLACK)  # Asegúrate de redibujar la pantalla después de guardar
            cuadro_activo, cuadros_texto = eventos_configuracion(evento, cuadro_activo, cuadros_texto) # Gestionar eventos de teclado
        
        pantalla.blit(imagen_fondo_escalar, (0, 0))  # Redibuja el fondo
        boton_volver_menu, boton_guardar = dibujar_botones_configuraciones(pantalla, pos_mouse, cuadro_activo, cuadros_texto) # Dibujar botones y cuadros de texto
        pygame.display.flip()
