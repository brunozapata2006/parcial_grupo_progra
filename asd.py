import pygame
from pathlib import Path
import time

# Constantes
CUADRO_ALTO = 40  # Altura de cada cuadro de texto
CUADRO_ANCHO = 500  # Ancho de los cuadros de texto
BLUE = (0, 0, 255)  # Azul
GRAY = (169, 169, 169)  # Gris
BLACK = (0, 0, 0)  # Negro
WHITE = (255, 255, 255)  # Blanco
ANCHO, ALTO = 800, 600  # Resolución de la ventana

# Configuración de la pantalla y fondo
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)
ruta_fondo = "assets/fondo.jpg"  # Cambia esto al fondo correcto
imagen_fondo = pygame.image.load(ruta_fondo)
imagen_fondo_escalar = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))

# Variables globales
cuadros_texto = ["", "", "", "", ""]  # Los 5 cuadros de texto vacíos
cuadro_activo = 0  # El primer cuadro es el activo
reloj = pygame.time.Clock()

path_csv = Path('preguntas_cargadas.csv')

# Función para mostrar texto
def mostrar_texto(texto, superficie, x, y, color=BLACK, font_size=30):
    fuente = pygame.font.Font(None, font_size)
    texto_renderizado = fuente.render(texto, True, color)
    superficie.blit(texto_renderizado, (x, y))

# Función para guardar en el archivo CSV
def guardar_textos(textos_guardados, path_csv):
    todos_contenido = True
    for texto in textos_guardados:
        if texto == "":
            todos_contenido = False
            break  # Salimos del bucle en cuanto encontramos un cuadro vacío

    if todos_contenido:
        archivo_existe = path_csv.exists()

        with open(path_csv, 'a', newline='', encoding='utf-8') as archivo:
            if not archivo_existe:
                archivo.write("Pregunta,Respuesta 1,Respuesta 2,Respuesta 3,Respuesta 4\n")
            
            archivo.write(",".join(textos_guardados) + "\n")

# Función para gestionar la entrada de texto
def gestionar_eventos_entrada(evento, cuadro_activo, cuadros_texto):
    if evento.type == pygame.KEYDOWN:
        if cuadro_activo < 5:
            if evento.key == pygame.K_BACKSPACE:  # Borrar un carácter
                cuadros_texto[cuadro_activo] = cuadros_texto[cuadro_activo][:-1]
            elif evento.key == pygame.K_RETURN:  # Cambiar de cuadro activo
                if cuadro_activo < 4:
                    cuadro_activo += 1
                else:
                    guardar_textos(cuadros_texto, path_csv)  # Guardar los datos en el CSV
                    cuadros_texto = ["", "", "", "", ""]  # Limpiar los cuadros de texto
                    cuadro_activo = 0  # Reiniciar el cuadro activo a 0
            else:  # Añadir un carácter al cuadro activo
                cuadros_texto[cuadro_activo] += evento.unicode
    return cuadro_activo, cuadros_texto

# Función para dibujar el botón "Salir" en la pantalla de agregar preguntas
def dibujar_boton_salir(surface):
    color_boton = BLUE
    x, y = 600, 550
    ancho, alto = 160, 40
    pygame.draw.rect(surface, color_boton, (x, y, ancho, alto))
    mostrar_texto("SALIR", surface, x + 40, y + 5, color=WHITE, font_size=25)
    return pygame.Rect(x, y, ancho, alto)  # Devolver el rectángulo del botón

# Bucle principal
def main():
    global cuadro_activo, cuadros_texto
    jugar = True
    estado = "menu"  # Puede ser "menu", "agregar preguntas", etc.

    while jugar:
        pos_mouse = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugar = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = evento.pos
                if estado == "agregar preguntas":
                    # Verificar si se hizo clic en el botón "Salir"
                    boton_salir = dibujar_boton_salir(pantalla)
                    if boton_salir.collidepoint(pos):
                        estado = "menu"  # Regresar al menú principal

        # Gestionar la entrada de texto
        if estado == "agregar preguntas":
            cuadro_activo, cuadros_texto = gestionar_eventos_entrada(evento, cuadro_activo, cuadros_texto)

            # Redibujar fondo de la pantalla
            pantalla.blit(imagen_fondo_escalar, (0, 0))

            # Dibujar cuadros de texto
            for i in range(5):
                x = (ANCHO - CUADRO_ANCHO) // 2
                y = 200 + i * (CUADRO_ALTO + 10)

                color = BLUE if i == cuadro_activo else GRAY
                pygame.draw.rect(pantalla, color, (x, y, CUADRO_ANCHO, CUADRO_ALTO))

                # Mostrar texto de fondo si el cuadro está vacío
                if cuadros_texto[i] == "":
                    if i == 0:
                        mostrar_texto("PREGUNTA", pantalla, x + 10, y + 5, color=GRAY)
                    else:
                        mostrar_texto(f"RESPUESTA {i}", pantalla, x + 10, y + 5, color=GRAY)
                else:
                    mostrar_texto(cuadros_texto[i], pantalla, x + 10, y + 5)

            # Dibujar el botón "Salir"
            dibujar_boton_salir(pantalla)

        pygame.display.flip()
        reloj.tick(30)

    pygame.quit()

# Ejecutar el juego
if __name__ == "__main__":
    main()
