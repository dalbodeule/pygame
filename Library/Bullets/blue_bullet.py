from .bullet import Bullet

class BlueBullet(Bullet):
    def __init__(self, x, y, toX, toY):
        super().__init__(x, y, toX, toY)

        self._radius = 6
        self._color = (0, 0, 190)

        # add damage field
        self._damage = 20
