import pygame


class GameObject:
    def __init__(self, image, x_off=0, y_off=0, tag="Junk"):
        self.img = image
        self.x = x_off
        self.y = y_off
        self.tag = tag
        self.width, self.height = self.img.get_size()

    def update(self, delta_time):
        pass

    def draw(self, display_surf):
        display_surf.blit(self.img, (self.x, self.y))

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def set_location(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    def load_img(self, image):
        self.img = image
        self.width, self.height = image.get_size()
