from game_object import GameObject
import settings
import random


class Wall(GameObject):
    def __init__(self, image, dx=1, x=0, y=0, tag="Junk"):
        super().__init__(image, x, y, tag)
        self.dx = dx
        self.x_original = x
        self.y_original = y
        self.game = None

    def update(self, delta_time):
        self.move(self.dx * delta_time, 0)
        if self.x < 0 - self.width - 10:
            # Load a random wall
            self.load_img(settings.SKINS[random.randint(0, len(settings.SKINS)-1)])
            # Go back to the original location and adjust the height based on the skin size
            self.set_location(self.x_original, self.y_original + settings.WALL_MAX_HEIGHT - self.height)
            if self.game:
                self.game.end_round()

