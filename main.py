import pygame

FPS = 30
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIN_WIDTH = 600
WIN_HEIGHT = 400

pygame.init()
surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
surface.fill(WHITE)
pygame.display.update()

count = 0
d, x, y, t = 30, 0, 0, 10
color_r, color_g, color_b = 0, 0, 0
motion_x, motion_y = 0, 0

while True:

    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                motion_y = 1

            elif event.key == pygame.K_UP:
                motion_y = -1

            elif event.key == pygame.K_LEFT:
                motion_x = -1

            elif event.key == pygame.K_RIGHT:
                motion_x = 1

        elif event.type == pygame.KEYUP and event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            color_r += 10
            color_r %= 255
            color_g -= 10
            color_g %= 255
            color_b *= 2
            color_b %= 255
            motion_x, motion_y = 0, 0

    x += motion_x*t
    x %= WIN_WIDTH
    y += motion_y*t
    y %= WIN_HEIGHT

    count += 1
    if count%30 == 0:
        pygame.display.set_caption('Timer: ' + str(count//30))

    surface.fill(WHITE)
    pygame.draw.rect(surface, (color_r, color_g, color_b), (x, y, d, d))
    if x >= WIN_WIDTH + d:
        x = 0 - d
    else:
        x += 1

    pygame.display.update()

