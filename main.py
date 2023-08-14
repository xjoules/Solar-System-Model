import pygame as pg
import json
pg.init()

with open("data.json", "r") as file:
    INPUT = json.load(file)

WIDTH = 1280
HEIGHT = 720
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Project X")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class One(pg.sprite.Group):
    def create(self):
        for i in INPUT["Stars"]:
            i = INPUT["Stars"][i]
            color = (i["Color"]["r"], i["Color"]["g"], i["Color"]["b"])
            star(self,
                i["Name"],
                i["Radius"],
                i["Position"]["x"],
                i["Position"]["y"],
                color
                )


class star(pg.sprite.Sprite):
    def __init__(self, sprite_group, name, radius, x, y, color):
        super().__init__(sprite_group)
        self.sprite_group = sprite_group

        self.name = name
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color

        self.surface = pg.display.get_surface()

    def update(self):
        self.draw()

    def draw(self):
        pos = (self.x, self.y)
        pg.draw.circle(self.surface, self.color, pos, self.radius)
        #print(self.name, self.radius, pos, self.color)

class planet(star):
    def __init__(self, sprite_group, name, star_name, radius, x, y, color):
        super().__init__(sprite_group, name)

def run():
    sprites = One()
    sprites.create()

    clock = pg.time.Clock()
    run = True
    
    while run:
        clock.tick(60)
        WIN.fill(BLACK)

        sprites.update()
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
    pg.quit()

if __name__ == '__main__':
    run()
