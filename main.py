import pygame

screen = pygame.display.set_mode((800, 640))
pygame.display.set_caption("Subway Simulator")
running = True
clock = pygame.time.Clock()

ItalianBread6InchImage = pygame.image.load("img/Bread/Italian 6-inch.png")
FloorImage = pygame.image.load("img/Background/floor.png")

subX = 800

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(FloorImage, (0,0))
    screen.blit(ItalianBread6InchImage, (subX, 450))

    subX-=2

    print(subX)

    clock.tick(60)
    pygame.display.update()