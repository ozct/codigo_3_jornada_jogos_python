import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 500))
pg.display.set_caption("Night Sky")
clock = pg.time.Clock()

font = pg.font.Font(None, 36)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((20, 24, 48))

    radius, rings = 200, 0
    while radius > 10:
        pg.draw.circle(screen, (150, 190, 255), (400, 240), radius, 1)
        radius = radius // 2
        rings  += 1

    text = font.render(f"Rings: {rings}", True, (230, 230, 245))
    screen.blit(text, (20, 20))

    pg.display.flip()
    clock.tick(60)

pg.quit()