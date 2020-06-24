import pygame

class HPBar:
    def __init__(self, screen, maxhp, size):
        self.__maxhp = maxhp
        self.__hp = maxhp
        self.__size = size
        self.__is_show = True

        # add bg
        self.__bg = Rect(screen, (190, 0, 0), size)
        # add hpbar
        self.__hpbar = Rect(screen, (0, 190, 0), size)

    # update hpbar size
    def update(self, hp):
        self.__hp = hp

        # calc and set hp bar size
        self.__hpbar.set_size(hp/self.__maxhp * self.__size)

    def show(self):
        self.__is_show = True

    def hide(self):
        self.__is_show = False

    # draw hpbar
    def draw(self, screen):
        if self.__is_show:
            self.__bg.draw(screen)
            self.__hpbar.draw(screen)

class Rect:
    def __init__(self, screen, color, size):
        self.__size = size
        self.__color = color

        self.update(screen)

    def set_size(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    # set rect position and size
    def update(self, screen):
        width, height = screen.get_size()
        self.__rect = [
            width - self.__size - 20,
            20,
            self.__size,
            20
        ]

    def draw(self, screen):
        # update bar size
        self.update(screen)
        # draw rect
        pygame.draw.rect(screen, self.__color, self.__rect)
