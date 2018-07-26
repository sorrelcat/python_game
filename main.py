import pygame

FPS = 30
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIN_WIDTH = 600
WIN_HEIGHT = 400

count = 0
d, x, y, t = 30, 200, 200, 1
surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

def draw_rect(color):
    surface.fill(WHITE)
    pygame.draw.rect(surface, color, (x, y, d, d))
    pygame.display.update()
    clock.tick(FPS)

pygame.init()
draw_rect(GREEN)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    draw_rect(GREEN)

    if keys[pygame.K_RIGHT]:
        x += t
    elif keys[pygame.K_LEFT]:
        x -= t
    if keys[pygame.K_UP]:
        y -= t
    elif keys[pygame.K_DOWN]:
        y += t

    if keys[pygame.K_SPACE]:
        while x >= 0 and y >= 0:
            x -= t
            y -= t
            draw_rect(LIGHT_BLUE)
        if x > 0:
            while x > 0:
                draw_rect(RED)
                x -= t
        if y > 0:
            while y > 0:
                draw_rect(BLUE)
                y -= t
        x, y = 0, 0

    x %= WIN_WIDTH
    y %= WIN_HEIGHT
