import pygame

screen = pygame.display.set_mode((800, 640))
pygame.display.set_caption("Subway Simulator")
running = True
clock = pygame.time.Clock()

ItalianBread6InchImage = pygame.image.load("img/Bread/Italian 6-inch.png")
FloorImage = pygame.image.load("img/Background/floor.png")
TomatoesImage = pygame.image.load("img/Vegatables/tomatoes.png")
TomatoesContainer = pygame.image.load("img/Container/tomatoesContainer.png")


subX = 800

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if(pygame.mouse.get_pos() <= (606, 175) and pygame.mouse.get_pos() >= (606+194, 175+258)):
        print("Colliding")

    screen.blit(FloorImage, (0,0))
    screen.blit(ItalianBread6InchImage, (subX, 450))
    screen.blit(TomatoesImage, (subX, 450))
    screen.blit(TomatoesContainer, (606, 175))

    subX-=2

    clock.tick(60)
    pygame.display.flip()
    pygame.display.update()