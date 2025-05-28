# Example file showing a basic pygame "game loop"
import pygame as pg
import function
from function import big_pos

# pygame setup
pg.init()
screen = pg.display.set_mode((900, 1000))
clock = pg.time.Clock()
running = True

cercle = []
croix = []
big_croix = []
big_cercle = []
function.CreateBoard()

def grilles():
    x = 0
    y = 100
    width = 1

    for i in range(9):
        if i == 2 or i == 5:
            width =10
        pg.draw.line(screen, (0,0,0), (x, y), (900, y), width)
        width = 1
        y += 100
    y = 0
    x = 100
    for i in range(9):
        if i == 2 or i == 5:
            width =10
        pg.draw.line(screen, (0,0,0), (x, y), (x, 900), width)
        width = 1
        x += 100


def draw_cross(center, size, width=10):
    half_size = size // 2
    x, y = center

    # Ligne de haut gauche à bas droite
    pg.draw.line(screen, pg.Color("blue"), (x - half_size, y - half_size), (x + half_size, y + half_size), width)

    # Ligne de bas gauche à haut droite
    pg.draw.line(screen, pg.Color("blue"), (x - half_size, y + half_size), (x + half_size, y - half_size), width)

def draw_cercle(center, size, width=10):

    pg.draw.circle(screen, pg.Color("red"), (center), size, width)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            pos = function.DetectClick(x,y)
            big_pos = function.big_pos
            if pos :
                if function.joueur == function.player1:
                    croix.append(pos)
                elif function.joueur == function.player2:
                    cercle.append(pos)
                if function.win == function.player1:
                    big_croix.append(big_pos)
                    function.win = 0
                elif function.win == function.player2:
                    big_cercle.append(big_pos)
                    function.win = 0

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    grilles()

    for pos in cercle:
        draw_cercle(pos,40)

    for pos in croix:
        draw_cross(pos,60)

    for pos in big_croix:
        draw_cross(pos,280)

    for pos in big_cercle:
        draw_cercle(pos,140)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()