from .bullet import Bullet

class WhiteBullet(Bullet):
    def __init__(self, x, y, toX, toY):
        super().__init__(x, y, toX, toY)

        self._radius = 5
        self._color = (190, 190, 190)

        # add damage field
        self._damage = 40
