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

def draw_circle(color, pos):
    pygame.draw.circle(surface, color, pos, d)
    pygame.display.update()
    clock.tick(2)

pygame.init()
draw_rect(GREEN)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    if pressed[0]:
        draw_circle(RED, pos)
    if pressed[2]:
        draw_circle(BLUE, pos)

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

    if keys[pygame.K_LSHIFT] and t < 10:
        t += 1

    if keys[pygame.K_RSHIFT] and t > 1:
        t -= 1


    x %= WIN_WIDTH
    y %= WIN_HEIGHT

    '''Напишите код в котором имитируется полет снаряда (пусть его роль сыграет круг) в место клика мышью. 
    Снаряд должен вылетать из нижнего края окна и лететь вверх, т. е. изменяться должна только координата y. 
    Пока летит один, другой не должен появляться. Когда снаряд достигает цели, должен имитировать взрыв, 
    например, в этом месте прорисовываться квадрат.'''