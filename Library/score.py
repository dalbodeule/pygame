class ScoreObj:
    def __init__(self, score, bullet, time):
        self.score = score
        self.bullet = bullet
        self.time = time

    def __repr__(self):
        return "(score → s: {}, b: {}, t: {})".format(self.score, self.bullet, self.time)
