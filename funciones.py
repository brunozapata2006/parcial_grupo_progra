from pathlib import Path  # Para trabajar con rutas de archivos

import pygame  # Libreria principal para crear juegos en 2D
from pygame import surface  # Importa la clase 'surface' de pygame para trabajar con superficies (pantallas)

from colores import *  # Importa los colores definidos en otro archivo
from configuraciones import *  # Importa configuraciones (posiblemente con mas valores de colores, configuraciones de juego, etc.)

import csv

def guardar_textos(cuadros_texto, path_csv):
    '''
    ¿Para qué sirve? 
    Esta función guarda los textos introducidos en una lista en un archivo CSV. Los textos se guardan solo si todos los cuadros contienen contenido (ningún cuadro vacío).

    ¿Qué parámetros acepta?
    - cuadros_texto: (list) Lista que contiene los textos que se guardarán en el archivo CSV. Debe contener una pregunta y cuatro respuestas.
    - path_csv: (Path) Ruta del archivo CSV donde se guardarán los textos.

    ¿Qué retorna?
    - None. La función guarda los textos en el archivo CSV si todos los cuadros tienen contenido y no retorna ningún valor.
    '''
    todos_contenido = True  # Se inicializa una variable para verificar si todos los cuadros tienen contenido
    for texto in cuadros_texto:  # Recorre cada texto en la lista
        if texto == "":  # Si algún texto está vacío, marca como False
            todos_contenido = False
            break  # Sale del bucle si encuentra un cuadro vacío

    if todos_contenido:  # Si todos los cuadros tienen texto
        archivo_existe = path_csv.exists()  # Verifica si el archivo ya existe

        with open(path_csv, 'a', newline='', encoding='utf-8') as archivo:  # Abre el archivo en modo de append
            if not archivo_existe:  # Si el archivo no existe, escribe la cabecera
                archivo.write("Pregunta,Respuesta 1,Respuesta 2,Respuesta 3,Respuesta correcta\n")

            # Escribe los textos de los cuadros en el CSV, separados por comas
            archivo.write(f"{cuadros_texto[0]},{cuadros_texto[1]},{cuadros_texto[2]},{cuadros_texto[3]},{cuadros_texto[4]}\n")
            
# Función para guardar nombre y puntuación en un archivo CSV
def guardar_nombre_csv(nombre, puntuacion, path_csv):
    '''
    ¿Para qué sirve? 
    Esta función guarda el nombre y la puntuación del jugador en un archivo CSV.

    ¿Qué parámetros acepta?
    - nombre: (str) El nombre del jugador.
    - puntuacion: (int) La puntuación del jugador.
    - path_csv: (Path) Ruta del archivo CSV donde se guardarán los datos.

    ¿Qué retorna?
    - None. La función guarda el nombre y la puntuación en el archivo CSV si ambos valores son válidos.
    '''
    archivo_existe = path_csv.exists()  # Verifica si el archivo ya existe
    
    with open(path_csv, 'a', newline='', encoding='utf-8') as archivo:  # Abre el archivo en modo de append
        escritor = csv.writer(archivo)
        if not archivo_existe:  # Si el archivo no existe, escribe la cabecera
            escritor.writerow(["Nombre", "Puntuación"])
        escritor.writerow([nombre, puntuacion])  # Escribe el nombre y la puntuación en una nueva fila

def eventos_carg_preguntas(csv, evento, cuadro_activo, cuadros_texto):
    ''' 
    ¿Para qué sirve?
    Esta función gestiona los eventos de teclado para escribir en los cuadros de texto o cambiar de cuadro. 
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

# Funcion para limpiar la pantalla y mostrar un fondo
def limpiar_pantalla():
    '''
    ¿Para qua sirve?
    Esta funcion limpia la pantalla y dibuja un fondo.
    
    ¿Qua parametro acepta?
    - Ninguno.
    
    ¿Qua retorna?
    - None. La funcion solo limpia la pantalla y muestra un fondo.
    '''
    ruta_fondo = 'assets/fondo.jpg'  # Ruta de la imagen de fondo
    imagen_fondo = pygame.image.load(ruta_fondo)  # Carga la imagen de fondo
    imagen_fondo_escalar = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))  # Escala la imagen para ajustarla a la pantalla
    pygame.display.flip()  # Actualiza la pantalla
