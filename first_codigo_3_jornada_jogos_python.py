import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("first_codigo_3_jornada_jogos_python.py")
clock = pg.time.Clock()

color1 = (200, 230, 250)
color2 = (250, 160, 60)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((25, 25, 5)) 

    for i in range(8):
        pg.draw.circle(screen, (color1), (100 + i * 70,  240), 7)

    for x in range(60, 600, 40):
        pg.draw.ellipse(screen, (color2), (x, 100, 12, 5))

    for h in range(6):
        pg.draw.rect(screen, (color2[0], 80 + h * 30, 100 + h * 20), (50 + h * 80, 300, 40, 40))

    # pg.draw.circle(screen, (0, 0, 255), (600, 240), 15)
    # pg.draw.circle(screen, (0, 0, 255), (500, 240), 7)
    # pg.draw.circle(screen, (0, 0, 255), (405, 240), 11)
    # pg.draw.circle(screen, (0, 0, 255), (340, 240), 20)
    # pg.draw.circle(screen, (0, 0, 255), (100, 240), 5)

    pg.display.flip()
    clock.tick(60)

pg.quit()