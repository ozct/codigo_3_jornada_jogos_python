import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("first_codigo_3_jornada_jogos_python.py")
clock = pg.time.Clock()

color1 = (200, 230, 250)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((25, 25, 5)) 

    for i in range(8):
        pg.draw.circle(screen, (color1), (100 + i * 70,  240), 20)
    # pg.draw.circle(screen, (0, 0, 255), (600, 240), 15)
    # pg.draw.circle(screen, (0, 0, 255), (500, 240), 7)
    # pg.draw.circle(screen, (0, 0, 255), (405, 240), 11)
    # pg.draw.circle(screen, (0, 0, 255), (340, 240), 20)
    # pg.draw.circle(screen, (0, 0, 255), (100, 240), 5)

    pg.display.flip()
    clock.tick(60)

pg.quit()