import settings


class Observer:
    """
        This is the link between the Ai and the environment.
        They keep tracking of the score, distance (between the 'reference object' and the targets) and collisions
    """
    def __init__(self, core, targets=None):
        self.reference_object = core
        self.targets = targets
        self.ai = None

        self.collisions = 0
        self.jump_distances = []

        self.score = 0

    def get_score(self):
        return self.score

    def add_jump_distance(self):
        self.jump_distances.append(self.get_distances())

    def get_distances(self):
        distances = []
        if self.targets and self.reference_object:
            for target in self.targets:
                distances.append(target.x - self.reference_object.x)

        return distances

    def check_collision(self):
        if self.targets and self.reference_object:
            for target in self.targets:
                if self.collide(self.reference_object, target):
                    self.collisions += 1

    def collide(self, rect1, rect2):
        return (rect1.x < rect2.x + rect2.width) and (rect2.x < rect1.x + rect1.width) and \
               (rect1.y < rect2.y + rect2.height) and (rect2.y < rect1.y + rect1.height)

    def check_score(self):
        if self.collisions == 0:
            self.score += 1

    def round_reset(self):
        self.collisions = 0
        self.jump_distances = []

    def reset(self):
        self.round_reset()
        self.score = 0

    def set_reference_object(self, reference_objec):
        if reference_objec:
            self.reference_object = reference_objec

    def set_targets(self, targets=None):
        if targets:
            self.targets = targets

    def set_ai(self, ai):
        if ai:
            self.ai = ai
        else:
            print("NUll AI")

    def add_target(self, target_new):
        if target_new:
            self.targets.append(target_new)

