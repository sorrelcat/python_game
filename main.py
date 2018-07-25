import pygame

FPS = 30
clock = pygame.time.Clock()

pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.update()

count = 0

while True:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    count += 1
    if count%30 == 0:
        pygame.display.set_caption('Timer: ' + str(count//30))
    pygame.display.update()

