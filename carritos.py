

import pygame
import random

# inicializar pygame
pygame.init()

# establecer las dimensiones de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# establecer el título de la ventana
pygame.display.set_caption("Juego de carreras")

# establecer los colores
white = (255, 255, 255)
black = (0, 0, 0)
red = "green"

# establecer la posición y tamaño del coche del jugador
player_width = 50
player_height = 80
player_x = (screen_width / 2) - (player_width / 2)
player_y = screen_height - player_height - 10

# establecer la velocidad del coche del jugador
player_speed = 10

# establecer la posición y tamaño de los obstáculos
obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 0.3

# establecer la puntuación inicial
score = 0

# establecer la fuente del texto
font = pygame.font.SysFont(None, 25)

# función para mostrar la puntuación en la pantalla
def show_score(x, y):
    score_text = font.render("Puntuación: " + str(score), True, black)
    screen.blit(score_text, (x, y))

# bucle principal del juego
game_over = False
while not game_over:

    # comprobar los eventos del teclado y del ratón
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_x += player_speed

    # mover el coche del jugador
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width

    # mover los obstáculos
    obstacle_y += obstacle_speed
    if obstacle_y > screen_height:
        obstacle_x = random.randint(0, screen_width - obstacle_width)
        obstacle_y = -obstacle_height
        score += 1

    # comprobar si el jugador ha chocado con un obstáculo
    if player_y < obstacle_y + obstacle_height:
        if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x:
            game_over = True

    # dibujar los objetos en la pantalla
    screen.fill(white)
    pygame.draw.rect(screen, red, [obstacle_x, obstacle_y, obstacle_width, obstacle_height])
    pygame.draw.rect(screen, black, [player_x, player_y, player_width, player_height])
    show_score(10, 10)

    # actualizar la pantalla
    pygame.display.update()

# cerrar pygame y salir del programa
pygame.quit()
quit()
