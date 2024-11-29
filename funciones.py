from colores import *  # Importa los colores definidos en otro archivo
import pygame  # Librería principal para crear juegos en 2D
from pathlib import Path  # Para trabajar con rutas de archivos
from configuraciones import *  # Importa configuraciones (posiblemente con más valores de colores, configuraciones de juego, etc.)
from pygame import surface  # Importa la clase 'surface' de pygame para trabajar con superficies (pantallas)

# Función para mostrar texto en la pantalla
def mostrar_texto(texto, superficie, x, y, color=BLACK, font_size=30):
    ''' 
    ¿Para qué sirve?
    Esta función permite mostrar un texto en una superficie de Pygame en una posición específica.

    ¿Qué parámetro acepta?
    - texto: (str) El texto que se va a mostrar en la pantalla.
    - superficie: (pygame.Surface) La superficie sobre la cual se dibuja el texto.
    - x: (int) La posición en el eje X donde se dibujará el texto.
    - y: (int) La posición en el eje Y donde se dibujará el texto.
    - color: (tuple) El color del texto. Por defecto es BLACK.
    - font_size: (int) El tamaño de la fuente del texto. Por defecto es 30.

    ¿Qué retorna?
    - None. La función solo dibuja el texto en la pantalla sin devolver nada.
    '''
    fuente = pygame.font.Font(None, font_size)  # Crea un objeto fuente con el tamaño especificado
    texto_renderizado = fuente.render(texto, True, color)  # Renderiza el texto con la fuente y el color
    superficie.blit(texto_renderizado, (x, y))  # Dibuja el texto en la superficie en la posición (x, y)
    

# Función para guardar los textos introducidos en un archivo CSV
def guardar_textos(textos_guardados, path_csv):
    ''' 
    ¿Para qué sirve?
    Esta función guarda una lista de textos en un archivo CSV, añadiendo una fila al archivo si es necesario.

    ¿Qué parámetro acepta?
    - textos_guardados: (list) Lista de textos que se guardarán en el archivo CSV.
    - path_csv: (Path) Ruta al archivo CSV donde se guardarán los textos.

    ¿Qué retorna?
    - None. La función guarda los textos en el archivo CSV y no retorna ningún valor.
    '''
    todos_contenido = True  # Inicializa un flag para verificar si todos los cuadros contienen texto
    for texto in textos_guardados:
        if texto == "":  # Si algún cuadro está vacío, se marca como 'no todo contenido'
            todos_contenido = False
            break  # Salimos del bucle en cuanto encontramos un cuadro vacío

    if todos_contenido:  # Si todos los cuadros contienen texto
        archivo_existe = path_csv.exists()  # Verifica si el archivo CSV ya existe

        with open(path_csv, 'a', newline='', encoding='utf-8') as archivo:  # Abre el archivo en modo de append
            if not archivo_existe:
                archivo.write("Pregunta,Respuesta 1,Respuesta 2,Respuesta 3,Respuesta correcta\n")  # Escribe la cabecera si el archivo es nuevo
            
            archivo.write(",".join(textos_guardados) + "\n")  # Escribe los textos guardados como una fila en el CSV

# Función para gestionar los eventos de entrada de texto (por ejemplo, teclas presionadas)
def gestionar_eventos_entrada(evento, cuadro_activo, cuadros_texto):
    ''' 
    ¿Para quo sirve?
    Esta funcion gestiona los eventos de teclado para escribir en los cuadros de texto o cambiar de cuadro.

    ¿Qué parámetro acepta?
    - evento: (pygame.event.Event) El evento generado por las teclas del teclado (escribir por ejemplo)
    - cuadro_activo: (int) El índice del cuadro de texto actualmente activo (de 0 a 4, siendo 0 la pregunta)
    - cuadros_texto: (list) Lista de cadenas que representan el texto en cada cuadro.

    ¿Qué retorna?
    - cuadro_activo: (int) El indice actualizado del cuadro de texto activo.
    - cuadros_texto: (list) La lista actualizada con el texto introducido.
    '''
    path_csv = Path('preguntas_cargadas.csv')  # Ruta al archivo CSV donde se guardarán los textos
    
    if evento.type == pygame.KEYDOWN:  # Si se presiona una tecla
        if cuadro_activo < 5:  # Si el cuadro activo está dentro del rango válido
            if evento.key == pygame.K_BACKSPACE:  # Si se presiona la tecla BACKSPACE
                cuadros_texto[cuadro_activo] = cuadros_texto[cuadro_activo][:-1]  # Elimina el último carácter
            elif evento.key == pygame.K_RETURN:  # Si se presiona la tecla ENTER
                if cuadro_activo < 4:  # Si no estamos en el último cuadro
                    cuadro_activo += 1  # Cambia al siguiente cuadro de texto
                else:  # Si es el último cuadro, guarda y limpia
                    guardar_textos(cuadros_texto, path_csv)  # Guarda los textos en el CSV
                    cuadros_texto = ["", "", "", "", ""]  # Limpia los cuadros de texto
                    cuadro_activo = 0  # Reinicia el cuadro activo a 0
            else: 
                if len(cuadros_texto[cuadro_activo]) < 50:  # Añadir un límite de caracteres por cuadro
                    cuadros_texto[cuadro_activo] += evento.unicode  # Añade el carácter al cuadro activo

    return cuadro_activo, cuadros_texto  # Devuelve el índice del cuadro activo y la lista de textos actualizada

# Función para dibujar botones con texto en un fondo transparente, con detección de hover (cuando el mouse pasa sobre ellos)
def dibujar_texto_con_boton_transparente(pantalla:surface, texto, x:int, y:int, ancho:int, alto:int, color_normal:tuple, color_hover:tuple, pos_mouse):
    ''' 
    ¿Para qué sirve?
    Dibuja un botón con texto que cambia de color cuando el mouse pasa por encima (hover).

    ¿Qué parámetro acepta?
    - pantalla: (pygame.Surface) La superficie donde se dibuja el botón.
    - texto: (str) El texto que se mostrará en el botón.
    - x: (int) La posición en el eje X de la esquina superior izquierda del botón.
    - y: (int) La posición en el eje Y de la esquina superior izquierda del botón.
    - ancho: (int) El ancho del botón.
    - alto: (int) El alto del botón.
    - color_normal: (tuple) El color del texto cuando no hay hover.
    - color_hover: (tuple) El color del texto cuando el mouse está encima del botón.
    - pos_mouse: (tuple) Las coordenadas actuales del mouse.

    ¿Qué retorna?
    - pygame.Surface: El texto renderizado, que actúa como el "botón" visual.
    '''
    pos_mouse = pygame.mouse.get_pos()  # Obtiene la posición del mouse
    color_texto = color_hover if x <= pos_mouse[0] <= x + ancho and y <= pos_mouse[1] <= y + alto else color_normal  # Cambia el color si el mouse está sobre el botón
    fuente = pygame.font.SysFont("Showcard Gothic", 30)  # Selecciona la fuente
    texto_renderizado = fuente.render(str(texto), True, color_texto)  # Renderiza el texto con el color adecuado
    texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))  # Ajusta el rectángulo para centrar el texto en el botón
    mostrar_texto = pantalla.blit(texto_renderizado, texto_rect)  # Dibuja el texto en la pantalla

    return mostrar_texto  # Retorna la superficie con el texto renderizado

# Función para limpiar la pantalla y mostrar un fondo
def limpiar_pantalla():
    ruta_fondo = 'assets/fondo.jpg'
    imagen_fondo = pygame.image.load(ruta_fondo)
    imagen_fondo_escalar = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))
    pygame.display.flip()