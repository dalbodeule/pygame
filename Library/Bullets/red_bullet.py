from .bullet import Bullet

class RedBullet(Bullet):
    def __init__(self, x, y, toX, toY):
        super().__init__(x, y, toX, toY)

        self._radius = 10
        self._color = (190, 0, 0)

        # add damage field
        self._damage = 10
