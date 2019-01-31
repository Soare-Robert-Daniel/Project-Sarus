class Individual:
    def __init__(self, threshold=0):
        self.threshold = threshold
        self.score = 0

    def set_score(self, score):
        self.score = score

    def __str__(self):
        return "Threshold: %d" % self.threshold

    def get_threshold(self):
        return self.threshold
