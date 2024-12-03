from pathlib import Path  # Para trabajar con rutas de archivos
import pygame  # Librería principal para crear juegos en 2D
import csv  # Para trabajar con archivos CSV
from colores import *  # Colores definidos en otro archivo
from configuraciones import *  # Configuraciones del juego
from funciones_guardar import *

# Función para manejar los eventos de teclado en los cuadros de texto
def eventos_carg_preguntas(csv, evento, cuadro_activo, cuadros_texto):
    ''' 
    ¿Para qué sirve?
    Gestiona los eventos de teclado para escribir en los cuadros de texto o cambiar de cuadro. 
    Dependiendo del archivo CSV proporcionado, los datos introducidos pueden ser preguntas y respuestas o nombre y puntuación.
    
    ¿Qué parámetros acepta?
    - csv: (str) Ruta del archivo CSV donde se guardarán los textos introducidos. Puede ser para preguntas y respuestas o para el ranking (nombre y puntuación).
    - evento: (pygame.event.Event) El evento generado por la acción de la tecla (por ejemplo, pulsar una tecla para escribir).
    - cuadro_activo: (int) El índice del cuadro de texto actualmente activo, de 0 a 4 (solo hay 5 cuadros de texto: una pregunta y 4 respuestas).
    - cuadros_texto: (list) Lista de cadenas de texto que representan el contenido en cada cuadro de texto.
    
    ¿Qué retorna?
    - (int, list): Devuelve una tupla con el índice del cuadro activo actualizado y la lista de textos actualizada.
    '''
    path_csv = Path(csv)  # Ruta al archivo CSV donde se guardarán los textos
    
    if evento.type == pygame.KEYDOWN:  # Si se presiona una tecla
        if cuadro_activo < 5:  # Si el cuadro activo está dentro del rango válido (hay un máximo de 5 cuadros)
            if evento.key == pygame.K_BACKSPACE:  # Si se presiona la tecla BACKSPACE
                cuadros_texto[cuadro_activo] = cuadros_texto[cuadro_activo][:-1]  # Elimina el último carácter
            elif evento.key == pygame.K_RETURN:  # Si se presiona la tecla ENTER
                if cuadro_activo < 4:  # Si no estamos en el último cuadro (cuadro 4 es el último)
                    cuadro_activo += 1  # Cambia al siguiente cuadro de texto
                else:  # Si es el último cuadro, guarda y limpia
                    guardar_textos(cuadros_texto, path_csv)  # Llamada a la función de guardar
                    cuadros_texto = [""] * 5  # Limpia los cuadros de texto
                    cuadro_activo = 0  # Reinicia el cuadro activo a 0
            else: 
                if len(cuadros_texto[cuadro_activo]) < 50:  # Añadir un límite de caracteres por cuadro
                    cuadros_texto[cuadro_activo] += evento.unicode  # Añade el carácter al cuadro activo

    return cuadro_activo, cuadros_texto  # Devuelve el índice del cuadro activo y la lista de textos actualizada

# Función para limpiar la pantalla y mostrar un fondo
def limpiar_pantalla():
    '''
    ¿Para qué sirve?
    Esta función limpia la pantalla y dibuja un fondo.
    
    ¿Qué parámetro acepta?
    - Ninguno.
    
    ¿Qué retorna?
    - None. La función solo limpia la pantalla y muestra un fondo.
    '''
    ruta_fondo = 'assets/fondo.jpg'  # Ruta de la imagen de fondo
    imagen_fondo = pygame.image.load(ruta_fondo)  # Carga la imagen de fondo
    imagen_fondo_escalar = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))  # Escala la imagen para ajustarla a la pantalla
    pygame.display.flip()  # Actualiza la pantalla