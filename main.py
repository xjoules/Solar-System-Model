import pygame as pg
import json
from math import radians, cos, sin, pi
from random import uniform, randrange
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
            star(self, i["Name"], i["Size"], i["Position"]["x"], i["Position"]["y"], color)
        
        for i in INPUT["Planets"]:
            i = INPUT["Planets"][i]
            color = (i["Color"]["r"], i["Color"]["g"], i["Color"]["b"])
            planet(self, i["Name"], i["Orbits"], i["Size"], i["Distance"], i["Velocity"], color)

    def get_body_by_name(self, name):
        for sprite in self:
            if sprite.name == name:
                return sprite


class star(pg.sprite.Sprite):
    def __init__(self, sprite_group, name, size, x, y, color):
        super().__init__(sprite_group)
        self.sprite_group = sprite_group

        self.name = name
        self.size = size
        self.x = x
        self.y = y
        self.color = color

        self.surface = pg.display.get_surface()

    def update(self):
        self.draw()

    def draw(self):
        pos = (self.x, self.y)
        pg.draw.circle(self.surface, self.color, pos, self.size)


class planet(star):
    def __init__(self, sprite_group, name, parent_name, size, distance, velocity, color):
        super().__init__(sprite_group, name, size, 0, 0, color)
        self.parent = sprite_group.get_body_by_name(parent_name)
        self.distance = distance
        self.velocity = velocity

        self.name = name
        self.size = size
        #self.x = self.parent.x + self.distance
        #self.y = self.parent.y
        
        self.color = color

        self.center_of_rotation_x = self.parent.x
        self.center_of_rotation_y = self.parent.y

        self.angle = radians(uniform(0, 360))
        self.x = self.center_of_rotation_x + self.distance * cos(self.angle)
        self.y = self.center_of_rotation_y - self.distance * sin(self.angle)

    def update(self):
        self.center_of_rotation_x, self.center_of_rotation_y = self.parent.x, self.parent.y
        self.x = (self.center_of_rotation_x + self.distance * cos(self.angle))
        self.y = (self.center_of_rotation_y - self.distance * sin(self.angle))
        self.draw()
        self.angle = self.angle + self.velocity
        self.x = self.x + self.distance * self.velocity * cos(self.angle + pi / 2)
        self.y = self.y - self.distance * self.velocity * sin(self.angle + pi / 2)


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
