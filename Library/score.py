class ScoreObj:
    def __init__(self, score, bullet, time):
        self.score = score
        self.bullet = bullet
        self.time = time

    def __repr__(self):
        return "(score → s: {}, b: {}, t: {})".format(self.score, self.bullet, self.time)

    # compare score (with ScoreObj and float(timestamp))
    def __eq__(self, other):
        if isinstance(other, ScoreObj):
            return bool(self.score == other.score and self.bullet == other.bullet and self.time == other.time)
        elif isinstance(other, float):
            return bool(self.time == other)
        else:
            raise TypeError("{} isan't compare ScoreObj".format(type(other)))
            