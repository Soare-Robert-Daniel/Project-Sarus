from game_object import GameObject


class Player(GameObject):
    def __init__(self, image, jump_speed=1, x=0, y=0, tag="Junk"):
        super().__init__(image, x, y, tag)
        self.x_original = x
        self.y_original = y

        self.jump_speed = jump_speed
        self.jump_height = 0
        self.jump_height_limit = 100
        self.fall = False
        self.grounded = True

        self.width, self.height = image.get_size()

        self.obs = None

    def update(self, delta_time):
        if not self.grounded:
            direction = 0  # do nothing
            if self.jumping():
                direction = -1  # go Up
            elif self.falling():
                direction = 1  # go Down
            # Compute the movement on vertical axis (Y)
            # print("Direction: %d, Current y: %d, Height: %d, Limit: %d" % (direction, self.y, self.jump_height, self.jump_height_limit))
            dy = self.jump_speed * delta_time * direction
            self.jump_height -= dy
            self.move(0, dy)

        if self.obs:
            self.obs.check_collision()

    def jump(self, limit=50):
        if self.grounded:
            self.jump_height_limit = limit
            self.fall = False
            self.grounded = False

            if self.obs:
                self.obs.add_jump_distance()

    def jumping(self):
        if self.fall:
            return False
        # Check if we are at the peek
        if self.jump_height > self.jump_height_limit:
            # Reverse the limits
            self.jump_height = self.jump_height_limit
            self.jump_height_limit = 0

            self.fall = True
            return False
        return True

    def falling(self):
        # Check if we are at the ground
        if self.jump_height < self.jump_height_limit:
            self.jump_height = self.jump_height_limit
            self.fall = False
            self.grounded = True
            # set the original Y
            self.y = self.y_original
            return False
        return True
