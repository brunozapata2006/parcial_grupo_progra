# Variables globales para el estado "agregar preguntas"
preguntas_guardadas = []  # Lista de preguntas guardadas.
input_box = pygame.Rect(50, 500, 500, 40)  # Caja de texto para ingresar nuevas preguntas.
input_text = ""  # Texto actual en la caja de entrada.
input_active = False  # Estado de la caja de texto.

# Dentro del bucle principal del juego
while jugar:
    pos_mouse = pygame.mouse.get_pos()  # Obtiene la posición del mouse.

    for evento in pygame.event.get():  # Maneja eventos.
        if evento.type == pygame.QUIT:
            jugar = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = evento.pos  # Obtiene posición del clic.
            bandera_click = True

            # Verifica si se hizo clic en la caja de texto
            if input_box.collidepoint(pos):
                input_active = True
            else:
                input_active = False

            # Verifica si se hizo clic en el botón "Volver" (ya existente)
            if estado == "agregar preguntas":
                dibujar_boton_volver_preguntas = dibujar_botones_agregar_pregunta(
                    pantalla, pos_mouse, cuadro_activo, cuadros_texto
                )
                if dibujar_boton_volver_preguntas.collidepoint(pos):
                    estado = "menu"

        elif evento.type == pygame.KEYDOWN:
            if estado == "agregar preguntas" and input_active:
                if evento.key == pygame.K_RETURN:
                    if input_text.strip():
                        preguntas_guardadas.append(input_text.strip())  # Guarda la pregunta.
                        input_text = ""  # Limpia la caja de entrada.
                elif evento.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  # Borra el último carácter.
                else:
                    input_text += evento.unicode  # Agrega el carácter ingresado.

    # Estado "agregar preguntas"
    if estado == "agregar preguntas":
        pantalla.blit(imagen_fondo_escalar, (0, 0))  # Dibuja el fondo.

        # Dibuja preguntas guardadas como cuadros azules
        y_offset = 50
        for pregunta in preguntas_guardadas:
            rect = pygame.Rect(50, y_offset, 700, 40)
            pygame.draw.rect(pantalla, (0, 102, 204), rect)
            text_surface = font.render(pregunta, True, WHITE)
            pantalla.blit(text_surface, (rect.x + 10, rect.y + 10))
            y_offset += 50

        # Dibuja la caja de texto
        pygame.draw.rect(pantalla, (200, 200, 200) if input_active else WHITE, input_box, 0)
        pygame.draw.rect(pantalla, BLACK, input_box, 2)
        text_surface = font.render(input_text, True, BLACK)
        pantalla.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        # Dibuja el botón "Volver" (ya existente)
        dibujar_botones_agregar_pregunta(pantalla, pos_mouse, cuadro_activo, cuadros_texto)

    pygame.display.update()  # Actualiza la pantalla.
    bandera_click = False  # Reinicia la bandera.
    reloj.tick(30)  # Control de FPS.
