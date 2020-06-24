from .Bullets.blue_bullet import BlueBullet
from .Bullets.red_bullet import RedBullet
from .Bullets.white_bullet import WhiteBullet

from random import randint as rnint

def Bullet(x, y, toX, toY):
    rnd = rnint(1, 100)

    if rnd <= 50:
        return RedBullet(x, y, toX, toY)
    elif rnd <= 90:
        return BlueBullet(x, y, toX, toY)
    else:
        return WhiteBullet(x, y, toX, toY)
