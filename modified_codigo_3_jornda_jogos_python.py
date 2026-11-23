import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Night Sky")
clock = pg.time.Clock()

def draw_star():
    color1 = (200, 230, 250)
    screen.fill((20, 24, 48))
    pg.draw.circle(screen, color1, (400, 240), 200, 3)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    draw_star()
    pg.display.flip()
    clock.tick(30)


pg.quit()