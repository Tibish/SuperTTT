# Example file showing a basic pygame "game loop"
import pygame as pg

# pygame setup
pg.init()
screen = pg.display.set_mode((900, 900))
clock = pg.time.Clock()
running = True

def grilles():
    screen.fill("white")

    x = 0
    y = 100
    for i in range(9):
        pg.draw.line(screen, (0,0,0), (x, y), (900, y), 1)
        y += 100
    y = 0
    x = 100
    for i in range(9):
        pg.draw.line(screen, (0,0,0), (x, y), (x, 900), 1)
        x += 100


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    grilles()

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()