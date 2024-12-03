import csv
import os
import random
from pathlib import Path

# Función para guardar los textos en el archivo CSV
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
    todos_contenido = True  # Inicializa como True, se cambiará si algún cuadro está vacío
    
    # Recorre los cuadros de texto para verificar que todos tengan contenido
    for texto in cuadros_texto:
        if texto == "":  # Si algún cuadro está vacío, marca como False
            todos_contenido = False
            break  # Salir del bucle si se encuentra un cuadro vacío
    
    # Si todos los cuadros contienen texto, guarda los datos en el archivo CSV
    if todos_contenido:
        archivo_existe = path_csv.exists()  # Verifica si el archivo ya existe
        
        # Abre el archivo en modo 'append' para agregar nuevos datos sin sobrescribir
        with open(path_csv, 'a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            
            # Si el archivo no existe, escribe los encabezados
            if not archivo_existe:
                escritor.writerow(["Pregunta", "Respuesta 1", "Respuesta 2", "Respuesta 3", "Respuesta correcta"])
            
            # Escribe los textos de los cuadros en el archivo CSV
            escritor.writerow(cuadros_texto)

# Función para guardar el nombre y puntuación en un archivo CSV
def guardar_nombre_csv(nombre, puntuacion, path_csv):
    '''
    ¿Para qué sirve? 
    Guarda el nombre y la puntuación del jugador en un archivo CSV.
    
    ¿Qué parámetros acepta?
    - nombre: (str) El nombre del jugador.
    - puntuacion: (int) La puntuación del jugador.
    - path_csv: (Path) Ruta del archivo CSV donde se guardarán los datos.

    ¿Qué retorna?
    - None. Guarda el nombre y la puntuación en el archivo CSV.
    '''
    archivo_existe = path_csv.exists()  # Verifica si el archivo CSV ya existe
    
    # Abre el archivo en modo 'append' para agregar nuevos datos sin sobrescribir
    with open(path_csv, 'a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        
        # Si el archivo no existe, escribe los encabezados
        if not archivo_existe:
            escritor.writerow(["Nombre", "Puntuación"])
        
        # Escribe el nombre y la puntuación en una nueva fila
        escritor.writerow([nombre, puntuacion])

def guardar_vida_tiempo():
    pass
