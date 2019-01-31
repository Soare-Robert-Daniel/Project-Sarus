from player import Player
import settings


class Bot(Player):
    def __init__(self, image, threshold, jump_speed=1, x=0, y=0, tag="Junk"):
        super().__init__(image, jump_speed, x, y, tag)
        self.threshold = threshold
        self.target = None
        self.jump_height_limit = 120

    def update(self, delta_time):
        if self.grounded:
            # check the distance between the bot and the target (the wall) on it's right side
            if 0 < self.target.x - self.x < self.threshold:
                # print("Distance: %d" % (self.target.x - self.x))
                self.jump(settings.HEIGHT_JUMP_LIMIT_MAX)

        super().update(delta_time)

    def set_target(self, target):
        self.target = target

    def set_threshold(self, threshold):
        self.threshold = threshold
